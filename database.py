from select import select
import sqlalchemy
from sqlalchemy import create_engine, text

# Removed unnecessary import of "sqlalchemy"

connection_string = "mysql+pymysql://lrk67ujurl06a80dm7vc:pscale_pw_JDr7cU6xg8GZSvj7OEOrfpXGOKZhGBpw3POBm2KT6yj@aws.connect.psdb.cloud:3306/skillskope"
# Update connection string with the actual database details

engine = create_engine(connection_string, connect_args={"ssl":{"ssl_ca": "/etc/ssl/cert.pem"}})
print(sqlalchemy.__version__)


