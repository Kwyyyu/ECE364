#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <9/11/2019>
#######################################################

from pprint import pprint

def getMonthlyVolume():
    result = {}
    with open("stocks.dat", "r") as nFile:
        contents = nFile.readlines()

    for i in range(2, len(contents)):
        if len(contents[i])>0:
            text = contents[i].split(",")
            month = text[0][0:7]
            if month in result.keys():
                result[month] += int(float(text[2]))
            else:
                result[month] = int(float(text[2]))
    return result


def getCommonDays(year1,year2):
    year_map = {}
    result = set()
    with open("stocks.dat", "r") as nFile:
        contents = nFile.readlines()
    for i in range(2, len(contents)):
        if len(contents[i]) > 0:
            text = contents[i].split(",")
            year = text[0][0:4]
            day = text[0][5:10]
            year_map.setdefault(year, []).append(day)
    year1_list = set(year_map[year1])
    year2_list = set(year_map[year2])
    common_day = year1_list & year2_list
    for i in common_day:
        month = i[0:2]
        day = i[3:5]
        temp_list = [month, day]
        day_tuple = tuple(temp_list)
        result.add(day_tuple)
    return result


def getNamesBySymbol(n):
    with open("transactions.dat", "r") as nFile:
        contents = nFile.readlines()
    name_map = {}
    company_map = {}
    company_set = set()
    for i in range(len(contents)):
        if len(contents[i]) > 0:
            text = contents[i].split()
            name = text[0]
            for j in range(1, len(text)):
                name_map.setdefault(name, []).append(text[j][:len(text[j])-1])
                company_set.add(text[j][:len(text[j])-1])
    for i in company_set:
        name_set = set()
        for j in name_map.keys():
            count = 0
            temp_list = name_map[j]
            for k in range(len(temp_list)):
                if temp_list[k] == i:
                    count += 1
            if count >= n:
                name_set.add(j)
        #print(i,name_set)
        if name_set:
            company_map[i] = name_set
    return company_map


if __name__ == "__main__":
    pprint(getNameBySymbol(5))
