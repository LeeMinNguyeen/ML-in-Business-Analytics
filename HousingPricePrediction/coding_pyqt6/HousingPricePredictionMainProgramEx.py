from HousingPricePredictionMainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow

class HousingPricePredictionEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    
    def setupSignalAndSlot(self):
        self.pushButtonPredict.clicked.connect(self.predictbuttonClicked)
        self.pushButtonClear.clicked.connect(self.clearbuttonClicked)
        self.pushButtonClose.clicked.connect(self.closebuttonClicked)
    
    def predictbuttonClicked(self):
        AvgAreaIncome = float(self.lineEditAvgAreaIncome.text())
        AvgAreaHouseAge = float(self.lineEditAvgAreaHouseAge.text())
        AvgAreaNumberofRooms = float(self.lineEditAvgAreaNumberofRooms.text())
        AvgAreaNumberofBedrooms = float(self.lineEditAvgAreaNumberofBedrooms.text())
        AreaPopulation = float(self.lineEditAreaPopulation.text())
        
        import pickle
        modelname = "./HousingPricePrediction/trainedmodel/housingmodel.zip"
        trainedmodel = pickle.load(open(modelname, 'rb'))
        prediction = trainedmodel.predict([[AvgAreaIncome, AvgAreaHouseAge, AvgAreaNumberofRooms, AvgAreaNumberofBedrooms, AreaPopulation]])
        self.lineEditPredictedHousePrice.setText(str(prediction[0]))
        
    def clearbuttonClicked(self):
        self.lineEditAvgAreaIncome.clear()
        self.lineEditAvgAreaHouseAge.clear()
        self.lineEditAvgAreaNumberofRooms.clear()
        self.lineEditAvgAreaNumberofBedrooms.clear()
        self.lineEditAreaPopulation.clear()
        self.lineEditPredictedHousePrice.clear()
        
    def closebuttonClicked(self):
        self.MainWindow.close()
        
    def showWindow(self):
        self.MainWindow.show()
    
if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = HousingPricePredictionEx()
    ui.setupUi(MainWindow)
    ui.showWindow()
    app.exec()