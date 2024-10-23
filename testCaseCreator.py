# File usage -> python script.py 'ss 0t200 0t500'
# 'ss 0t200 0t500' is testcase constraint, a - array, s - string, n - number, t - to
# Generates test cases on given code constraints

from random import randint, choice
from sys import argv


def type_array(n):
    testcases = []
    edgecases = [
        [n[2]] * n[1],
        [n[3]] * n[1],
        [n[2]] * n[0],
        [n[3]] * n[0],
        [randint(n[2], n[3]) for _ in range(n[0], n[1]  + 1)],
        [randint(n[2], n[3]) for _ in range(n[0], n[1]  + 1)]
    ]

    testcases.extend(edgecases)

    while len(testcases) < NUMT:
        randomcase = [randint(n[2], n[3]) for _ in range(n[0], min(n[1], 100) + 1)]
        testcases.append(randomcase)
    
    return testcases

def type_nums(n):
    testcases = []
    edgecases = [n[0], n[1]]
    testcases.extend(edgecases)

    while len(testcases) < NUMT:
        randomcase = randint(n[0], min(n[1], 10**7))
        testcases.append(randomcase)

    return testcases

def type_string(n):
    testcases = []

    stringtype = [chr(i) for i in range(65, 91)]
    stringtype.extend([chr(i) for i in range(97, 123)])
    stringtype.extend([chr(i) for i in range(48, 58)])

    edgecases = [
        ''.join(choice(stringtype) for _ in range(n[0], n[1] + 1)),
        ''.join(choice(stringtype) for _ in range(n[0], n[1] + 1)),
        ''.join(choice(stringtype) for _ in range(n[0], n[0] + 1))
    ]
    testcases.extend(edgecases)

    while len(testcases) < NUMT:
        randomcase = ''.join(choice(stringtype) for _ in range(n[0], min(n[1], 100) + 1))
        testcases.append(randomcase)
    
    return testcases


NUMT = 500  # number of testcases per arg

test = argv[1].split()  # testcase constraint

for i, k in enumerate(test[0]):

    n = test[i + 1].split('t')
    n = list(map(int, n))

    if k == 'a':
        with open(f'tests/{argv[1]}.txt', 'a') as file:
            tests = type_array(n)
            for i in tests:
                file.write(f'{i}\n')

    elif k == 's':
        with open(f'tests/{argv[1]}.txt', 'a') as file:
            tests = type_string(n)
            for i in tests:
                file.write(f'{i}\n')
    else:
        with open(f'tests/{argv[1]}.txt', 'a') as file:
            tests = type_nums(n)
            for i in tests:
                file.write(f'{i}\n')