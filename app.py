from flask import Flask, jsonify, render_template, request
from database import load_projects_from_db
from sqlalchemy import text

app = Flask(__name__)

@app.route("/")
def hello_world():
    projects = load_projects_from_db()
    return render_template('home.html', pro=projects)


@app.route("/api/projects")
def list_projects():
    try:
        projects = load_projects_from_db()
        return jsonify(projects)
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
