class product:
    def __init__(self, id, productid, productname, quantity, price, categoryid):
        self.id = id
        self.productid = productid
        self.productname = productname
        self.quantity = quantity
        self.price = price
        self.categoryid = categoryid
        
    def __str__(self):
        return f"{self.id}\t{self.productid}\t{self.productname}\t{self.quantity}\t{self.price}\t{self.categoryid}"