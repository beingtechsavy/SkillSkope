from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)



@app.route("/", methods=['GET'])
def hello_world():
    return render_template("home.html")

@app.route("/signup")
def signup():
    return render_template("register.html")

@app.route('/submit', methods=['POST','GET'])
def submit():
    return render_template("project.html")
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
