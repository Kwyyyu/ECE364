#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <8/21/2019>
#######################################################

import difflib
import math
import os

def find(pattern):
    f = open("sequence.txt", "r")
    contents = f.read()
    subseq = []
    result = []
    for i in range(len(contents) - len(pattern) + 1):
        temp = contents[i:i + len(pattern)]
        subseq.append(temp)
    # print(subseq)
    for i in subseq:
        match = 1
        for index in range(len(pattern)):
            if pattern[index] != 'X' and pattern[index] != i[index]:
                match = 0
                break
        if match == 1:
            result.append(i)
    # print(result)
    return result


def getStreakProduct(sequence, maxSize, product):
    subseq = []
    result = []
    for i in range(len(sequence)):
        for j in range(2, maxSize + 1):
            if i + j <= len(sequence):
                temp = sequence[i:i + j]
                subseq.append(temp)
    # print(subseq)
    for i in subseq:
        temp_product = 1
        for j in range(len(i)):
            temp_product = temp_product*int(i[j])
        if temp_product == product:
            result.append(i)
    # print(result)
    return result


def writePyramids(filePath, baseSize, count, char):
    result = []
    row = int((baseSize+1)/2)
    for i in range(0,row):
        for n in range(0,count):
            for j in range(0, row-i-1):
                result.append(" ")
                # print(end=" ")
            for j in range(0, i*2+1):
                result.append(char)
                # print(char,end="")
            for j in range(0, row-i-1):
                result.append(" ")
                # print(end=" ")
            if n < count-1:
                result.append(" ")
            # print(end=" ")
        result.append("\n")
        # print("\r")
    f = open(filePath,"w")
    f.write(''.join(result))
    f.close()
    return result


def getStreaks(sequence, letters):
    result = []
    subseq = []
    letter = []
    temp = []
    for i in range(0, len(letters)):
        letter.append(letters[i])
    i = 0
    while i < len(sequence):
        j = i+1
        while j < len(sequence) and sequence[j] == sequence[i]:
            j += 1
        temp = sequence[i:j]
        subseq.append(temp)
        i = j
    # print(subseq)
    for i in range(len(subseq)):
        for j in letter:
            if j in subseq[i]:
                result.append(subseq[i])
    # print(result)
    return result


def findNames(nameList, part, name):
    names = []
    f_name = []
    l_name = []
    result = []
    for i in range(0, len(nameList)):
        names.append(nameList[i])
        split_name = nameList[i].split()
        f_name.append(split_name[0])
        l_name.append(split_name[1])
    if part == "L":
        for i in range(0, len(l_name)):
            if name.lower() == l_name[i].lower():
                result.append(names[i])
    elif part == "F":
        for i in range(0, len(f_name)):
            if name.lower() == f_name[i].lower():
                result.append(names[i])
    elif part == "FL":
        for i in range(0, len(f_name)):
            if name.lower() == f_name[i].lower() or name.lower() == l_name[i].lower():
                result.append(names[i])
    return result


def convertToBoolean(num, size):
    result = []
    if isinstance(num, int) and isinstance(size, int):
        list_num = []
        i = 0
        while num != 0 or i < size:
            if num != 0:
                bit = num % 2
                list_num.append(bit)
                num = int(num / 2)
            else:
                list_num.append(0)
            i += 1
        list_num.reverse()
        for i in range(0, len(list_num)):
            if list_num[i] == 1:
                result.append(True)
            else:
                result.append(False)
    return result


def convertToInteger(boolList):
    if isinstance(boolList, list) and boolList:
        for i in boolList:
            if type(i) != bool:
                return None
        result = 0
        list_num = []
        for i in range(0, len(boolList)):
            if boolList[i]:
                list_num.append(1)
            else:
                list_num.append(0)
        list_num.reverse()
        for i in range(0, len(list_num)):
            result = result + list_num[i]*pow(2, i)
        return result
    else:
        return None


if __name__ == "__main__":
    names = ["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield",
             "Johnson Cadence"]
    print(findNames(names, "FL", "johnson"))
