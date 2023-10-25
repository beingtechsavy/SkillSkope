import dataclasses
from flask import Flask, jsonify, render_template, request
from flask_marshmallow import Marshmallow
from database import engine
from sqlalchemy import text

app = Flask(__name__)
ma = Marshmallow(app)


class ProjectInfo(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'college', 'skills', 'salary', 'currency', 'responsibilities')


projects_info = ProjectInfo(many=True)


def load_projects_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from projects"))
        projects = [row._mapping for row in result.all()]
        return projects


@app.route("/")
def hello_world():
    projects = load_projects_from_db()
    return render_template('home.html', pro=projects)


@app.route("/api/projects")
def list_projects():
    try:
        projects = load_projects_from_db()
        return jsonify(projects_info.dump(projects))
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
