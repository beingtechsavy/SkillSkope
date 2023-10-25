from select import select
import sqlalchemy
from sqlalchemy import create_engine, text

# Removed unnecessary import of "sqlalchemy"

connection_string = "mysql+pymysql://xnyprwssnte8n4e9x6dk:pscale_pw_DDazoNkh8O2TTUcUZ2xLgOfjwHGD5Pes4ruhrszwkAI@aws.connect.psdb.cloud:3306/skillskope"
# Update connection string with the actual database details

engine = create_engine(connection_string, connect_args={"ssl":{"ssl_ca": "/etc/ssl/cert.pem"}},pool_pre_ping=True)
print(sqlalchemy.__version__)


