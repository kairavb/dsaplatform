from flask import Flask, redirect, render_template, request
from waitress import serve

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        textarea_content = request.form['textarea']
        
        # Save the content to a file
        with open('output.txt', 'a') as f:
            f.write(textarea_content + '\n')  # Append content with a newline
        
        return 'Content saved successfully!'
    return render_template("index.html")

@app.route("/game", methods=["GET","POST"])
def game():
    if request.method == "POST":
        pass
    else:
        pass
    return render_template("index.html")

@app.route("/results", methods=["GET","POST"])
def result():
    return render_template("index.html")


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)