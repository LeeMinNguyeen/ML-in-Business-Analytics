import pandas_read_xml as pdx
from bs4 import BeautifulSoup

#### BeautifulSoup ####

with open("Dataset\\SalesTransactions.xml", 'r') as f:
    data = f.read()
    
bs_data = BeautifulSoup(data, 'xml')
UelSample = bs_data.find_all('UelSample')
print(UelSample)


####    Pandas     ####

df = pdx.read_xml("Dataset\\SalesTransactions.xml", ['UelSample', 'SalesItem'])

data = df.iloc[0]
print(data)

