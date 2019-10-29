#! /user/local/bin/python3.7

import os
from inspect import getmembers, isfunction


stringFunctions = ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
                   'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
                   'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'ljust', 'lower', 'lstrip',
                   'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
                   'rstrip', 'split', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


def runCheckAgainstStringFunctions():

    fileName = "Lab06Module.py"

    if not os.path.exists(fileName):
        message = f"The file {fileName} was NOT found. No check has been made!"
        print(f"-------------------------------\n{message}\n-------------------------------\n")
        return

    with open(fileName, "r") as cFile:
        lines = cFile.readlines()

    printOut = ""
    functions = set()

    for index, line in enumerate(lines):
        for fn in stringFunctions:
            verb = f".{fn}("

            if verb in line:
                line = line.strip()
                printOut += f'   Fn: "{fn}()" => Line({index:03d}): "{line}"\n'
                functions.add(f"{fn}()")

    if printOut:
        fnStr = ", ".join(functions)
        message = (f"The file {fileName} contains one or more string functions that cannot be used.\n"
                   f"Please remove these functions, or you might get 0.\n\n"
                   f"Functions Used: {fnStr}\n\n"
                   f"Location Details:\n{printOut}")
    else:
        message = f"The file '{fileName}' has been checked, and it does not contain any unacceptable string functions."

    print(f"-------------------------------\n{message}\n-------------------------------\n")


def checkFunctionNames():
    # Define desired functions that should be present.
    functionNames = ['getGenres', 'getAuthorOf', 'getBookInfo', 'getBooksBy', 'getBooksBelow', 'searchForWord']

    # Attempt to import the code, and fail otherwise.
    try:
        import Lab06Module as student

    except:
        print("-------------------------------")
        print("Unable to find expected file.")
        print("-------------------------------")
        print()
        exit(-1)
    else:
        print("-------------------------------")
        print("Code file imported successfully.")
        print("-------------------------------")
        print()

    # Obtain all functions in the code.
    presentFunctions = [fnName for fnName, _ in getmembers(student, isfunction)]

    # Check whether each function is present or missing, and print out the result.
    for fnIndex, fnName in enumerate(functionNames):

        if fnName in presentFunctions:
            print('{}- Function "{}" located.'.format(fnIndex + 1, fnName))
        else:
            print('{}- =======> Unable to locate the function "{}".'.format(fnIndex + 1, fnName))


if __name__ == "__main__":
    runCheckAgainstStringFunctions()
    checkFunctionNames()
