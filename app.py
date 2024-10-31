from flask import Flask, redirect, render_template, request
from waitress import serve
from random import sample
from subprocess import run
import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

qdata, resultdata = [], []
score, maxscore = 0, 0

cursor.execute('SELECT * FROM ques')
data = cursor.fetchall()

QRANGE = [0, len(data)]
SCORECARD = [-20, 50 , 70, 100]

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        global qdata, score, maxscore, resultdata
        qdata, resultdata = [], []
        score, maxscore = 0, 0
        qid = int(request.form.get("code"))

        if qid == 1:
            n, minutes = 3, 5
        elif qid == 2:
            n, minutes = 5, 7
        elif qid == 3:
            n, minutes = QRANGE[1], 5
        elif qid == 4:
            n, minutes = QRANGE[1], 7
        elif qid == 5:
            n, minutes = QRANGE[1], 10
        else:
            n, minutes = 10, 10

        qlist = sample(range(QRANGE[0], QRANGE[1]), n)
        for i in qlist:
            qdata.append([data[i][0], minutes, data[i][4]])
        return redirect("/game")
    else:
        return render_template("index.html")


@app.route("/game", methods=["GET","POST"])
def game():
    global score, maxscore, resultdata
    return_code = 0
    output = ''
    if request.method == "POST":
        textarea_content = request.form['textarea']
        with open('answers/user.py', 'w') as f:
            f.write(textarea_content + '\n')
        
        result = run(['python', 'judge.py', f'{data[qdata[-1][0] - 1][1]}', f'{data[qdata[-1][0] - 1][3]}'], capture_output=True, text=True)
        return_code = result.returncode
        output = result.stdout
        
        maxscore += SCORECARD[qdata[-1][2] + 1]
        if return_code == 0:
            score += SCORECARD[qdata[-1][2] + 1]
        else:
            score += SCORECARD[0]
        
        output = "Passed" if len(output) == 0 else output
        resultdata.append([qdata[-1][0], data[qdata[-1][0] - 1][2], output, qdata[-1][2]])

        qdata.pop()
        if len(qdata) == 0:
            return redirect("/result")

    else:
        if len(qdata) == 0:
            return redirect("/")

    return render_template("game.html", timer=qdata[-1][1], prblm=data[qdata[-1][0] - 1][2], score=score)


@app.route("/result")
def result():
    if maxscore == 0:
        return redirect("/")
    else:
        length = len(resultdata)
        return render_template("result.html", score=score, maxscore=maxscore, resultdata=resultdata, length=length)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)