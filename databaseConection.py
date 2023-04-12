import mysql.connector
db = mysql.connector.connect(
    host = DBhost,
    user = DBuser,
    passwd = DBpassword,
    database = DBname
)

mycursor = db.cursor()
