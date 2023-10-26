from select import select
import sqlalchemy
from sqlalchemy import create_engine, text

# Removed unnecessary import of "sqlalchemy"

connection_string = "mysql+pymysql://5zhlgbxd4dll38mnwry7:pscale_pw_mz84wpWoZ49OlLdw798IAv7GgazAnV4a8JKfONrGVbp@aws.connect.psdb.cloud:3306/skillskope"
# Update connection string with the actual database details

engine = create_engine(connection_string, connect_args={"ssl":{"ssl_ca": "/etc/ssl/cert.pem"}},pool_pre_ping=True,pool_recycle=3600)
print(sqlalchemy.__version__)


