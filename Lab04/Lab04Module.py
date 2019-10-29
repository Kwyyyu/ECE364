#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <9/17/2019>
#######################################################

import os
from pprint import pprint

def getDifference(provider1,provider2):
    Diff = set()
    prov1 = set()
    prov2 = set()
    namelist = os.listdir('./providers/')
    if provider1+".dat" not in namelist:
        raise ValueError("Oops! No such file name as "+provider1+". Please check and try again...")
    elif provider2+".dat" not in namelist:
        raise ValueError("Oops! No such file name as " + provider2 + ". Please check and try again...")
    else:
        with open("./providers/"+provider1+".dat","r") as nfile:
            contents = nfile.readlines()
        for sbc_record in contents[3:]:
            if len(sbc_record) > 0:
                sbc_name = sbc_record.split()[0] + " " + sbc_record.split()[1]
                prov1.add(sbc_name)
        with open("./providers/"+provider2+".dat","r") as nfile:
            contents = nfile.readlines()
        for sbc_record in contents[3:]:
            if len(sbc_record) > 0:
                sbc_name = sbc_record.split()[0] + " " + sbc_record.split()[1]
                prov2.add(sbc_name)
        Diff = prov1 - prov2
        return Diff


def getPriceOf(sbc,provider):
    namelist = os.listdir('./providers/')
    result = 0
    if provider + ".dat" not in namelist:
        raise ValueError("Oops! No such file name as " + provider + ". Please check and try again...")
    else:
        with open("./providers/"+provider+".dat","r") as nfile:
            contents = nfile.readlines()
        for sbc_record in contents[3:]:
            if len(sbc_record) > 0:
                sbc_name = sbc_record.split()[0] + " " + sbc_record.split()[1]
                price = float(sbc_record.split()[3][1:])
                if sbc_name == sbc:
                    result = price
                    break
    if result is 0:
        raise ValueError("Oops! No such SBC name as " + sbc + ". Please check and try again...")
    return result


def checkAllPrices(sbcSet):
    sbc_map = {}
    final_map = {}
    for filename in os.listdir('./providers/'):
        with open('./providers/'+filename, "r") as nfile:
            contents = nfile.readlines()
        for sbc_record in contents[3:]:
            if len(sbc_record) > 0:
                sbc_name = sbc_record.split()[0] + " " + sbc_record.split()[1]
                price = float(sbc_record.split()[3][1:])
                sbc_map.setdefault(sbc_name, []).append([price, filename])
    for sbc in sbcSet:
        price_list = sbc_map[sbc]
        vmin = price_list[0][0]
        provider = price_list[0][1]
        for price_record in price_list:
            if price_record[0] < vmin:
                vmin, provider = price_record
        final_map[sbc] = (vmin, provider[:len(provider)-4])
    return final_map


def getFilter():
    phone_list = []
    final_map = {}
    with open("phones.dat", "r") as nfile:
        contents = nfile.readlines()
    for phone_record in contents[1:]:
        if len(phone_record) > 0:
            name, phone = phone_record.split(",")
            if phone[len(phone)-1] == '\n':
                phone_number = phone[1:4]+phone[6:9]+phone[10:len(phone)-1]
            else:
                phone_number = phone[1:4]+phone[6:9]+phone[10:len(phone)]
            phone_list.append(phone_number)
    for number in phone_list:
        for index in range(len(number)-2):
            new_string = number[index:index+3]
            phone_findlist = []
            for phone in phone_list:
                if new_string in phone:
                    phone_findlist.append(phone)
            if len(phone_findlist) == 1:
                final_map[new_string] = number
    return final_map


if __name__ == "__main__":
    # print(getDifference("provider2","provider4"))
    # print(getPriceOf("Rasp. Pi-4702MQ", "provider2"))
    print(checkAllPrices({"Rasp. Pi-5850EQ","Rasp. Pi-5600U"}))