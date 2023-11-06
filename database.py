from select import select
import sqlalchemy
from sqlalchemy import create_engine, text



connection_string = "mysql+pymysql://9pi97xuivkh875kmktfm:pscale_pw_nnjHhTqHuc996wkchVSjrnSnXw4MoAtbC8mIVWRsgEg@aws.connect.psdb.cloud:3306/skillskope"


engine = create_engine(connection_string, connect_args={"ssl":{"ssl_ca": "/etc/ssl/cert.pem"}})
print(sqlalchemy.__version__)
def load_projects_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from projects"))
        projects = [row._mapping for row in result.all()]
        return projects



