from collection2Tasks import *
import difflib
from pprint import pprint

if __name__  == "__main__":
    # problem 1
    q1 = getTechWork("Turner, Theresa")
    q1_sorted = dict(sorted(q1.items()))

    # problem2
    q2 = getStrainConsumption("Cardiovirus")
    q2_sorted = dict(sorted(q2.items()))

    # problem3
    q3 = getTechSpending()
    q3_sorted = dict(sorted(q3.items()))

    # problem4
    q4 = getStrainCost()
    q4_sorted = dict(sorted(q4.items()))

    # problem5
    q5 = getAbsentTechs()

    # problem6
    q6 = getUnusedStrains()

    with open('testdata_result_kai.txt', 'w') as f:
        f.write('Problem1: {}\n'.format(q1_sorted))
        f.write('Problem2: {}\n'.format(q2_sorted))
        f.write('Problem3: {}\n'.format(q3_sorted))
        f.write('Problem4: {}\n'.format(q4_sorted))
        f.write('Problem5: {}\n'.format(sorted(q5)))
        f.write('Problem6: {}\n'.format(sorted(q6)))

    a = open('testdata_result_kai.txt', 'r')
    b = open('testdata_result.txt', 'r')
    diff = difflib.ndiff(a.readlines(), b.readlines())
    print(''.join(diff))