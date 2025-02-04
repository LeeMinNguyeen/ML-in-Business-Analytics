from connectors import MySQLConnector
import os, sys
for folder in os.listdir('./Class_Exercises/Buoi_4/salemanagement'):
    sys.path.append(os.path.abspath('./Class_Exercises/Buoi_4/salemanagement/'+folder))

from employee import NhanVien

class NhanVienConnector(MySQLConnector):
    def __init__(self):
        super().__init__()
    
    def dang_nhap(self,username,password):
        cursor=self.conn.cursor()
        sql=f"select * from employee where username='{username}' and password='{password}'"
        cursor.execute(sql)
        dataset = cursor.fetchone()
        
        nv = None# giả sử không tìm thấy nhân viên đúng theo USERname +password
        
        if dataset != None:
            id, manhanvien, tennhanvien, username, password, isdeleted = dataset
            #vào được đây tức là có nhân viên
            nv=NhanVien(id,manhanvien,tennhanvien,username,password,isdeleted)
        
        cursor.close()
        
        return nv
    