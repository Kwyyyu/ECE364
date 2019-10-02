from simpleTasks import *
import difflib

if __name__  == "__main__":
    # Write  anything  here to test  your  code.
    #problem1
    P1_sequence = find ('x38x')

    #problem2
    P2_product = getStreakProduct('54789654321687984', 6, 288)

    #problem3
    writePyramids('testdata1_pyramid.txt', 15, 5, '*')

    #problem4
    P4_streak = getStreaks("AAASSSSSSAPPPSSPPBBCCCSSSSABDJSPIEOWQ", "SACQERD")

    #problem5
    P5_name = findNames(["George Smith", "Mark joHnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"], "LF", "johnson")

    #problem6
    P6_binary = convertToBoolean(123352345,45)

    #problem7
    P7_decimal = convertToInteger(P6_binary)

    with open('testdata1_result_kai.txt', 'w') as f:
        f.write('Problem1: {}\n'.format(P1_sequence))
        f.write('Problem2: {}\n'.format(P2_product))
        f.write('Problem3: {}\n'.format(P4_streak))
        f.write('Problem4: {}\n'.format(P5_name))
        f.write('Problem5: {}\n'.format(P6_binary))
        f.write('Problem6: {}\n'.format(P7_decimal))

    a = open('testdata1_result_kai.txt', 'r')
    b = open('testdata1_result.txt', 'r')
    diff = difflib.ndiff(a.readlines(),b.readlines())
    print(''.join(diff))

    a = open('testdata1_result_kai.txt', 'r')
    b = open('testdata1_result.txt', 'r')
    diff = difflib.ndiff(a.readlines(), b.readlines())
    print(''.join(diff))