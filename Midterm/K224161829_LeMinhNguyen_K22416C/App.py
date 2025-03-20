import sys, os
sys.path.append(os.path.abspath('./Midterm/K224161829_LeMinhNguyen_K22416C/Backend'))
from UI import MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow



if __name__ == "__main__":

    qApp=QApplication([])
    qmainWindow=QMainWindow()
    window=MainWindow()
    window.setupUi(qmainWindow)
    window.showWindow()
    qApp.exec()