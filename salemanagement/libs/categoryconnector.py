from connectors import MySQLConnector
import os, sys
for folder in os.listdir('./salemanagement'):
    sys.path.append(os.path.abspath('./salemanagement/'+folder))

from category import category

class CategoryConnector(MySQLConnector):
    def __init__(self):
        super().__init__()
    
    def GetAll(self):
        sql = "select * from category"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        dataset = cursor.fetchall()
        
        categorylist = [[item[0], item[1], item[2]] for item in dataset]
        
        return categorylist


