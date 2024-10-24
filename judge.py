# File usage -> python judge.py 'testcasefile' 'answerfile'
# Judges the user code against question number on test cases

from importlib import import_module
from ast import literal_eval
from os import path, system
from sys import argv

NUMT = 200  # number of testcases per arg
TESTFILE = argv[1]  # testcase file
ANSFILE = argv[2]  # answer file

# importing expected_code and given_code
expected_code = import_module(f'answers.{ANSFILE}')
given_code = import_module('answers.user')

# getting testcases array ready
testcases = []
with open(f'tests/{TESTFILE}.txt', 'r') as file:
    for line in file:
        testcases.append(literal_eval(line))
n = len(testcases)
args = n//NUMT

# check given code
for i in range(NUMT):
    status = True

    try:
        if args == 1:
            given_ans = given_code.main(testcases[i])
            expected_ans = expected_code.main(testcases[i])
        elif args == 2:
            given_ans = given_code.main(testcases[i], testcases[i + NUMT])
            expected_ans = expected_code.main(testcases[i], testcases[i + NUMT])
        elif args == 3:
            given_ans = given_code.main(testcases[i], testcases[i + NUMT], testcases[i + 2 * NUMT])
            expected_ans = expected_code.main(testcases[i], testcases[i + NUMT], testcases[i + 2 * NUMT])
        else:
            given_ans = given_code.main(testcases[i], testcases[i + NUMT], testcases[i + 2 * NUMT], testcases[i + 3 * NUMT])
            expected_ans = expected_code.main(testcases[i], testcases[i + NUMT], testcases[i + 2 * NUMT], testcases[i + 3 * NUMT])
    except Exception as e:
        print(f"Execution Error, {e}")
        status = False
        break


    if given_ans == expected_ans:
        print(f"testcase {i + 1} passed")
    else:
        print(f"Testcase {i + 1} Failed\n")
        print(f"Testcase:\n{testcases[i]}")
        print(f"Output:\n{given_ans}")
        print(f"Required Output:\n{expected_ans}")
        status = False
        break

print()
if status:
    print("All test cases Successfully Passed!")
else:
    print("Retry...")