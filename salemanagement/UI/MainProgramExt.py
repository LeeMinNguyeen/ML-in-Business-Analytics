from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow
import sys
from MainProgram import Ui_MainWindow
from ProductMainWindowExt import ProductMainWindowEx

class MainProgramEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalandSlot()
    
    def setupSignalandSlot(self):
        self.actionExit.triggered.connect(self.exitProgram)
        self.actionCategoryManagement.triggered.connect(self.showCategoryManagement)
    
    def showCategoryManagement(self):
        self.productmainwindow = QMainWindow()
        self.productui = ProductMainWindowEx()
        self.productui.setupUi(self.productmainwindow)
        self.productui.showWindow()
    
    def exitProgram(self):
        sys.exit(0)
    
    def showWindow(self):
        self.MainWindow.show()
        
if __name__ == "__main__":
    # PyQt6 imports are already grouped at the top
    
    app = QApplication([])

    mainwindow = QMainWindow()
    myui = MainProgramEx()
    myui.setupUi(mainwindow)
    myui.showWindow()
    app.exec()