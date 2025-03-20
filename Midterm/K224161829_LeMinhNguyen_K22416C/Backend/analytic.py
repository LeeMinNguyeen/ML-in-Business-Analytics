from connectMySQL import Connector
import pandas as pd

class Analytic:
    def __init__(self):
        conn = Connector()
        conn.server = "localhost"
        conn.port = 3306
        conn.database = "retails"
        conn.username = "root"
        conn.password = "nguyin"
        self.conn = conn.connect()
    
    def calcTotalSalesByProduct(self):
        sql = """
            select p.Name, sum(o.OrderQty*o.UnitPrice) as total_sales
            from orderdetails o
            join product p
            on o.ProductID = p.ProductID
            group by p.Name;
            """
        df = pd.read_sql(sql, self.conn)
        return df
    
    def calcTotalSalesByCategory(self):
        sql = """
            select c.Name, sum(o.OrderQty*o.UnitPrice) as total_sales
            from orderdetails o
            join product p
            on o.ProductID = p.ProductID
            join category c
            on p.ProductSubcategoryID = c.CategoryID
            join subcategory s
            on c.CategoryID = s.CategoryID
            group by c.Name;
        """
        df = pd.read_sql(sql, self.conn)
        return df
    
    def calcTotalSalesByYearMonth(self):
        sql = """
            select o.OrderDate, od.OrderQty, od.UnitPrice
            from orders o
            join orderdetails od
            on o.OrderID = od.OrderID
        """
        df = pd.read_sql(sql, self.conn)
        
        df['OrderDate'] = pd.to_datetime(df['OrderDate'], format='%d/%m/%Y')
        df['year'] = df['OrderDate'].dt.year
        df['month'] = df['OrderDate'].dt.month
        df['total_sales'] = df['OrderQty']*df['UnitPrice']
        
        result = df.groupby(['year', 'month'])['total_sales'].sum().reset_index()
        return result
    
    def ListFastOrder(self):
        sql = """
            select OrderID, OrderDate, DueDate, ShipDate
            from orders
        """
        df = pd.read_sql(sql, self.conn)
        
        df['OrderDate'] = pd.to_datetime(df['OrderDate'], format='%d/%m/%Y')
        df['DueDate'] = pd.to_datetime(df['DueDate'], format='%d/%m/%Y')
        df['ShipDate'] = pd.to_datetime(df['ShipDate'], format='%d/%m/%Y')

        df = df[df['ShipDate'] < (df['DueDate'] - pd.Timedelta(days=3))]
        
        return df
    
    def GetCustomerDetailsbyID(self, CustomerID):
        sql = f"""
            select *
            from customer
            where CustomerID = '{CustomerID}' 
        """
        df = pd.read_sql(sql, self.conn)
        return df
    
    def GetCustomerOrdersbyCustomerID(self, CustomerID):
        sql = f"""
            select o.OrderID, o.OrderDate, o.DueDate, o.ShipDate, o.EmployeeID
            from orders o
            join customer c
            on o.CustomerID = c.CustomerID
            where c.CustomerID = '{CustomerID}'
        """
        df = pd.read_sql(sql, self.conn)
        return df
    
if __name__ == "__main__":
    analytic = Analytic()
    print(analytic.calcTotalSalesByYearMonth())
    print(analytic.ListFastOrder())
    print(analytic.GetCustomerDetailsbyID('11958'))
    print(analytic.GetCustomerOrdersbyCustomerID('11958'))