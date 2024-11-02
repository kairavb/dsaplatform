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
add method to add unique testcases
revert back to data.txt insteat sql bcz i fucked up
now i have to go back to data.txt instead data.db :(

## Question Data Table Schema
run this to create table, sqlite3

CREATE TABLE IF NOT EXISTS ques (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tcase TEXT NOT NULL,
    image TEXT NOT NULL UNIQUE,
    ansname TEXT NOT NULL UNIQUE,
    tag INTEGER NOT NULL CHECK (tag IN (0, 1, 2))
);

add questions with,

```sql
INSERT INTO ques (tcase, image, ansname, tag)
VALUES ('n 1t100', 'ques1', 'ans1', 0);
```

Tags,
0 --> easy
1 --> easy
2 --> hard

Tree
```
.
├── answers
│   ├── ans1.py
│   ├── ans2.py
│   └── user.py
├── app.py
├── data.db
├── judge.py
├── README.md
├── static
│   ├── 1.png
│   └── 2.png
├── templates
│   ├── game.html
│   ├── index.html
│   └── result.html
├── testCaseCreator.py
├── testrun.py
└── tests
    ├── an 1t10t-100t100 -100t100.txt
    └── n 1t100.txt
```

## running code

after cloning, add your own questions (optional)

question images in /static
answers in /answers and sql data table

then in root dir run
```python app.py```