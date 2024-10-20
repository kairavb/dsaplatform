import importlib

# importing expected_code and given_code
expected_code = importlib.import_module('answers.a1')
given_code = importlib.import_module('answers.user')

# getting testcases array ready
testcases = []
with open('tests/t1.txt', 'r') as file:
    for line in file:
        testcases.append(line.strip().split())
n = len(testcases)

# check given code
for i in range(n):
    status = True
    given_ans = given_code.main(testcases[i])
    expected_ans = expected_code.main(testcases[i])

    if given_ans == expected_ans:
        print(f"testcase {i} passed")
    else:
        print(f"Testcase {i} Failed\n")
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