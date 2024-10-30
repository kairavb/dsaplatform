# dsaplatform
A platform to practice dsa questions

to check a code corecction,
it should be

1. compile and run in finite time
2. have best time and space complexity acc to ans
3. correct for all the test cases

the type of test cases should be,

1. base cases
2. edge cases
3. random cases
4. duplicates
5. large inputs
6. special cases

TODO
check code finite compile time
add questions
add comments to code base

Question Data Table Schema
cursor.execute('''
CREATE TABLE IF NOT EXISTS ques (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tcase TEXT NOT NULL,
    image TEXT NOT NULL,
    ansname TEXT NOT NULL,
    tag INTEGER NOT NULL
)
''')