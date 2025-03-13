import mysql.connector
import traceback
import pandas as pd

class Connector:
    def __init__(self, server=None, port=None, database=None, username=None, password=None):
        self.server = server
        self.port = port
        self.database = database
        self.username = username
        self.password = password
    
    def connect(self):
        try:
            self.conn = mysql.connector.connect(host = self.server,
                                                port = self.port,
                                                database = self.database,
                                                user = self.username,
                                                password = self.password)
            print("Connected to MySQL")
        except:
            self.conn = None
            traceback.print_exc()
        return self.conn

    def disConnect(self):
        if self.conn != None:
            self.conn.close()
            
    def GetTableData(self, table):
        if self.conn == None:
            return None
        query = "SELECT * FROM " + table
        return pd.read_sql(query, self.conn)


if __name__ == "__main__":
    conn = Connector(
        server   = 'localhost',
        port     = 3306,
        database = 'sakila',
        username = 'root',
        password = "nguyin"
    )
    conn.connect()