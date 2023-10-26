from select import select
import sqlalchemy
from sqlalchemy import create_engine, text

# Removed unnecessary import of "sqlalchemy"

connection_string = "mysql+pymysql://h6y63ob127ts1e9nhizp:pscale_pw_WVYUqxAtVTNOwvygvB7v1f43RAcowesXXg9gVP1r0H4@aws.connect.psdb.cloud:3306/skillskope"
# Update connection string with the actual database details

engine = create_engine(connection_string, connect_args={"ssl":{"ssl_ca": "/etc/ssl/cert.pem"}},pool_pre_ping=True,pool_recycle=3600)
print(sqlalchemy.__version__)


