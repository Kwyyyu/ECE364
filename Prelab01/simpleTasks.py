#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <8/21/2019>
#######################################################

import difflib

def find(pattern):
    f = open("sequence.txt", "r")
    contents = f.read()
    sebseq = []
    result = []
    for i in range(len(contents) - len(pattern) + 1):
        temp = contents[i:i + len(pattern)]
        sebseq.append(temp)
    # print(sebseq)
    for i in sebseq:
        match = 1
        for index in range(len(pattern)):
            if pattern[index] != 'x' and pattern[index] != i[index]:
                match = 0
                break
        if match == 1:
            result.append(i)
    # print(result)
    return result


def getStreakProduct(sequence, maxSize, product):
    sebseq = []
    result = []
    for i in range(len(sequence)):
        for j in range(2, maxSize + 1):
            if i + j <= len(sequence):
                temp = sequence[i:i + j]
                sebseq.append(temp)
    # print(sebseq)
    for i in sebseq:
        temp_product = 1
        for j in range(len(i)):
            temp_product = temp_product*int(i[j])
        if temp_product == product:
            result.append(i)
    # print(result)


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





if __name__ == "__main__":
    writePyramids("pyramidtest.txt", 15, 5, '*')

    a = open("pyramidtest.txt",'r').readlines()
    b = open("pyramid15.txt",'r').readlines()
    diff = difflib.ndiff(a, b)
    print('\n'.join(diff))