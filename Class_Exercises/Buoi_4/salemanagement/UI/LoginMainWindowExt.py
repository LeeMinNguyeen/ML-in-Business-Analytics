from LoginMainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow
from MainProgramExt import MainProgramEx

import os, sys
for folder in os.listdir('./Class_Exercises/Buoi_4/salemanagement'):
    sys.path.append(os.path.abspath('./Class_Exercises/Buoi_4/salemanagement/'+folder))

from employeeconnector import NhanVienConnector

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