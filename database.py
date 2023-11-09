import os
from sqlalchemy import create_engine, text

# Ensure the 'g_string' environment variable is set
connection_string = os.environ.get('g_string')
print(connection_string)
if connection_string is None:
    raise ValueError("Environment variable 'g_string' is not set.")

engine = create_engine(connection_string, connect_args={"ssl_ca": "/etc/ssl/cert.pem"})

def load_projects_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from projects"))

    result_dicts = []
    for row in result.all():
        result_dicts.append(dict(row._mapping))
    return result_dicts