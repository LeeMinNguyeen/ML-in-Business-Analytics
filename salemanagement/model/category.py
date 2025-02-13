class category:
    def __init__(self, id=None, categoryid=None, categoryname=None):
        self.id = id
        self.categoryid = categoryid
        self.categoryname = categoryname
        
    def __str__(self):
        return f"{self.id}\t{self.categoryid}\t{self.categoryname}"
    