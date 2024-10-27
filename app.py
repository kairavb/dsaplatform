from flask import Flask, redirect, render_template, request
from waitress import serve
from ast import literal_eval
from random import randint
from time import time

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
        qid = request.form.get("1")

        for _ in range(3):
            qdata.append([data[randint(1,3)][1], 10])

        return redirect("/game")
    else:
        return render_template("index.html")


@app.route("/game", methods=["GET","POST"])
def game():
    if request.method == "POST":

        textarea_content = request.form['textarea']
        with open('user.py', 'w') as f:
            f.write(textarea_content + '\n')

        qdata.pop()
        if len(qdata) == 0:
            return "done" # results screen
        
    else:
        if len(qdata) == 0:
            return redirect("/")
        
    return render_template("index4.html", timer=qdata[-1][1], prblm=qdata[-1][0])


@app.route("/results", methods=["GET","POST"])
def result():
    return render_template("index.html")


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)