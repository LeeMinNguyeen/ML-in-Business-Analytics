from connectMySQL import Connector
import pandas as pd

from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

class Kmeans_model:
    def __init__(self):
        conn = Connector()
        conn.server = "localhost"
        conn.port = 3306
        conn.database = "retails"
        conn.username = "root"
        conn.password = "nguyin"
        self.conn = conn.connect()
        
    def GetData(self):
        self.Customer = pd.read_sql("select * from customer", self.conn)
        self.OrderDetails = pd.read_sql("select o.*, p.*, c.CategoryID, s.*, od.* from orderdetails o join product p on o.ProductID = p.ProductID join category c on p.ProductSubcategoryID = c.CategoryID join subcategory s on c.CategoryID = s.CategoryID join orders od on od.OrderID = o.OrderID", self.conn)
        
        print(self.Customer.head())
        print(self.OrderDetails.head())
        
    def Kmeans(self):
        # Preprocess the data
        self.data = self.OrderDetails.groupby('CustomerID').agg({'OrderQty': 'sum', 'UnitPrice': 'mean'}).reset_index()
        self.data['TotalSpent'] = self.data['OrderQty'] * self.data['UnitPrice']
        
        # Standardize the data
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(self.data[['TotalSpent']])
        
        # Apply KMeans
        kmeans = KMeans(n_clusters=3, random_state=42)
        self.data['Cluster'] = kmeans.fit_predict(data_scaled)
        
        # Plot the clusters
        fig, ax = plt.subplots()
        scatter = ax.scatter(self.data['CustomerID'], self.data['TotalSpent'], c=self.data['Cluster'], cmap='viridis')
        ax.set_xlabel('CustomerID')
        ax.set_ylabel('TotalSpent')
        ax.set_title('Customer Clusters based on Purchasing Power')
        plt.colorbar(scatter, ax=ax)
        return fig
        
    def GetCustomerDetailsbyCluster(self, cluster):
        return self.data[self.data['Cluster'] == cluster]
    
class LinearRegress:
    def __init__(self):
        conn = Connector()
        conn.server = "localhost"
        conn.port = 3306
        conn.database = "retails"
        conn.username = "root"
        conn.password = "nguyin"
        self.conn = conn.connect()
    
    def GetData(self):
        self.OrderDetails = pd.read_sql("select o.*, p.*, c.CategoryID as CatID, s.*, od.* from orderdetails o join product p on o.ProductID = p.ProductID join category c on p.ProductSubcategoryID = c.CategoryID join subcategory s on c.CategoryID = s.CategoryID join orders od on od.OrderID = o.OrderID", self.conn)
        self.OrderDetails['OrderDate'] = pd.to_datetime(self.OrderDetails['OrderDate'], format='%d/%m/%Y')
            
    def LinearRegression_model(self, category_id=1):
        # Filter data for the specific category
        self.data = self.OrderDetails[self.OrderDetails['CatID'] == category_id]
        
        # Preprocess the data
        self.data = self.data.groupby(['OrderDate', 'CatID']).agg({'OrderQty': 'sum', 'UnitPrice': 'mean'}).reset_index()
        self.data['TotalSales'] = self.data['OrderQty'] * self.data['UnitPrice']
        
        # Convert OrderDate to datetime and extract features
        self.data['Year'] = self.data['OrderDate'].dt.year
        self.data['Month'] = self.data['OrderDate'].dt.month
        
        # Prepare the features and target variable
        X = self.data[['Year', 'Month', 'OrderQty', 'UnitPrice']]
        y = self.data['TotalSales']
        
        # Standardize the features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Fit the Linear Regression model
        model = LinearRegression()
        model.fit(X_scaled, y)
        
        # Predict the sales amount
        self.data['PredictedSales'] = model.predict(X_scaled)
        
        # Plot the actual vs predicted sales over time
        fig, ax = plt.subplots()
        ax.plot(self.data['OrderDate'], self.data['TotalSales'], label='Actual Sales', color='blue')
        ax.plot(self.data['OrderDate'], self.data['PredictedSales'], label='Predicted Sales', color='red')
        ax.set_xlabel('Order Date')
        ax.set_ylabel('Sales')
        ax.set_title(f'Actual vs Predicted Sales Over Time for Category {category_id}')
        plt.legend()
        return fig
    
    def returnTable(self):
        return self.data
        
if __name__ == "__main__":
    model = LinearRegress()
    model.GetData()
    model.LinearRegression_model()
    print(model.returnTable())
    # model.Kmeans()
    # print(model.GetCustomerDetailsbyCluster(0))