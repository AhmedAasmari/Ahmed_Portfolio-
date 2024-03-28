from sqlalchemy import create_engine,text
import os

engine = create_engine(os.environ['DB_CONNECTION_STRING'])

def load_projects_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from Myprojects"))
    projects = []
    for row in result.all():
      projects.append(dict(row._mapping))
    return projects
    

def load_project_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"select * from Myprojects where id ={id}"))
    row = result.all()
    return dict(row[0]._mapping)

def add_message_to_db(data):
  with engine.connect() as conn:
    sql = text(
        f"INSERT INTO mymessages (full_name, email, message) VALUES (\'{data['full_name']}\', \'{data['email']}\', \'{data['message']}\')"
    )
    conn.execute(sql)
    conn.commit()