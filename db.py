# pip install pymysql

# conectar db -> host, user, pass, bd
import pymysql 

host = "localhost"
user = "root"
clave = ""
db = "fotografia"

def conexionMySQL():
    return pymysql.connect(host=host, user=user, password=clave, database=db)