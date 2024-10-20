from random import randrange
from sys import argv


def type_array(n):

    testarrl = randrange(n[0], n[1] + 1)
    testarre = []

    for _ in range(testarrl):
        testarre.append(randrange(n[2], n[3] + 1))

    return testarre

def type_nums(n):

    num = randrange(n[0], n[1] + 1)

    return num

def type_string(n):
    sn = randrange(n[0], n[1] + 1)
    s = ''

    # 48 - 57 nums
    # 65 - 90 smallchr
    # 97 - 122 capchr
    # 32 - 47 58-64 91-96 123-126 syb
    for _ in range(sn):
        s += chr(randrange(32, 126 + 1))
    
    return s


# print("a - a")
# print("b - an")
# print("c - asn")
# print("d - s")
# print("e - sn")
# print("f - n")
# print("g - nn")
# print("h - nnn")
# print("i - ann")
# print("j - ss")


NUMT = 200

# python script.py 'ss 0t200 0t500'
test = argv[1].split()

for i, k in enumerate(test[0]):

    n = test[i + 1].split('t')
    n = list(map(int, n))

    if k == 'a':
        with open(f'tests/{argv[1]}.txt', 'a') as file:
            for _ in range(NUMT):
                file.write(f'{type_array(n)}\n')

    elif k == 's':
        with open(f'tests/{argv[1]}.txt', 'a') as file:
            for _ in range(NUMT):
                file.write(f'{type_string(n)}\n')
    else:
        with open(f'tests/{argv[1]}.txt', 'a') as file:
            for _ in range(NUMT):
                file.write(f'{type_nums(n)}\n')