import mysql.connector

mydb=mysql.connector.connect(host='localhost',
                              user='root',
                              password='admin',
                              port='3306',
                              database='mini_project')