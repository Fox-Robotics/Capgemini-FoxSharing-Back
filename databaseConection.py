import mysql.connector
from config import DBhost, DBuser, DBpassword, DBname

db = mysql.connector.connect(
    host = DBhost,
    user = DBuser,
    passwd = DBpassword,
    database = DBname
)

mycursor = db.cursor()
