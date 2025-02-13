from ProductMainWindow import Ui_MainWindow

class ProductMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
    
    def showWindow(self):
        self.MainWindow.show()