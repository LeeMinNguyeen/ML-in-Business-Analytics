from calendar import c
import os, sys
for folder in os.listdir('./salemanagement'):
    sys.path.append(os.path.abspath('./salemanagement/'+folder))

from product import product
from connectors import MySQLConnector

class ProductConnector(MySQLConnector):
    def getproductbycategory(self, categoryid):
        sql = f"select * from product where categoryid={categoryid}"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        dataset = cursor.fetchall()
        
        productlist = []
        for c in dataset:
            productlist.append(product(c[0],c[1],c[2],c[3],c[4],c[5]))
        
        cursor.close()
        return productlist
    
if __name__ == "__main__":
    categoryconnector = ProductConnector()
    categoryconnector.connects()
    productlist = categoryconnector.getproductbycategory(1)
    for product in productlist:
        print(product)