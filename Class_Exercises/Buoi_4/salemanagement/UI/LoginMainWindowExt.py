from LoginMainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow
from MainProgramExt import MainProgramEx

class LoginMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalandSlot()
        
    def setupSignalandSlot(self):
        self.pushButtonLogin.clicked.connect(self.login)
        
    def showWindow(self):
        self.MainWindow.show()
        
    def login(self):
        username = self.lineEditUsername.text()
        password = self.lineEditPassword.text()
        
        if username == 'admin' and password == 'admin':
            self.MainWindow.hide()
            self.mainProgramWindow = QMainWindow()
            self.mainProgram = MainProgramEx()
            self.mainProgram.setupUi(self.mainProgramWindow)
            self.mainProgram.showWindow()
        else:
            self.msg = QMessageBox()
            self.msg.setWindowTitle('Login failed')
            self.msg.setText('Login failed')
            self.msg.show()
        
if __name__ == "__main__":
    # PyQt6 imports are already grouped at the top
    
    app = QApplication([])

    mainwindow = QMainWindow()
    myui = LoginMainWindowEx()
    myui.setupUi(mainwindow)
    myui.showWindow()
    app.exec()