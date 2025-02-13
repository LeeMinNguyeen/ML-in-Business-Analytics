import os, sys
for folder in os.listdir('./salemanagement'):
    sys.path.append(os.path.abspath('./salemanagement/'+folder))

import traceback
from categoryconnector import CategoryConnector
from productconnector import ProductConnector

from PyQt6.QtCore import Qt
from ProductMainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow, QListWidgetItem, QTableWidgetItem

class ProductMainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.categoryconnector = CategoryConnector()
        self.categorylist = []
        self.productconnector = ProductConnector()
        self.productlist = []
    
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.query_category()
        self.show_category()
        self.MainWindow = MainWindow
        self.setupSignalandSlot()
    
    def setupSignalandSlot(self):
        self.listWidgetDanhMuc.itemSelectionChanged.connect(self.load_product_list)
    
    def load_product_list(self):
        selected_index = self.listWidgetDanhMuc.currentRow()
        if selected_index < 0:
            return
        item = self.listWidgetDanhMuc.item(selected_index)
        category = item.data(Qt.ItemDataRole.UserRole)
        
        self.productconnector.connects()
        self.productlist = self.productconnector.getproductbycategory(category.id)
        
        self.show_productlist()
        
    def show_productlist(self):
        self.tableWidgetSanPham.setRowCount(0)
        try:
            for product in self.productlist:
                row_index = self.tableWidgetSanPham.rowCount()
                self.tableWidgetSanPham.insertRow(row_index)
                column_id = QTableWidgetItem(str(product.id))
                column_productid = QTableWidgetItem(str(product.productid))
                column_productname = QTableWidgetItem(product.productname)
                column_quantity = QTableWidgetItem(str(product.quantity))
                column_price = QTableWidgetItem(str(product.price))
                column_categoryid = QTableWidgetItem(str(product.categoryid))
                self.tableWidgetSanPham.setItem(row_index, 0, column_id)
                self.tableWidgetSanPham.setItem(row_index, 1, column_productid)
                self.tableWidgetSanPham.setItem(row_index, 2, column_productname)
                self.tableWidgetSanPham.setItem(row_index, 3, column_quantity)
                self.tableWidgetSanPham.setItem(row_index, 4, column_price)
                self.tableWidgetSanPham.setItem(row_index, 5, column_categoryid)
        except:
            traceback.print_exc()
        
    def showWindow(self):
        self.MainWindow.show()
        
    def show_category(self):
        self.listWidgetDanhMuc.clear()
        for category in self.categorylist:
            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, category)
            item.setText(category.categoryname)
            self.listWidgetDanhMuc.addItem(item)
    
    def query_category(self):
        self.categoryconnector.connects()
        self.categorylist = self.categoryconnector.GetAll()
        
if __name__ == "__main__":
    # PyQt6 imports are already grouped at the top
    
    app = QApplication([])

    mainwindow = QMainWindow()
    myui = ProductMainWindowEx()
    myui.setupUi(mainwindow)
    myui.showWindow()
    app.exec()