'''
    Name: Le Minh Nguyenn
    Student ID: K224161829
'''

class Product:
    '''
    A class to represent a product.

    Attributes
    ----------
    id : int
        the product ID
    name : str
        the product name
    price : float
        the product price

    Methods
    -------
    __str__()
        Return the product information.
    '''
    def __init__(self, id=None, name=None, price=None):
        '''
        Construct all the necessary attributes for the product object.

        Parameters
        ----------
            id : int
                the product ID
            name : str
                the product name
            price : float
                the product price
        '''
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        '''
        Return the product information.
        '''
        return f"ID: {self.id}\tName: {self.name}\tPrice: {self.price}"
    
    