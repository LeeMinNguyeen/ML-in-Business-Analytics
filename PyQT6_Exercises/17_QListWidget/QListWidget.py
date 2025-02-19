import sys
import os
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QInputDialog, QApplication, QWidget, QGridLayout, QListWidget, 
    QPushButton, QListWidgetItem, QMessageBox
)
from PyQt6.QtGui import QIcon

for folder in os.listdir('./PyQT6_Exercises/17_QListWidget'):
    sys.path.append(os.path.abspath('./PyQT6_Exercises/17_QListWidget' + folder))

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('QListWidget')
        self.setWindowIcon(QIcon('./images/ic_logo.png'))
        self.setGeometry(100, 100, 400, 100)

        layout = QGridLayout(self)
        self.setLayout(layout)

        self.list_widget = QListWidget(self)

        newItem = QListWidgetItem()
        newItem.setText("Metaverse")
        newItem.setIcon(QIcon('./images/ic_metaverse.png'))

        self.list_widget.addItem(newItem)
        self.list_widget.addItem("Smart Contract")
        self.list_widget.item(1).setIcon(QIcon('./images/ic_smartcontract.png'))
        self.list_widget.addItems(["Learn Python", "Machine Learning", "Deep Learning"])

        layout.addWidget(self.list_widget, 0, 0, 5, 1)

        add_button = QPushButton('Add New Item')
        add_button.clicked.connect(self.addItem)

        update_button = QPushButton('Update Item')
        update_button.clicked.connect(self.updateItem)

        insert_button = QPushButton('Insert New Item')
        insert_button.clicked.connect(self.insertItem)

        remove_button = QPushButton('Remove Selected Item')
        remove_button.clicked.connect(self.removeItem)

        clear_button = QPushButton('Clear All')
        clear_button.clicked.connect(self.clearAll)

        layout.addWidget(add_button, 0, 1)
        layout.addWidget(update_button, 1, 1)
        layout.addWidget(insert_button, 2, 1)
        layout.addWidget(remove_button, 3, 1)
        layout.addWidget(clear_button, 4, 1)

        self.list_widget.itemClicked.connect(self.processItemClicked)
        self.list_widget.itemDoubleClicked.connect(self.processItemDoubleClicked)
        self.list_widget.itemSelectionChanged.connect(self.processItemSelectionChanged)

        self.show()

class appfunctions(MainWindow):
    def __init__(self):
        super().__init__()

    def processItemSelectionChanged(self):
        current_row = self.list_widget.currentRow()
        item = self.list_widget.item(current_row)
        self.setWindowTitle(item.text())

    def processItemDoubleClicked(self):
        self.updateItem()

    def processItemClicked(self):
        current_row = self.list_widget.currentRow()
        data = self.list_widget.item(current_row)
        print("itemClicked=", data.text())

    def addItem(self):
        text, ok = QInputDialog.getText(self, 'Add a New Data', 'New Data:')
        if ok and text:
            self.list_widget.addItem(text)

    def updateItem(self):
        current_row = self.list_widget.currentRow()
        if current_row >= 0:
            item = self.list_widget.item(current_row)
            text, ok = QInputDialog.getText(self, 'Update Data', 'New Data:', text=item.text())
            if ok and text:
                item.setText(text)

    def insertItem(self):
        text, ok = QInputDialog.getText(self, 'Insert a New Data', 'New Data:')
        if ok and text:
            current_row = self.list_widget.currentRow()
            self.list_widget.insertItem(current_row + 1, text)

    def removeItem(self):
        current_row = self.list_widget.currentRow()
        if current_row >= 0:
            item = self.list_widget.item(current_row)
            msg = QMessageBox()
            msg.setText(f"Are you sure you want to remove {item.text()}?")
            msg.setWindowTitle("Removing Confirmation")
            msg.setIcon(QMessageBox.Icon.Question)
            buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            msg.setStandardButtons(buttons)
            result = msg.exec()
            if result == QMessageBox.StandardButton.Yes:
                current_item = self.list_widget.takeItem(current_row)
                del current_item

    def clearAll(self):
        answer = QMessageBox.question(
            self,
            'Confirmation',
            'Do you want to clear all Data?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.list_widget.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = appfunctions()
    sys.exit(app.exec())