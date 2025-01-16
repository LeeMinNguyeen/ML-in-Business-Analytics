from flask import Flask, render_template
from flaskext.mysql import MySQL

import mysql.connector

class mysqlserver():
    def __init__(self, servername, user, password):     
        try:
            self.mysql = MySQL()
            
            # MySQL configurations
            app.config['MYSQL_DATABASE_USER'] = user
            app.config['MYSQL_DATABASE_PASSWORD'] = password
            app.config['MYSQL_DATABASE_DB'] = servername
            app.config['MYSQL_DATABASE_HOST'] = 'localhost'
            
            self.mysql.init_app(app)

            self.conn = self.mysql.connect()
            print("Connection is successful!")

        except mysql.connector.Error as e:
            print("Error =", e)
    
    def runquery(self, query):
        cursor = self.conn.cursor()
        
        cursor.execute(query)
        self.conn.commit()
        
        data = cursor.fetchall()
        
        cursor.close
        
        return data
    
    def create(self, code, name):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO student(code, name) VALUES(%s, %s)", (code, name))
        self.conn.commit()
        print("Insert successfully!")
        cursor.close()
    
    def get_read_query(self, attributes = '*', condition = '', order = '', limit = '', offset = ''):
        
        if condition != '':
            condition = 'WHERE ' + condition
        if order != '':
            order = 'ORDER BY ' + order
        if limit != '':
            limit = 'LIMIT ' + limit
        if offset != '':
            offset = 'OFFSET ' + offset
        
        query = f"""
                SELECT {attributes}
                FROM student
                {condition}
                {order}
                {limit}
                {offset}
                """
        
        return query
    
    def readall(self, attributes = '*', condition = '', order = '', limit = '', offset = ''):
        cursor = self.conn.cursor()
        
        query = self.get_read_query(attributes, condition, order, limit, offset)
        
        cursor.execute(query)
        
        data = cursor.fetchall()
    
        print("ID\tCode\tName")
        for item in data:
            print(item[0], "\t", item[1], "\t", item[2])
        
        cursor.close()
        
    def readmany(self, number, attributes = '*', condition = '', order = '', limit = '', offset = ''):
        cursor = self.conn.cursor()
        
        query = self.get_read_query(attributes, condition, order, limit, offset)
        
        cursor.execute(query)
        
        data = cursor.fetchmany(number)
    
        print("ID\tCode\tName")
        for item in data:
            print(item[0], "\t", item[1], "\t", item[2])
        
        cursor.close()
        
    def readone(self, attributes = '*', condition = '', order = '', limit = '', offset = ''):
        cursor = self.conn.cursor()
        
        query = self.get_read_query(attributes, condition, order, limit, offset)
        
        cursor.execute(query)
        
        data = cursor.fetchone()
    
        print("ID\tCode\tName")
        print(data[0], "\t", data[1], "\t", data[2])
        
        cursor.close()
    
    def update(self, id, code, name):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE student SET code=%s, name=%s WHERE id=%s", (code, name, id))
        self.conn.commit()
        print("Update successfully!")
        cursor.close()
    
    def delete(self, id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM student WHERE id=%s", (id))
        self.conn.commit()
        print("Delete successfully!")
        cursor.close()
    
    def close(self):
        self.conn.close()
        print("MySQL is closed")

app = Flask(__name__)

if __name__ == "__main__":
    student = mysqlserver('k22416c', 'root', 'nguyin')

    data = student.runquery('SELECT * FROM student LIMIT 4 OFFSET 1')

    print("ID\tCode\tName")
    for item in data:
        print(item[0],"\t",item[1],"\t",item[2])
