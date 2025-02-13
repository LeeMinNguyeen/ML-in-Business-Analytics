from calendar import c
import os, sys
for folder in os.listdir('./salemanagement'):
    sys.path.append(os.path.abspath('./salemanagement/'+folder))

from category import category
from connectors import MySQLConnector

class CategoryConnector(MySQLConnector):
    def __init__(self):
        super().__init__()
    
    def GetAll(self):
        sql = "select * from category"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        dataset = cursor.fetchall()
        
        categorylist = []
        for c in dataset:
            categorylist.append(category(c[0],c[1],c[2]))
        
        cursor.close()
        return categorylist

    def __str__(self):
        return f"{self.id}\t{self.categoryid}\t{self.categoryname}"

if __name__ == "__main__":
    categoryconnector = CategoryConnector()
    categoryconnector.connects()
    categorylist = categoryconnector.GetAll()
    for category in categorylist:
        print(category)