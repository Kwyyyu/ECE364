from regexTasks import *
import difflib
from pprint import pprint

if __name__  == "__main__":
    q1 = getUrlParts("http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall")

    q2 = getQueryParameters("http://www.google.com/Math/Const?Pi=3.14&Max_Int=65536&What_Else=Not-Here&Howaboutthis=HA")

    q3 = getSpecial("The TART program runs on Tuesdays and Thursdays, but it does not start until next weet", "t")

    q4 = getRealMAC("The TART program runs on 58:1C-0A-6E-39-4D, but it does not start until next weet")
    # q4 = getRealMAC("The TART program runs on, but it does not start until next week.")

    q5 = getRejectedEntries()

    q6 = getEmployeesWithIDs()

    q7 = getEmployeesWithoutIDs()

    q8 = getEmployeesWithPhones()

    q9 = getEmployeesWithStates()

    q10 = getCompleteEntries()

    with open('testdata_result_kai.txt', 'w') as f:
        f.write('Problem1: {}\n'.format(q1))
        f.write('Problem2: {}\n'.format(q2))
        f.write('Problem3: {}\n'.format(q3))
        f.write('Problem4: {}\n'.format(q4))
        f.write('Problem5: {}\n'.format(q5))
        f.write('Problem6: {}\n'.format(dict(sorted(q6.items()))))
        f.write('Problem7: {}\n'.format(q7))
        f.write('Problem8: {}\n'.format(dict(sorted(q8.items()))))
        f.write('Problem9: {}\n'.format(dict(sorted(q9.items()))))
        f.write('Problem10: {}\n'.format(dict(sorted(q10.items()))))

    a = open('testdata_result_kai.txt', 'r')
    b = open('testdata_result.txt', 'r')
    diff = difflib.ndiff(a.readlines(), b.readlines())
    print(''.join(diff))