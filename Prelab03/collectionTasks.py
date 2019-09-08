#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <9/4/2019>
#######################################################

import os
import sys
from pprint import pprint


def getProjectMap():
    map = {}
    with open("./maps/projects.dat", "r") as file:
        projects = file.readlines()
    for i in range(2, len(projects)):
        if len(projects[i]) > 1:
            text = projects[i].split()
            map.setdefault(text[1], []).append(text[0])
    return map


def getCircuitMap():
    map = {}
    with open("./maps/projects.dat", "r") as file:
        projects = file.readlines()
    for i in range(2, len(projects)):
        if len(projects[i]) > 1:
            text = projects[i].split()
            map.setdefault(text[0], []).append(text[1])
    return map


def getStudentMap():
    map = {}
    with open("./maps/students.dat", "r") as file:
        projects = file.readlines()
    for i in range(2, len(projects)):
        if len(projects[i]) > 1:
            text = projects[i].split()
            map[text[0]+" "+text[1]] = text[3]
    return map


def getStudentidMap():
    map = {}
    with open("./maps/students.dat", "r") as file:
        projects = file.readlines()
    for i in range(2, len(projects)):
        if len(projects[i]) > 1:
            text = projects[i].split()
            map[text[3]] = text[0]+" "+text[1]
    return map


def getComponentCountByProject(projectID,componentsSymbol):
    parts = []
    result = ""
    fname = "None"

    # get the list of circuit
    project_map = getProjectMap()
    circuit = project_map[projectID]

    # with open("./maps/projects.dat", "r") as file:
    #     projects = file.readlines()
    # for i in range(2, len(projects)):
    #     if len(projects[i]) > 1:
    #         text = projects[i].split()
    #         if text[1] == projectID:
    #             circuit.append(text[0])

    # decide which component
    file_map = {
        "R": "resistors.dat",
        "I": "inductors.dat",
        "C": "capacitors.dat",
        "T": "transistors.dat"
    }

    if componentsSymbol not in ["R", "T", "C", "I"]:
        filename = "None"
    else:
        filename = file_map[componentsSymbol]

        # get the component's name list
        with open("./maps/"+filename, "r") as file:
            components = file.readlines()
        for i in range(3, len(components)):
            if len(components[i]) > 1:
                text = components[i].split()
                parts.append(text[0])

        if len(circuit) > 0:
            result = 0
            for root, dirs, files in os.walk('./circuits/'):
                for i in circuit:
                    name = "circuit_" + i + ".dat"
                    if name in files:
                        with open('./circuits/'+name, "r") as nFile:
                            contents = nFile.readlines()
                        for k in range(len(contents)):
                            if contents[k].strip() in parts:
                                result += 1
    if result == "":
        raise ValueError("Oops! No such project ID. Please check and try again...")
    return result
    # try:
    #     return int(result)
    # except ValueError:
    #     print("Oops! No such project ID. Please check and try again...")


def getComponentCountByStudent(studentName,componentsSymbol):
    student_id = 0
    parts = []
    # get the student's name list
    with open("./maps/students.dat", "r") as file:
        students = file.readlines()
    for i in range(2, len(students)):
        if len(students[i]) > 1:
            text = students[i].split()
            if studentName in students[i]:
                student_id = text[3]
    if student_id == 0:
        result = "None"
        raise ValueError("Oops! No such student name. Please check and try again...")
    else:
        result = 0
        # decide which component
        file_map = {
            "R": "resistors.dat",
            "I": "inductors.dat",
            "C": "capacitors.dat",
            "T": "transistors.dat"
        }
        if componentsSymbol not in ["R", "T", "C", "I"]:
            filename = "None"
        else:
            filename = file_map[componentsSymbol]
            # get the component's name list
            with open("./maps/" + filename, "r") as file:
                components = file.readlines()
            for i in range(3, len(components)):
                if len(components[i]) > 1:
                    text = components[i].split()
                    parts.append(text[0])
            # go through the circuits and find parts
            for root, dirs, files in os.walk('./circuits/'):
                for i in files:
                    with open('./circuits/' + i, "r") as nFile:
                        contents = nFile.readlines()
                    flag = 0
                    for k in range(len(contents)):
                        if student_id in contents[k].strip():
                            flag = 1
                            break
                    if flag == 1:
                        for j in range(len(contents)):
                            if contents[j].strip() in parts:
                                result += 1
    return result
    # try:
    #     return int(result)
    # except ValueError:
    #     print("Oops! No such student name. Please check and try again...")


def getParticipationByStudent(studentName):
    student_id = 0
    circuit = []
    project = []
    # get the student's name list
    with open("./maps/students.dat", "r") as file:
        students = file.readlines()
    for i in range(2, len(students)):
        if len(students[i]) > 1:
            text = students[i].split()
            if studentName in students[i]:
                student_id = text[3]
    if student_id == 0:
        result = 0
        raise ValueError("Oops! No such student name. Please check and try again...")
    else:
        result = {}
        # go through the circuits and find participated ones
        for root, dirs, files in os.walk('./circuits/'):
            for i in files:
                with open('./circuits/' + i, "r") as nFile:
                    contents = nFile.readlines()
                for k in range(len(contents)):
                    if student_id in contents[k].strip():
                        circuit.append(i[8:len(i)-4])
                        break
        # get the project
        circuit_map = getCircuitMap()
        for i in circuit:
            project += circuit_map[i]
        result = set(project)
    return set(result)


