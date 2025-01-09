'''
    Name: Le Minh Nguyenn
    Student ID: K224161829

    Lọc sp có giá từ a - b (trong khoảng giá)
    Xóa tất cả sp có giá nhỏ hơn x
'''

from product import Product
from filefactory import FileFactory

# Filter product by price
def FilterByPriceRange(dataset):
    min, max = PriceRange()
    filteredProducts = []
    for product in dataset:
        if product.price >= min and product.price <= max:
            filteredProducts.append(product)
    return filteredProducts

def PriceRange():
    min = float(input("Enter min price: "))
    max = float(input("Enter max price: "))
    return min, max

# Delete product smaller than specified price
def DeleteProductByPrice(dataset):
    price = float(input("Enter price: "))
    
    dataset_copy = dataset[:] # Copy dataset to avoid changing the original dataset
    # Không có [:] thì dataset_copy sẽ tham chiếu đến dataset
    
    # Nếu xóa trực tiếp dataset thì vòng lặp sẽ bị skip product tiếp theo do bị đôn lên
    for product in dataset_copy:
        if product.price < price:
            dataset.remove(product)
    
    return dataset

if __name__ == "__main__":
    
    # Read file
    ff = FileFactory()
    path="E:\\Project\\ML-in-Business-Analytics\\Class_Exercises\\Buổi_1\\OOP"

    dataset = ff.readData(f"{path}\\products.json", Product)

    print("Dataset:")
    for product in dataset:
        print(product)

    print("\n--------------\n")
    
    filteredProducts = FilterByPriceRange(dataset)
    print("Filtered Products:")
    for product in filteredProducts:
        print(product)

    print("\n--------------\n")
    
    deletedProducts = DeleteProductByPrice(dataset)
    print("Dataset after delete products:")
    for product in deletedProducts:
        print(product)
