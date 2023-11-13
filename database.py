import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()
import os

# Ensure the 'g_string' environment variable is set
connection_string = os.environ['DB_NAME']

engine = create_engine(connection_string, connect_args={"ssl_ca": "C:/Users/arpan/cacert.pem"})


def load_projects_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from projects"))

    result_dicts = []
    for row in result.all():
        result_dicts.append(dict(row._mapping))
    return result_dicts