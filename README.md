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
generate better testcases as shown above
check code finite compile and run as shown above
a interface to interact and play
result screen makeover
add questions
add comments to code base
resizer highlight
add a sql data, for questions/results (im so tired!)
data.txt and result.txt
['prblmid', 'testcasefile', 'prblmname', 'answername', 'prblmquality']
['qid', 'q name', 'q result', 'tag']

cursor.execute('''
CREATE TABLE IF NOT EXISTS ques (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tcase TEXT NOT NULL,
    image TEXT NOT NULL,
    ansname TEXT NOT NULL,
    tag INTEGER NOT NULL
)
''')