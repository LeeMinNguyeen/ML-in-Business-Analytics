'''
    Name: Le Minh Nguyenn
    Student ID: K224161829
'''

from product import Product
from filefactory import FileFactory

p1=Product(1, "Coca", 6000)

dataset = []
dataset.append(p1)
dataset.append(Product(2, "Pepsi", 6000))
dataset.append(Product(3, "Fanta", 7000))
dataset.append(Product(4, "Redbull", 9000))
dataset.append(Product(5, "Monster", 12000))

print("Dataset:")
for product in dataset:
    print(product)
    
### Input data ###
while True:
    id = int(input("Enter product ID: "))
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    
    dataset.append(Product(id, name, price))
    
    choice = input("Do you want to continue? (Y/N)")
    if choice.lower() == "n":
        break
    
print("Updated Dataset:")
for product in dataset:
    print(product)

### Write to json file ###
path = "E:\\Project\\ML-in-Business-Analytics\\Class_Exercises\\Buổi_1\\OOP" # File path
ff = FileFactory()
ff.writeData(f"{path}\\products.json", dataset)
print("Write to json file successfully!")

