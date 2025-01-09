'''
    Name: Le Minh Nguyenn
    Student ID: K224161829
'''

from product import Product
from filefactory import FileFactory

ff = FileFactory()
path="E:\\Project\\ML-in-Business-Analytics\\Class_Exercises\\Buổi_1\\OOP"

dataset = ff.readData(f"{path}\\products.json", Product)

print("Dataset:")
for product in dataset:
    print(product)