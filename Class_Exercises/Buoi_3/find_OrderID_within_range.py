import pandas as pd
import pandas_read_xml as pdx

def find_orders_within_range(df, minValue, maxValue, sort):
    
    df['TotalPrice'] = df['UnitPrice'].astype(float) * df['Quantity'].astype(int) * (1 - df['Discount'].astype(float))
    
    filtered_df = df[(df['TotalPrice'] >= minValue) & (df['TotalPrice'] <= maxValue)]
    
    unique_orders = filtered_df[['OrderID', 'TotalPrice']].drop_duplicates()
    
    if sort:
        unique_orders = unique_orders.sort_values(by='TotalPrice')
        
    unique_orders = unique_orders.reset_index(drop=True)

    return unique_orders

df = pdx.read_xml("Dataset\\SalesTransactions.xml", ['UelSample', 'SalesItem'])
df = pd.json_normalize(df.iloc[0])

print(df)

minValue = 0
maxValue = 20

result = find_orders_within_range(df, minValue, maxValue, True)

print('Danh sách các hóa đơn trong phạm vi giá trị từ', minValue, 'đến', maxValue, ' là:', result)
