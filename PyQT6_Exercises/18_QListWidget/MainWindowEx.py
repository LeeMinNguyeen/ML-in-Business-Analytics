import os, sys
import json
import os.path

for folder in os.listdir('.\\PyQT6_Exercises\\18_QListWidget'):
    sys.path.append(os.path.abspath('.\\PyQT6_Exercises\\18_QListWidget'+folder))

from PyQt6.QtCore import Qt
from MainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMessageBox, QListWidgetItem
from PyQt6.QtGui import QIcon

from employee import Employee

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.dataset = []
        
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonNew.clicked.connect(self.add_new_item)
        self.pushButtonDelete.clicked.connect(self.delete_item)
        self.pushButtonClose.clicked.connect(self.close)
        self.listWidgetEmployee.itemSelectionChanged.connect(self.show_selected_item)
        self.pushButtonSave.clicked.connect(self.save_employee)
        self.readEmployeeFromJson()
        
    def show(self):
        self.MainWindow.show()
        
    def add_new_item(self):
        self.EmployeeName.setText("")
        self.EmployeeEmail.setText("")
        self.EmployeeName.setFocus()
        
    def writeEmployeeToJson(self):
        dataset = []
        for i in range(0, self.listWidgetEmployee.count()):
            item = self.listWidgetEmployee.item(i)
            emp = item.data(Qt.ItemDataRole.UserRole)
            dataset.append(emp)
        jsonString = json.dumps([emp.__dict__ for emp in dataset])
        jsonFile = open("database.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        
    def readEmployeeFromJson(self):
        if os.path.isfile(".\\PyQT6_Exercises\\18_QListWidget\\database.json") == False:
            return
        file = open('.\\PyQT6_Exercises\\18_QListWidget\\database.json', "r")
        # Reading from file
        self.dataset = json.loads(file.read(), object_hook=lambda d: Employee(**d))
        file.close()
        for emp in self.dataset:
            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, emp)
            item.setText(str(emp))
            item.setCheckState(Qt.CheckState.Unchecked)
            item.setIcon(QIcon("images/ic_user.png"))
            self.listWidgetEmployee.addItem(item)
    
    def save_employee(self):
        insertEmployee = Employee(self.EmployeeName.text(),self.EmployeeEmail.text(),self.Woman.isChecked())
        isDuplicated=False
        for i in range(0,self.listWidgetEmployee.count()):
            item = self.listWidgetEmployee.item(i)
            data = item.data(Qt.ItemDataRole.UserRole)
            if insertEmployee.email.lower() == data.email.lower():
                isDuplicated = True
                break
        if not isDuplicated:
            item = QListWidgetItem()
        item.setData(Qt.ItemDataRole.UserRole,insertEmployee)
        item.setText(str(insertEmployee))
        item.setCheckState(Qt.CheckState.Unchecked)
        item.setIcon(QIcon("images/ic_user.png"))
        if not isDuplicated:
            self.listWidgetEmployee.addItem(item)
        self.writeEmployeeToJson()
    
    def delete_item(self):
        answer = QMessageBox.question(
            self.MainWindow,
            'Confirmation',
            'Do you want to remove checked Items?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.No:
            return
        for index in range(self.listWidgetEmployee.count()-1,-1,-1):
            item=self.listWidgetEmployee.item(index)
            if item.checkState()==Qt.CheckState.Checked:
                current_item = self.listWidgetEmployee.takeItem(index)
                del current_item
        self.processNew()
        self.writeEmployeeToJson()
        
    def close(self):
        msg = QMessageBox()
        msg.setText(f"Are you sure you want to exit ?")
        msg.setWindowTitle("Exit Confirmation")
        msg.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msg.setStandardButtons(buttons)
        result = msg.exec()
        if result == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
            
    def show_selected_item(self):
        current_row = self.listWidgetEmployee.currentRow()
        if current_row < 0:
            return
        item = self.listWidgetEmployee.item(current_row)
        emp = item.data(Qt.ItemDataRole.UserRole)
        self.EmployeeName.setText(emp.name)
        self.EmployeeEmail.setText(emp.email)
        if emp.gender==True:
            self.Woman.setChecked(True)
        else:
            self.Man.setChecked(True)
    
