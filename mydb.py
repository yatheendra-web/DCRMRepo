#Install Mysql on your computer
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
)
cursorObj = dataBase.connector()

cursorObj.execute("CREATE DATABASE elderco")
print("All Done!")