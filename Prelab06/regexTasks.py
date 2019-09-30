#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <9/27/2019>
#######################################################

import re
from uuid import UUID
import functools
from pprint import pprint as pp


def getUrlParts(url: str) -> tuple:
    """Take in a URL and return the base address, controller and action values as a tuple."""
    match = re.search(r'(?P<base>[\w.-]+)/(?P<controller>[\w.-]+)/(?P<action>[\w.-]+)', url)
    base = match["base"]
    controller = match["controller"]
    action = match["action"]
    return base, controller, action


def getQueryParameters(url: str) -> list:
    """Take in a URL and return a list of tuples of field and values."""
    match = re.findall(r'(?P<field>[\w.-]+)=(?P<value>[\w.-]+)', url)
    return match


def getSpecial(sentence: str, letter: str) -> list:
    """Take in a sentence and the letter, return a list of words from the sentence that start or end with this letter,
     but not both, regardless of the letter case."""
    match1 = re.findall(r'\b'+letter+r'\w+', sentence, re.IGNORECASE)
    match2 = re.findall(r'\w+'+letter+r'\b', sentence, re.IGNORECASE)
    inter = set(match1).intersection(set(match2))
    match = list(set(match1 + match2) - inter)
    return match


def getRealMAC(sentence: str):
    """Take in a sentence, if it contains a MAC address, return the address, else return None"""
    match1 = re.search(r'\b([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\b', sentence)
    if match1:
        endpoint = match1.span()[1]
        if sentence[endpoint] is not ":" and sentence[endpoint] is not "-":
            return match1.group()
    else:
        return None


@functools.lru_cache()
def getNameMap() -> dict:
    """A map where the key is the employee's name, the value is a tuple of their uuid, phone number and state"""
    final_map = {}
    with open("Employees.dat", "r") as nFile:
        contents = nFile.readlines()
    for record in contents:
        reg1 = r'[A-Za-z]+[,]?[ A-Za-z]+'
        name = re.search(reg1, record).group()
        if "," in name:
            last_name, first_name = name.split(",")
            name = first_name[1:] + " " + last_name
        reg2 = r'[0-9A-Fa-f]{8}-?[0-9A-Fa-f]{4}-?[0-9A-Fa-f]{4}-?[0-9A-Fa-f]{4}-?[0-9A-Fa-f]{12}'
        uuid = re.search(reg2, record).group() if re.search(reg2, record) else None
        if uuid is not None:
            uuid = str(UUID(uuid))
        # if uuid is not None and "-" not in uuid:
        #     uuid = uuid[0:8]+"-"+uuid[8:12]+"-"+uuid[12:16]+"-"+uuid[16:20]+"-"+uuid[20:]
        reg3_1 = r'([(][0-9]{3}[)] [0-9]{3}-[0-9]{4}[;]|[0-9]{3}-[0-9]{3}-[0-9]{4}[;]|[0-9]{10}[;])'
        number = re.search(reg3_1, record).group() if re.search(reg3_1, record) else None
        if number is not None:
            number = number[:len(number)-1]
            if "(" not in number:
                if "-" in number:
                    number = "("+number[0:3]+") "+number[4:]
                else:
                    number = "("+number[0:3]+") "+number[3:6]+"-"+number[6:]
        state = re.search(r'[a-zA-Z ]+$', record).group() if re.search(r'[a-zA-Z ]+$', record) else None
        final_map[name] = (uuid, number, state)
    pp(final_map)
    return final_map


def getRejectedEntries() -> list:
    name_map = getNameMap()
    final_list = []
    for employee in name_map.keys():
        record = name_map[employee]
        uuid, number, state = record
        if uuid == number == state == None:
            final_list.append(employee)
    return sorted(final_list)


def getEmployeesWithIDs() -> dict:
    final_map = {}
    name_map = getNameMap()
    for employee in name_map.keys():
        record = name_map[employee]
        uuid, number, state = record
        if uuid is not None:
            final_map[employee] = uuid
    return final_map


def getEmployeesWithoutIDs() -> list:
    name_map = getNameMap()
    final_list = []
    for employee in name_map.keys():
        record = name_map[employee]
        uuid, number, state = record
        if uuid is None:
            if number or state:
                final_list.append(employee)
    return sorted(final_list)


def getEmployeesWithPhones() -> dict:
    final_map = {}
    name_map = getNameMap()
    for employee in name_map.keys():
        record = name_map[employee]
        uuid, number, state = record
        if number is not None:
            final_map[employee] = number
    return final_map


def getEmployeesWithStates() -> dict:
    final_map = {}
    name_map = getNameMap()
    for employee in name_map.keys():
        record = name_map[employee]
        uuid, number, state = record
        if state is not None:
            final_map[employee] = state
    return final_map


def getCompleteEntries() -> dict:
    final_map = {}
    name_map = getNameMap()
    for employee in name_map.keys():
        record = name_map[employee]
        uuid, number, state = record
        if uuid and number and state:
            final_map[employee] = record
    return final_map


if __name__ == "__main__":
    # print(getUrlParts("http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"))
    # print(getQueryParameters("http://www.google.com/Math/Const?Pi=3.14&Max_Int=65536&What_Else=Not-Here"))
    # print(getSpecial("The TART program runs on Tuesdays and Thursdays, but it does not start until next week.", "t"))
    print(getRealMAC("58:1C:0A:6E:39:4D for test"))
    # (getNameMap())
    # pp(getRejectedEntries())
    # pp(getEmployeesWithIDs())
    # pp(getEmployeesWithoutIDs())
    # pp(getEmployeesWithPhones())
    # pp(getEmployeesWithStates())
    # pp(getCompleteEntries())