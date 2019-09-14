#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <9/12/2019>
#######################################################

import os
import functools
from pprint import pprint
from collections import defaultdict

def getTechMap() -> dict:
    ''' A dictionary where the key is the technician's name, the value is the ID. '''
    tech_map = {}
    with open("./maps/technicians.dat", "r") as file:
        tech_list = file.readlines()
    for tech_record in tech_list[2:]:
        temp_record = tech_record.split()
        if len(temp_record) > 0:
            tech_name = temp_record[0]+" "+temp_record[1]
            tech_id = temp_record[3]
            tech_map[tech_name] = tech_id
    return tech_map


def getTechIdMap() -> dict:
    ''' A dictionary where the key is the technician's ID, the value is the name. '''
    tech_map = {}
    with open("./maps/technicians.dat", "r") as file:
        tech_list = file.readlines()
    for tech_record in tech_list[2:]:
        temp_record = tech_record.split()
        if len(temp_record) > 0:
            tech_name = temp_record[0]+" "+temp_record[1]
            tech_id = temp_record[3]
            tech_map[tech_id] = tech_name
    return tech_map


# @functools.lru_cache()
def getReportMap() -> dict:
    ''' A dictionary where the key is the technician's id, the value is the reports ids he/she submitted.'''
    report_map = {}
    for filename in os.listdir('./reports/'):
        with open("./reports/"+filename, "r") as file:
            report_list = file.readlines()
        user_id = report_list[0].split()[2]
        report_map.setdefault(user_id, []).append(filename)
    return report_map


def getVirusMap() -> dict:
    ''' A dictionary where the key is the virus's name, the value is a list of virus id and unit cost.'''
    virus_map = {}
    with open("./maps/viruses.dat", "r") as file:
        virus_list = file.readlines()
    for virus_record in virus_list[2:]:
        if len(virus_record) > 0:
            virus_name, _, virus_id, _, cost = virus_record.split()
            virus_map[virus_name] = [virus_id, cost]
    return virus_map


def getVirusIdMap() -> dict:
    ''' A dictionary where the key is the virus's id, the value is a list of virus name and unit cost.'''
    virus_map = {}
    with open("./maps/viruses.dat", "r") as file:
        virus_list = file.readlines()
    for virus_record in virus_list[2:]:
        temp_record = virus_record.split()
        if len(virus_record) > 0:
            virus_name, _, virus_id, _, cost = virus_record.split()
            virus_map[virus_id] = [virus_name, cost]
    return virus_map


def getTechWork(techName:str) -> dict:
    ''' Get the name of a technician, return a dictionary where key is the virus name, the value is the total number of
    virus used in all his experiments. '''
    tech_map = getTechMap()
    report_map = getReportMap()
    virus_id_map = getVirusIdMap()
    tech_id = tech_map[techName]
    final_map = defaultdict(int)
    if tech_id in report_map.keys():
        report_list = report_map[tech_id]
        for report in report_list:
            with open("./reports/"+report, "r") as file:
                virus_list = file.readlines()
            for vlist in virus_list[4:]:
                if len(vlist) > 0:
                    virus_id = vlist.split()[1]
                    virus_name = virus_id_map[virus_id][0]
                    units = vlist.split()[2]
                    final_map[virus_name] += int(units)
    final_map = {k: v for k, v in final_map.items()}
    return final_map


def getStrainConsumption(virusName:str) -> dict:
    ''' Give a virus name, return a dictionary where the key is the technician name, the value is the virus units number
    used by that technician'''
    virus_map = getVirusMap()
    virus_id = virus_map[virusName][0]
    tech_id_map = getTechIdMap()
    final_map = defaultdict(int)
    for filename in os.listdir('./reports/'):
        with open("./reports/"+filename, "r") as file:
            report_list = file.readlines()
        user_id = report_list[0].split()[2]
        user_name = tech_id_map[user_id]
        for record in report_list[4:]:
            if record.split()[1] == virus_id:
                unit = int(record.split()[2])
                final_map[user_name] += unit
    final_map = {k: v for k, v in final_map.items()}
    return final_map


def getTechSpending() -> dict:
    ''' Return a dictionary where the key is the technician name, the value is cost of all virus units
        used by that technician'''
    virus_id_map = getVirusIdMap()
    tech_id_map = getTechIdMap()
    final_map = defaultdict(float)
    for filename in os.listdir('./reports/'):
        with open("./reports/"+filename, "r") as file:
            report_list = file.readlines()
        user_id = report_list[0].split()[2]
        user_name = tech_id_map[user_id]
        cost = 0.0
        for record in report_list[4:]:
            if len(record) > 0:
                trial, virus_id, unit = record.split()
                unit_cost = virus_id_map[virus_id][1][1:]
                cost += float(unit_cost)*float(unit)
        final_map[user_name] += cost
    final_map = {k: round(v, 2) for k, v in final_map.items()}
    return final_map


def getStrainCost() -> dict:
    ''' Return a dictionary where the key is the virus name, the value is cost of it used in all experiments'''
    final_map = defaultdict(float)
    virus_id_map = getVirusIdMap()
    virus_map = getVirusMap()
    for filename in os.listdir('./reports/'):
        with open("./reports/"+filename, "r") as file:
            report_list = file.readlines()
        for record in report_list[4:]:
            if len(record) > 0:
                trial, virus_id, unit = record.split()
                virus_name = virus_id_map[virus_id][0]
                price = float(virus_map[virus_name][1][1:])
                final_map[virus_name] += float(unit)*price
    final_map = {k: round(v, 2) for k, v in final_map.items()}
    return final_map


def getAbsentTechs() -> set:
    '''return a set of names of the technicians who have not done any experiments'''
    tech_set1 = set(getTechMap().keys())
    tech_set2 = set()
    tech_map = getTechIdMap()
    report_map = getReportMap()
    for tech_id in report_map.keys():
        tech_set2.add(tech_map[tech_id])
    diff = tech_set1 - tech_set2
    return diff


def getUnusedStrains() -> set:
    '''return a set of names of virus that have not been used'''
    virus_set1 = set(getVirusMap().keys())
    virus_set2 = set()
    virus_id_list = set()
    virus_map = getVirusIdMap()
    for filename in os.listdir('./reports/'):
        with open("./reports/"+filename, "r") as file:
            report_list = file.readlines()
        for record in report_list[4:]:
            if len(record) > 0:
                virus_id_list.add(record.split()[1])
    for virus_id in virus_id_list:
        virus_set2.add(virus_map[virus_id][0])
    diff = virus_set1 - virus_set2
    return diff


if __name__ == "__main__":
    pprint(getTechWork("Turner, Theresa"))
    # pprint(getStrainConsumption("Adenoviridae"))
    # pprint(getTechSpending())
    # pprint(getStrainCost())
    # pprint(getAbsentTechs())
    # pprint(getUnusedStrains())