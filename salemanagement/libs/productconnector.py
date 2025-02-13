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
    
    def product_detail(self, id):
        cursor=self.conn.cursor()
        sql=f"select * from product where id={id}"
        cursor.execute(sql)
        dataset = cursor.fetchone()
        
        p = None
        
        if dataset != None:
            id, productid, productname, quantity, price, categoryid = dataset
            p = product(id, productid, productname, quantity, price, categoryid)
        
        cursor.close()
        
        return p
    
    def delete_product(self, id):
        cursor=self.conn.cursor()
        sql=f"delete from product where id={id}"
        cursor.execute(sql)
        self.conn.commit()
        result = cursor.rowcount
        cursor.close()
        return result
    
    def add_product(self, product):
        cursor=self.conn.cursor()
        sql=f"insert into product(id, productid, productname, amount, price, categoryid) values('{product.id}', '{product.productid}', '{product.productname}', {product.quantity}, {product.price}, {product.categoryid})"
        cursor.execute(sql)
        self.conn.commit()
        result = cursor.rowcount
        cursor.close()
        return result
    
    def change_detail(self, product):
        cursor=self.conn.cursor()
        sql=f"update product set productid='{product.productid}', productname='{product.productname}', amount={product.quantity}, price={product.price}, categoryid={product.categoryid} where id={product.id}"
        cursor.execute(sql)
        self.conn.commit()
        result = cursor.rowcount
        cursor.close()
        return result
    
if __name__ == "__main__":
    categoryconnector = ProductConnector()
    categoryconnector.connects()
    productlist = categoryconnector.getproductbycategory(1)
    for product in productlist:
        print(product)