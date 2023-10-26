from select import select
import sqlalchemy
from sqlalchemy import create_engine, text

# Removed unnecessary import of "sqlalchemy"

connection_string = "mysql+pymysql://8o8e7e67yr1nwv462obz:pscale_pw_NPwt077xvg80gEIAFv7oTspg5qkymTYuWK3jOFVHCcu@aws.connect.psdb.cloud:3306/skillskope"
# Update connection string with the actual database details

engine = create_engine(connection_string, connect_args={"ssl":{"ssl_ca": "/etc/ssl/cert.pem"}},pool_pre_ping=True)
print(sqlalchemy.__version__)


