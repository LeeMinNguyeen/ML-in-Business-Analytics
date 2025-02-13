import os, sys

for folder in os.listdir('./salemanagement'):
    sys.path.append(os.path.abspath('./salemanagement/'+folder))

import traceback
from categoryconnector import CategoryConnector
from productconnector import ProductConnector
from product import product

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
        self.tableWidgetSanPham.itemSelectionChanged.connect(self.show_product_detail)
        self.pushButtonXoa.clicked.connect(self.delete_product)
        self.pushButtonThemMoi.clicked.connect(self.add_product)
        self.pushButtonLuu.clicked.connect(self.update_product)
    
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
                if product.quantity <= 20:
                    column_quantity.setBackground(Qt.GlobalColor.yellow)
                    column_quantity.setForeground(Qt.GlobalColor.red)
        except:
            traceback.print_exc()
    
    def show_product_detail(self):
        selected_index = self.tableWidgetSanPham.currentRow()
        if selected_index == -1:
            return
        id = self.tableWidgetSanPham.item(selected_index, 0).text()
        self.productconnector.connects()
        product = self.productconnector.product_detail(id)
        if product == None:
            return
        self.lineEditId.setText(str(product.id))
        self.lineEditMa.setText(product.productid)
        self.lineEditTen.setText(str(product.productname))
        self.lineEditSoLuong.setText(str(product.quantity))
        self.lineEditDonGia.setText(str(product.price))
        self.lineEditIdDM.setText(str(product.categoryid))
    
    def showWindow(self):
        self.MainWindow.show()
        
    def show_category(self):
        self.listWidgetDanhMuc.clear()
        for category in self.categorylist:
            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, category)
            item.setText(category.categoryname)
            self.listWidgetDanhMuc.addItem(item)
            
    def delete_product(self):
        msg = self.lineEditId.text()+"-"+self.lineEditTen.text()
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Xác nhận xóa")
        dlg.setText(f"Bạn có chắc chắn muốn xóa {msg}")
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        ret = dlg.exec()
        if ret == QMessageBox.StandardButton.No:
            return
        
        id = self.lineEditId.text()
        self.productconnector.connects()
        result = self.productconnector.delete_product(id)
        if result > 0:
            QMessageBox.information(self.MainWindow, "Thông báo", "Xóa thành công")
            self.load_product_list()
        else:
            QMessageBox.information(self.MainWindow, "Thông báo", "Xóa không thành công")
            
    def add_product(self):
        id = self.lineEditId.text()
        productid = self.lineEditMa.text()
        productname = self.lineEditTen.text()
        quantity = self.lineEditSoLuong.text()
        price = self.lineEditDonGia.text()
        categoryid = self.lineEditIdDM.text()
        p = product(id, productid, productname, quantity, price, categoryid)
        self.productconnector.connects()
        result = self.productconnector.add_product(p)
        if result > 0:
            QMessageBox.information(self.MainWindow, "Thông báo", "Thêm mới thành công")
            self.load_product_list()
        else:
            QMessageBox.information(self.MainWindow, "Thông báo", "Thêm mới không thành công")
        
    def update_product(self):
        msg = self.lineEditId.text()+"-"+self.lineEditTen.text()
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Xác nhận thay đổi")
        dlg.setText(f"Bạn có chắc chắn muốn thay đổi {msg}")
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        ret = dlg.exec()
        if ret == QMessageBox.StandardButton.No:
            return
        
        id = self.lineEditId.text()
        productid = self.lineEditMa.text()
        productname = self.lineEditTen.text()
        quantity = self.lineEditSoLuong.text()
        price = self.lineEditDonGia.text()
        categoryid = self.lineEditIdDM.text()
        p = product(id, productid, productname, quantity, price, categoryid)
        self.productconnector.connects()
        result = self.productconnector.change_detail(p)
        if result > 0:
            QMessageBox.information(self.MainWindow, "Thông báo", "Cập nhật thành công")
            self.load_product_list()
        else:
            QMessageBox.information(self.MainWindow, "Thông báo", "Cập nhật không thành công")
    
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