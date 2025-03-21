import mysql.connector
import traceback
import pandas as pd

class Connector:
    def __init__(self,server=None, port=None, database=None, username=None, password=None):
        self.server=server
        self.port=port
        self.database=database
        self.username=username
        self.password=password
    
    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.server,
                port=self.port,
                database=self.database,
                user=self.username,
                password=self.password)
            return self.conn
        except:
            self.conn=None
            traceback.print_exc()
        return None

    def disConnect(self):
        if self.conn != None:
            self.conn.close()

    def queryDataset(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            if not df.empty:
                df.columns=cursor.column_names
            return df
        except:
            traceback.print_exc()
        return None
    
    def getTablesName(self):
        cursor = self.conn.cursor()
        cursor.execute("Show tables;")
        results=cursor.fetchall()
        tablesName=[]
        for item in results:
            tablesName.append([tableName for tableName in item][0])
        return tablesName
    
if __name__ == "__main__":
    try:
        connector = Connector()
        connector.server = "localhost"
        connector.port = 3306
        connector.database = "retails"
        connector.username = "root"
        connector.password = "nguyin"
        connector.connect()
        print("Connect database successful!")
    except:
        traceback.print_exc()

