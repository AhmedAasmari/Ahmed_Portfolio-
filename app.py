from flask import Flask, render_template, request
from database import load_projects_from_db, load_project_from_db, add_message_to_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  projects = load_projects_from_db()
  return render_template('home.html', projects=projects)


@app.route("/project/<id>")
def project_details(id):
  project = load_project_from_db(id)
  return render_template('project_details.html', project=project)


@app.route('/message')
def message():
  return render_template('contactus.html')


@app.route("/message_submitted", methods=['POST'])
def message_submitted():
  mdata = request.form
  add_message_to_db(mdata)
  return render_template('message_submitted.html', data=mdata)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)