from PyQt6.QtWidgets import QApplication, QMainWindow
import os, sys

for folder in os.listdir('./salemanagement'):
    sys.path.append(os.path.abspath('./salemanagement/'+folder))

from LoginMainWindowExt import LoginMainWindowEx
app = QApplication([])

mainwiindow = QMainWindow()
myui = LoginMainWindowEx()
myui.setupUi(mainwiindow)
myui.showWindow()
app.exec()