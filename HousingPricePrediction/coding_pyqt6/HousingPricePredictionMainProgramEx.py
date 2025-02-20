import os
from HousingPricePredictionMainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow

class HousingPricePredictionEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    
    def setupSignalAndSlot(self):
        self.ModelsList()
        self.pushButtonPredict.clicked.connect(self.predictbuttonClicked)
        self.pushButtonClear.clicked.connect(self.clearbuttonClicked)
        self.pushButtonClose.clicked.connect(self.closebuttonClicked)
        self.comboBoxChooseModel.currentIndexChanged.connect(self.chooseModelChanged)
    
    def ModelsList(self):
        model_folder = "./HousingPricePrediction/trainedmodel/"
        models = [f for f in os.listdir(model_folder) if f.endswith('.zip')]
        self.comboBoxChooseModel.addItems(models)
        self.modelname = self.comboBoxChooseModel.currentText()
    
    def chooseModelChanged(self):
        self.modelname = self.comboBoxChooseModel.currentText()
    
    def predictbuttonClicked(self):
        AvgAreaIncome = float(self.lineEditAvgAreaIncome.text())
        AvgAreaHouseAge = float(self.lineEditAvgAreaHouseAge.text())
        AvgAreaNumberofRooms = float(self.lineEditAvgAreaNumberofRooms.text())
        AvgAreaNumberofBedrooms = float(self.lineEditAvgAreaNumberofBedrooms.text())
        AreaPopulation = float(self.lineEditAreaPopulation.text())
        
        import pickle
        modelname = f"./HousingPricePrediction/trainedmodel/{self.modelname}"
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