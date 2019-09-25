#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <8/29/2019>
#######################################################

import os
import sys


def getMaxDifference(symbol):
    for root, dirs, files in os.walk('.'):
        name = symbol + ".dat"
        if name in files:
            with open(name, "r") as nFile:
                contents = nFile.read()
            vmax = -1
            date = -1
            record_list = contents.split("\n")
            for i in range(2, len(record_list)):
                if len(record_list[i]) > 1:
                    components = record_list[i].split(",")
                    delta = float(components[4]) - float(components[5])
                    if delta > vmax:
                        date = components[0]
                        vmax = delta
            return date
        else:
            return None


def getGainPercent(symbol):
    for root, dirs, files in os.walk('.'):
        name = symbol + ".dat"
        if name in files:
            with open(name, "r") as nFile:
                contents = nFile.read()
            sum = 0
            num = 0
            record_list = contents.split("\n")
            for i in range(2, len(record_list)):
                if len(record_list[i]) > 1:
                    sum += 1
                    components = record_list[i].split(",")
                    delta = float(components[1]) - float(components[3])
                    if delta > 0:
                        num += 1
            return "%.4f" % (num/sum*100)
        else:
            return None


def getVolumeSum(symbol, date1, date2):
    for root, dirs, files in os.walk('.'):
        name = symbol + ".dat"
        if name in files and date2 > date1:
            with open(name, "r") as nFile:
                contents = nFile.read()
            vsum = 0
            flag = 0
            record_list = contents.split("\n")
            for i in range(2, len(record_list)):
                if len(record_list[i]) > 1:
                    components = record_list[i].split(",")
                    if components[0] == date2:
                        flag = 1
                    if flag == 1:
                        vsum += float(components[2])
                    if components[0] <= date1:
                        break
            return int(vsum)
        else:
            return None


def getBestGain(date):
    for root, dirs, files in os.walk('.'):
        type = ".dat"
        vmax = -1
        for j in files:
            if type in j:
                with open(j, "r") as nFile:
                    contents = nFile.read()
                record_list = contents.split("\n")
                for i in range(2, len(record_list)):
                    if len(record_list[i]) > 1:
                        components = record_list[i].split(",")
                        if components[0] == date:
                            gain = (float(components[1])-float(components[3]))/float(components[3])*100
                            if gain > vmax:
                                vmax = gain
                            break
        return "%.4f" % vmax


def getAveragePrice(symbol, year):
    for root, dirs, files in os.walk('.'):
        name = symbol + ".dat"
        if name in files:
            with open(name, "r") as nFile:
                contents = nFile.read()
            vsum = 0
            sum = 0
            record_list = contents.split("\n")
            for i in range(2, len(record_list)):
                if len(record_list[i]) > 1:
                    components = record_list[i].split(",")
                    if str(year) in components[0]:
                        avg = (float(components[1])+float(components[3]))/2
                        vsum += avg
                        sum += 1
            return "%.4f" % (vsum/sum)
        else:
            return None


def getCountOver(symbol, price):
    for root, dirs, files in os.walk('.'):
        name = symbol + ".dat"
        if name in files:
            with open(name, "r") as nFile:
                contents = nFile.read()
            record_list = contents.split("\n")
            count = 0
            for i in range(2, len(record_list)):
                if len(record_list[i]) > 1:
                    components = record_list[i].split(",")
                    if float(components[1]) >= price and float(components[3]) >= price and float(components[4]) >= price and float(components[5]) >= price:
                        count += 1
            return count
        else:
            return None


if __name__ == "__main__":
    print(getAveragePrice('AMZN', 2017),getBestGain("2017/01/11"))