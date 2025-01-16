from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow
from MainProgram import Ui_MainWindow

class MainProgramEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalandSlot()
    
    def setupSignalandSlot(self):
        pass
        
    def showWindow(self):
        self.MainWindow.show()