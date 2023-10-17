from flask import Flask, jsonify, render_template, request, redirect, url_for


app = Flask(__name__)

Project=[{
    'id':1,
    'title':'healthcare website',
    'College':'ITER',
    'skills':'React js',
    'salary':1500000
},
{
    'id':2,
    'title':'Arduino robot',
    'College':'NIT',
    'skills':'Machine Learning',
    'salary':15000
},
{
    'id':3,
    'title':'fitness mobile app',
    'College':'NIST',
    'skills':'Java'
    
}]

@app.route("/")
def hello_world():
    return render_template('home.html',pro=Project)

@app.route("/api/projects")
def list_projects():
    return jsonify(Project)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
