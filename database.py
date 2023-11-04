from select import select
import sqlalchemy
from sqlalchemy import create_engine, text



connection_string = "mysql+pymysql://60fzbfh3luw5zb3lurn9:pscale_pw_87jI6xyaB8D3m5bqpnYU3Tvx4PFWJX9vAuAC2csXbb0@aws.connect.psdb.cloud:3306/skillskope"



engine = create_engine(connection_string, connect_args={"ssl":{"ssl_ca": "/etc/ssl/cert.pem"}},pool_pre_ping=True,pool_recycle=3600)
print(sqlalchemy.__version__)



