import os, sys
for folder in os.listdir('./56_MLBAProject'):
    sys.path.append(os.path.abspath('./56_MLBAProject/'+folder))

import mysql.connector

import traceback

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox

#from Connectors import Connector
from DatabaseConnect import Ui_MainWindow


import pandas as pd

class Connector:
    def __init__(self, server=None, port=None, database=None, username=None, password=None):
        self.server = server
        self.port = port
        self.database = database
        self.username = username
        self.password = password
    
    def connect(self):
        try:
            self.conn = mysql.connector.connect(host = self.server,
                                                port = self.port,
                                                database = self.database,
                                                user = self.username,
                                                password = self.password)
        except:
            self.conn = None
            traceback.print_exc()
        return self.conn

    def disConnect(self):
        if self.conn != None:
            self.conn.close()

    def queryDataset(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            if not df.empty:
                df.columns = cursor.column_names
            return df
        except:
            traceback.print_exc()
        return None
    
    def getTablesName(self):
        cursor = self.conn.cursor()
        cursor.execute("Show tables;")
        results=cursor.fetchall()
        tablesName=[]
        for item in results:
            tablesName.append([tableName for tableName in item][0])
        return tablesName

class DatabaseConnectEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonConnect.clicked.connect(self.connectDatabase)
    
    def connectDatabase(self):
        try:
            server = self.lineEditServer.text()
            port = int(self.lineEditPort.text())
            database = self.lineEditDatabase.text()
            username = self.lineEditUser.text()
            password = self.lineEditPassword.text()
            self.connector = Connector(server=server, port=port, database=database, username=username, password=password)
            self.connector.connect()
            self.msg = QMessageBox()
            self.msg.setText("Connect database successful!")
            self.msg.setWindowTitle("Info")
            self.msg.show()
            self.MainWindow.close()
            if self.parent != None:
                self.parent.checkEnableWidget(True)
        except:
            traceback.print_exc()
            self.msg = QMessageBox()
            self.msg.setText("Connect database failed")
            self.msg.setWindowTitle("Info")
            self.msg.show()
    
    def show(self):
        self.MainWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.MainWindow.show()
        
if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication, QMainWindow
    
    qApp=QApplication([])
    qmainWindow=QMainWindow()
    window=DatabaseConnectEx()
    window.setupUi(qmainWindow)
    window.show()
    qApp.exec()