import sys, os
sys.path.append(os.path.abspath('./Midterm/K224161829_LeMinhNguyen_K22416C/UI'))

from analytic import Analytic
from machinelearning import Kmeans_model, LinearRegress
from MainWindow import Ui_MainWindow

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow, QFileDialog

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MainWindow(Ui_MainWindow):
    def __init__(self):
        self.analytics = Analytic()
    
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignal()
        
    def setupSignal(self):
        self.pushButton_SalesByProduct.clicked.connect(self.SalesByProduct)
        self.pushButton_SalesByCategory.clicked.connect(self.SalesByCategory)
        self.pushButton_SalesByYearMonth.clicked.connect(self.SalesByYearMonth)
        self.pushButton_EarlyOrders.clicked.connect(self.EarlyOrder)
        self.pushButton_CustomerDetails.clicked.connect(self.GetCustomerDetails)
        self.pushButton_CustomerOrders.clicked.connect(self.GetCustomerOrders)
        
        self.pushButton_RunModel.clicked.connect(self.RunKMeans)
        self.pushButton_C1.clicked.connect(lambda: self.showCluster(0))
        self.pushButton_C2.clicked.connect(lambda: self.showCluster(1))
        self.pushButton_C3.clicked.connect(lambda: self.showCluster(2))
        
        self.pushButton.clicked.connect(self.Predict)
    
    def showResult(self, dataframe):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        if dataframe is None:
            return
        self.tableWidget.setColumnCount(len(dataframe.columns))
        self.tableWidget.setRowCount(len(dataframe.index))
        self.tableWidget.setHorizontalHeaderLabels(dataframe.columns)
        for i in range(len(dataframe.index)):
            for j in range(len(dataframe.columns)):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(dataframe.iat[i,j])))
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
    
    def SalesByProduct(self):
        self.showResult(self.analytics.calcTotalSalesByProduct())
        print("Sales by Product")
    
    def SalesByCategory(self):
        self.showResult(self.analytics.calcTotalSalesByCategory())
        print("Sales by Category")
    
    def SalesByYearMonth(self):
        self.showResult(self.analytics.calcTotalSalesByYearMonth())
        print("Sales by Year Month")
    
    def EarlyOrder(self):
        self.showResult(self.analytics.ListFastOrder())
        print("Early Orders")
    
    def GetCustomerDetails(self):
        self.CustomerID = self.lineEditCustomerID.text()
        self.showResult(self.analytics.GetCustomerDetailsbyID(self.CustomerID))
        print("Get Customer Details")
        
    def GetCustomerOrders(self):
        self.CustomerID = self.lineEditCustomerID.text()
        self.showResult(self.analytics.GetCustomerOrdersbyCustomerID(self.CustomerID))
        print("Get Customer Orders")
    
    def RunKMeans(self):
        self.model = Kmeans_model()
        self.model.GetData()
        fig = self.model.Kmeans()
        
        if not(self.verticalLayout_3.isEmpty()):
            self.verticalLayout_3.removeWidget(self.canvas)
        self.canvas = FigureCanvas(fig)
        self.verticalLayout_3.addWidget(self.canvas)
    
    def showCluster(self, cluster):
        
        dataframe = self.model.GetCustomerDetailsbyCluster(cluster)
    
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(0)
        if dataframe is None:
            return
        self.tableWidget_2.setColumnCount(len(dataframe.columns))
        self.tableWidget_2.setRowCount(len(dataframe.index))
        self.tableWidget_2.setHorizontalHeaderLabels(dataframe.columns)
        for i in range(len(dataframe.index)):
            for j in range(len(dataframe.columns)):
                self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(dataframe.iat[i,j])))
        self.tableWidget_2.resizeColumnsToContents()
        self.tableWidget_2.resizeRowsToContents()
        
    def Predict(self):
        self.predict_model = LinearRegress()
        self.predict_model.GetData()
        fig = self.predict_model.LinearRegression_model(category_id=int(self.comboBox.currentText()))
        
        if not(self.verticalLayout_4.isEmpty()):
            self.verticalLayout_4.removeWidget(self.canvas)
        self.canvas = FigureCanvas(fig)
        self.verticalLayout_4.addWidget(self.canvas)

        self.PredictTable()
    
    def PredictTable(self):
        dataframe = self.predict_model.returnTable()
        
        if dataframe is None:
            return
        self.tableWidget_3.setColumnCount(len(dataframe.columns))
        self.tableWidget_3.setRowCount(len(dataframe.index))
        self.tableWidget_3.setHorizontalHeaderLabels(dataframe.columns)
        for i in range(len(dataframe.index)):
            for j in range(len(dataframe.columns)):
                self.tableWidget_3.setItem(i, j, QTableWidgetItem(str(dataframe.iat[i,j])))
        self.tableWidget_3.resizeColumnsToContents()
        self.tableWidget_3.resizeRowsToContents()
        
    
    def showWindow(self):
        self.MainWindow.show()
        
if __name__ == "__main__":

    qApp=QApplication([])
    qmainWindow=QMainWindow()
    window=MainWindow()
    window.setupUi(qmainWindow)
    window.showWindow()
    qApp.exec()