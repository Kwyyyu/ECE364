#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <9/4/2019>
#######################################################

def getLeastFrequent():
    with open("numbers.dat", 'r') as file:
        content = file.read()
    nums = content.split()
    vmin = 10001
    cmin = 10001
    doc = []
    for i in range(0, len(nums)):
        count = 0
        if nums[i] not in doc:
            doc.append(nums[i])
            for j in range(0, len(nums)):
                if nums[j] == nums[i]:
                    count += 1
            if count < cmin:
                cmin = count
                vmin = nums[i]
    return int(vmin)


def getCodeFor(coordinate):
    result = []
    with open("coordinates.dat", 'r') as file:
        content = file.read()
    record_list = content.split("\n")

    for i in range(2, len(record_list)):
        if len(record_list[i]) > 1:
            components = record_list[i].split()
            if coordinate == float(components[0]) or coordinate == float(components[1]):
                result.append(components[2])
    result.sort()
    return result


def getSubMatrixSum(startRowIndex,endRowIndex,startColumnIndex,endColumnIndex):
    origin_matrix = []
    result = 0
    with open("numbers.dat", 'r') as file:
        content = file.readlines()
    for i in range(len(content)):
        components = content[i].split()
        origin_matrix.append(components)

    nrow = endRowIndex - startRowIndex+1
    ncol = endColumnIndex - startColumnIndex+1
    for i in range(nrow):
        for j in range(ncol):
            result = result + int(origin_matrix[i+startRowIndex][j+startColumnIndex])
    return result



if __name__ == "__main__":
    print(getSubMatrixSum(0,1,0,2))

