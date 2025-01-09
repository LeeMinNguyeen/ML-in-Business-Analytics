'''
    Name: Le Minh Nguyenn
    Student ID: K224161829
'''

dataset = []
dataset.append({"id": 1, "name": "thuoc tam than", "price": 200})
dataset.append({"id": 2, "name": "thuoc giam can", "price": 100})
dataset.append({"id": 3, "name": "thuoc tang can", "price": 30})
dataset.append({"id": 4, "name": "thuoc chong mat", "price": 400})
dataset.append({"id": 5, "name": "thuoc tri co don", "price": 1000})
def print_data(data):
    '''
    Print out the dataset.
    '''
    for product in data:
        id = product["id"]
        name = product["name"]
        price = product["price"]
        info = f"ID: {id}\tName: {name}\tPrice: {price}"
        print(info)
        
print_data(dataset)

### Sort the dataset by price ascending ###

print("\nsorted dataset:")

def sort_data(data):
    '''
    Sort the dataset by price.
    '''
    for i in range(0, len(data)):
        for j in range(i+1, len(data)):
            if data[i]["price"] > data[j]["price"]:
                data[i], data[j] = data[j], data[i]
    return data
    # return sorted(data, key=lambda x: x["price"]) # Alternative solution

print_data(sort_data(dataset))


### Add a new product to the dataset ###

def add_product(data):
    '''
    Add a new product to the dataset.
    '''
    id = int(input("Enter the product ID: "))
    name = input("Enter the product name: ")
    price = float(input("Enter the product price: "))
    
    data.append({"id": id, "name": name, "price": price})
    
    return data

print("\nNew product added:")
dataset = add_product(dataset)

print_data(dataset)

### Modified the product dict ###

def modify(data):
    '''
    Modify the price of a product.
    '''
    id = int(input("Enter the product ID: "))
    
    new_id = int(input("Enter the new ID: "))
    name = input("Enter the new name: ")
    price = float(input("Enter the new price: "))
    
    for product in data:
        if product["id"] == id:
            product["id"] = new_id
            product["price"] = price
            product["name"] = name
            break
    
    return data

print("\nProduct modified:")
dataset = modify(dataset)
print_data(dataset)

### Delete a product ###

def delete_product(data):
    '''
    Delete a product from the dataset.
    '''
    id = int(input("Enter the product ID: "))
    
    for product in data:
        if product["id"] == id:
            data.remove(product)
            break
    
    return data