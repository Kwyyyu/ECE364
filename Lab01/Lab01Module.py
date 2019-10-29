#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <8/21/2019>
#######################################################

def searchForNumber():
    num = 10
    while 1:
        sum = 0
        for i in range(2, 7):
            temp = num*i
            list1 = list(str(num))
            list2 = list(str(temp))
            list1.sort()
            list2.sort()
            if list1 == list2:
                sum += 1
            else:
                break
        if sum == 5:
            return num
        num += 1


def calculateChain():
    imax = -1
    vmax = -1
    for i in range(13, 1000001):
        list1 = []
        num = i
        while num > 1:
            if num % 2 == 0:
                num = num//2
            else:
                num = num*3+1
            list1.append(num)
        if len(list1) > vmax:
            imax = i
            vmax = len(list1)
    return imax


# def calculateTensor(M1,M2):
#     M_final = []
#     M_temp = []
#     M_temp2 = []
#     print(len(M1)*len(M2[0]),len(M1[0])*len(M2))
#     for i in M1:
#         for j in i:
#             print(j, M2)
#             for t in range(len(M2)):
#                 for k in range(len(M2[t])):
#                     M_temp.append(int(M2[t][k])*int(j))
#                     print("M1,", M_temp)
#     print("M1,",M_temp)
#     for i in range(len(M1)):
#         for j in range(len(M2[0])):
#             temp = M_temp[i*len(M2):(i+1)*len(M2)]
#         M_final.append(temp)
#
#     print(M_final)






