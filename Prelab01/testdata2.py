from simpleTasks import *
import difflib

if __name__  == "__main__":
    # Write  anything  here to test  your  code.
    #problem1
    P1_sequence = find('5xx3')

    #problem2
    P2_product = getStreakProduct('14257432958', 5, 40)

    #problem3
    writePyramids('testdata2_pyramid_kai.txt', 13, 6, '*')

    #problem4
    P4_streak = getStreaks("AAASSSSSSAPPPSSPPBBCCCSSSSABDJSPIEOWQ", "TSBPO")

    #problem5
    P5_name = findNames(["George Smith", "Mark joHnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"], "T", "johnson")

    #problem6
    P6_binary = convertToBoolean(15,"test")

    #problem7
    bList = [True, False, False, False, False, True, True, 5]
    P7_decimal = convertToInteger(bList)

    with open('testdata2_result_kai.txt', 'w') as f:
        f.write('Problem1: {}\n'.format(P1_sequence))
        f.write('Problem2: {}\n'.format(P2_product))
        f.write('Problem3: {}\n'.format(P4_streak))
        f.write('Problem4: {}\n'.format(P5_name))
        f.write('Problem5: {}\n'.format(P6_binary))
        f.write('Problem6: {}\n'.format(P7_decimal))

    a = open('testdata2_result_kai.txt', 'r')
    # you can change this to your own test2 file
    b = open('testdata1_result.txt', 'r')
    diff = difflib.ndiff(a.readlines(),b.readlines())
    print(''.join(diff))