def getParticipationByProject(projectID):
    project_map = getProjectMap()
    result = []
    if projectID not in project_map.keys():
        raise ValueError("Oops! No such project ID. Please check and try again...")
    else:
        circuit_id = project_map[projectID]
        studentid_map = getStudentidMap()
        # go through the circuit files and find students
        for root, dirs, files in os.walk('./circuits/'):
            for i in files:
                if i[8:len(i)-4] in circuit_id:
                    with open('./circuits/' + i, "r") as nFile:
                        contents = nFile.readlines()
                    for j in range(len(contents)):
                        if contents[j].strip() in studentid_map.keys():
                            result.append(studentid_map[contents[j].strip()])
    return set(result)


def getCostOfProjects():
    project_list = list(getProjectMap().keys())
    cost_map = {}
    for i in project_list:
        parts = []
        result = 0.00
        circuits = getProjectMap()[i]
        for root, dirs, files in os.walk('./circuits/'):
            for j in files:
                if j[8:len(j)-4] in circuits:
                    with open('./circuits/' + j, "r") as nFile:
                        contents = nFile.readlines()
                    ind = 0
                    for k in range(len(contents)):
                        if "Components" in contents[k]:
                            ind = k + 2
                    for k in range(ind, len(contents)):
                        if len(contents[k]) > 0:
                            parts.append(contents[k].strip())
        for filename in ["resistors.dat", "capacitors.dat", "transistors.dat", "inductors.dat"]:
            with open("./maps/" + filename, "r") as file:
                components = file.readlines()
            for j in range(3, len(components)):
                if len(components[j]) > 1:
                    text = components[j].split()
                    if text[0] in parts:
                        price = text[1]
                        result += float(price[1:])
        cost_map[i] = "{0:.2f}".format(result)
    return cost_map


def  getProjectByComponent(componentIDs):
    result = {}
    circuit_list = []
    project_list = []
    for root, dirs, files in os.walk('./circuits/'):
        for i in files:
            with open('./circuits/' + i, "r") as nFile:
                contents = nFile.readlines()
            for j in range(len(contents)):
                if contents[j].strip() in componentIDs:
                    circuit_list.append(i[8:len(i)-4])
                    break
    for i in circuit_list:
        projects = getCircuitMap()[i]
        project_list += projects
    result = set(project_list)
    return result


def getCommonByProject(projectID1, projectID2):
    project_map = getProjectMap()
    two_set = []
    if projectID1 not in project_map.keys():
        raise ValueError("Oops! No such project ID. Please check and try again...")
    else:
        for i in [projectID1, projectID2]:
            parts = set()
            circuit_list = getProjectMap()[i]
            for root, dirs, files in os.walk('./circuits/'):
                for j in files:
                    if j[8:len(j) - 4] in circuit_list:
                        with open('./circuits/' + j, "r") as nFile:
                            contents = nFile.readlines()
                        ind = 0
                        for k in range(len(contents)):
                            if "Components" in contents[k]:
                                ind = k + 2
                        for k in range(ind, len(contents)):
                            if len(contents[k]) > 0:
                                parts.add(contents[k].strip())
            two_set.append(parts)
        result = two_set[0] & two_set[1]
    return sorted(result)



def getComponentReport(componentIDs):
    result = dict.fromkeys(list(componentIDs), 0)
    project_map = getProjectMap()
    for index in project_map.keys():
        circuit_list = project_map[index]
        for root, dirs, files in os.walk('./circuits/'):
            for i in files:
                if i[8:len(i) - 4] in circuit_list:
                    with open('./circuits/' + i, "r") as nFile:
                        contents = nFile.readlines()
                    for k in range(len(contents)):
                        if contents[k].strip() in componentIDs:
                            result[contents[k].strip()] += 1
    return result


def getCircuitByStudent(studentNames):
    id_list = []
    circuit_id = set()
    for name in studentNames:
        id_list.append(getStudentMap()[name])
    for root, dirs, files in os.walk('./circuits/'):
        for i in files:
            with open('./circuits/' + i, "r") as nFile:
                contents = nFile.readlines()
            for k in range(len(contents)):
                if contents[k].strip() in id_list:
                    circuit_id.add(i[8:len(i) - 4])
                    break
    return circuit_id


def getCircuitByComponent(componentIDs):
    circuit_id = set()
    for root, dirs, files in os.walk('./circuits/'):
        for i in files:
            with open('./circuits/' + i, "r") as nFile:
                contents = nFile.readlines()
            for k in range(len(contents)):
                if contents[k].strip() in componentIDs:
                    circuit_id.add(i[8:len(i) - 4])
                    break
    return circuit_id


if __name__ == "__main__":
    T = getParticipationByProject("082D6241-40EE-432E-A635-65EA8AA374B6")
    #T = getCommonByProject("082D6241-40EE-432E-A635-65EA8AA374B6","77A1A82E-749E-43BF-B3BF-3E70F087F808")
    pprint(T)
