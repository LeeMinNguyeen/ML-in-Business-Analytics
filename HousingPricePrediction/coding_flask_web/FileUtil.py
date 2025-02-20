class FileUtil():
    def __init__(self, modelname):
        self.modelname = modelname
    
    def loadmodel(self):
        model = f"./HousingPricePrediction/trainedmodel/{self.modelname}"
        return model