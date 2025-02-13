import os, sys
for folder in os.listdir('./salemanagement'):
    sys.path.append(os.path.abspath('./salemanagement/'+folder))
    
from matplotlib import category
from categoryconnector import CategoryConnector

categoryconnector = CategoryConnector()
categoryconnector.connects()
categorylist = categoryconnector.GetAll()
print(categorylist)