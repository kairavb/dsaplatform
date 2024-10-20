from importlib import import_module
from ast import literal_eval
from os import path, system

NUMT = 200  # number of testcases per arg
PNUM = 1  # question number

# importing expected_code and given_code
expected_code = import_module(f'answers.a{PNUM}')
given_code = import_module('answers.user')

# read problem test case requirements
with open(f'problems/p{PNUM}.md', 'r') as file:
    name = file.readline().strip()

# if problem testcase not present, create one
if not path.isfile(f'tests/{name}.txt'):
    system(f'python testCaseCreator.py {name}')

# getting testcases array ready
testcases = []
with open(f'tests/{name}.txt', 'r') as file:
    for line in file:
        testcases.append(literal_eval(line))
n = len(testcases)
args = n//NUMT

# check given code
for i in range(NUMT):
    status = True

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