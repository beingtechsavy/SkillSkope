
# from select import select
# import sqlalchemy
from sqlalchemy import create_engine, text
import os


connection_string = os.getenv("c_string")


engine = create_engine(connection_string, connect_args={"ssl":{"ssl_ca": "/etc/ssl/cert.pem"}}) # type: ignore
# print(sqlalchemy.__version__)
def load_projects_from_db():
    # with engine.connect() as conn:
    #     result = conn.execute(text("select * from projects"))
    #     projects = [row._mapping for row in result.all()]
    #     return projects
    with engine.connect() as conn:
        result = conn.execute(text("select * from projects"))

    result_dicts = []
    for row in result.all():
        result_dicts.append(dict(row._mapping))
    return result_dicts


