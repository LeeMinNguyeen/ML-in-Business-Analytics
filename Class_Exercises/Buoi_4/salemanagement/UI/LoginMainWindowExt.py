from LoginMainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow
from MainProgramExt import MainProgramEx

import mysql.connector
import os, sys
for folder in os.listdir('./Class_Exercises/Buoi_4/salemanagement'):
    sys.path.append(os.path.abspath('./Class_Exercises/Buoi_4/salemanagement/'+folder))

from employee import NhanVien

class NhanVienConnector():
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
            print("Kết nối thành công")
        except Exception as e:
            print("Lỗi kết nối",e)
    
    def dang_nhap(self,username,password):
        cursor=self.conn.cursor()
        sql=f"select * from employee where username='{username}' and password='{password}'"
        cursor.execute(sql)
        dataset = cursor.fetchone()
        print(dataset)
        nv = None# giả sử không tìm thấy nhân viên đúng theo USERname +password
        
        if dataset != None:
            id, manhanvien, tennhanvien, username, password, isdeleted = dataset
            #vào được đây tức là có nhân viên
            nv=NhanVien(id,manhanvien,tennhanvien,username,password,isdeleted)
        
        cursor.close()
        
        return nv

class LoginMainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.nvconnector = NhanVienConnector()
    
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalandSlot()
    
    def setupSignalandSlot(self):
        self.pushButtonLogin.clicked.connect(self.login)
        
    def showWindow(self):
        self.MainWindow.show()
        
    def login(self):
        username=self.lineEditUsername.text()
        password=self.lineEditPassword.text()

        self.nvconnector.connects()
        
        print("Username:",username)
        print("Password:",password)
        
        self.nvlogin = self.nvconnector.dang_nhap(username, password)
        
        try:
            if self.nvlogin!=None:
                print("Đăng nhập thành công")
                self.MainWindow.hide()
                self.mainwindow = QMainWindow()
                self.myui = MainProgramEx()
                self.myui.setupUi(self.mainwindow)
                self.myui.showWindow()
            else:
                print("Đăng nhập thất bại")
                self.msg=QMessageBox()
                self.msg.setWindowTitle("Login thất bại")
                self.msg.setText("Bạn đăng nhập thất bại.\nKiểm tra lại thông tin đăng nhập")
                self.msg.setIcon(QMessageBox.Icon.Critical)
                self.msg.show()
        except Exception as e:
            print("Lỗi đăng nhập",e)
        
if __name__ == "__main__":
    # PyQt6 imports are already grouped at the top
    
    app = QApplication([])

    mainwindow = QMainWindow()
    myui = LoginMainWindowEx()
    myui.setupUi(mainwindow)
    myui.showWindow()
    app.exec()