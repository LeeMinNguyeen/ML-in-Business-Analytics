import os, sys
for folder in os.listdir('./salemanagement'):
    sys.path.append(os.path.abspath('./salemanagement/'+folder))

import mysql.connector

class MySQLConnector:
    def __init__(self,server=None,port=None,database=None,
                 username=None,password=None):
        if server == None:
            self.server = "localhost"
            self.port = 3306
            self.database = "k22416c_sales"
            self.username = "root"
            self.password = "nguyin"
        else:
            self.server = server
            self.port = port
            self.database = database
            self.username = username
            self.password = password
            
    def connects(self):
        try:
            self.conn = mysql.connector.connect(host=self.server,
                                                port=self.port,
                                                database=self.database,
                                                user=self.username,
                                                password=self.password)
        except Exception as e:
            print("Lỗi kết nối",e)
            