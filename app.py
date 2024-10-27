from flask import Flask, redirect, render_template, request
from waitress import serve
from ast import literal_eval
from random import randint
from os import system

QRANGE = [1, 3]
qdata = []
data = []
with open(f'data.txt', 'r') as file:
    for line in file:
        data.append(literal_eval(line))

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        global qdata
        qdata = []
        qid = request.form.get("code")

        if qid == 1:
            n, minutes = 3, 10
        elif qid == 2:
            n, minutes = 3, 10
        elif qid == 3:
            n, minutes = 3, 10
        elif qid == 4:
            n, minutes = 3, 10
        elif qid == 5:
            n, minutes = 3, 10
        else:
            n, minutes = 3, 10

        for _ in range(n):
            qdata.append([data[randint(QRANGE[0], QRANGE[1])][0], minutes])
        return redirect("/game")
    else:
        return render_template("index.html")


@app.route("/game", methods=["GET","POST"])
def game():
    if request.method == "POST":
        textarea_content = request.form['textarea']
        with open('user.py', 'w') as f:
            f.write(textarea_content + '\n')
        
        system(f"python judge.py '{data[qdata[-1][0]][1]}' '{data[qdata[-1][0]][3]}'")

        qdata.pop()
        if len(qdata) == 0:
            return "done" # results screen
    else:
        if len(qdata) == 0:
            return redirect("/")

    return render_template("index4.html", timer=qdata[-1][1], prblm=data[qdata[-1][0]][2])


@app.route("/results", methods=["GET","POST"])
def result():
    return render_template("index.html")


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)