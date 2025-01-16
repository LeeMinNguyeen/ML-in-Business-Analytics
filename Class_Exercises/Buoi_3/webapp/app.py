from flask import Flask, request, render_template, session, redirect, app
import numpy as np
import pandas as pd

def find_and_sort_orders(df, minValue, maxValue, sortType):
    
    df['TotalPrice'] = df['UnitPrice'].astype(float) * df['Quantity'].astype(int) * (1 - df['Discount'].astype(float))
    
    filtered_df = df[(df['TotalPrice'] >= minValue) & (df['TotalPrice'] <= maxValue)]
    
    unique_orders = filtered_df[['OrderID', 'TotalPrice']].drop_duplicates()
    
    if sortType:
        unique_orders = unique_orders.sort_values(by='TotalPrice', ascending=True)
    else:
        unique_orders = unique_orders.sort_values(by='TotalPrice', ascending=False)
        
    unique_orders = unique_orders.reset_index(drop=True)

    return unique_orders

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def main():
    if "min_value" in request.form:
        min_value = float(request.form["min_value"])
        max_value = float(request.form["max_value"])
        SortType = bool(request.form["SortType"])
        df = pd.read_csv('Dataset\\SalesTransactions.csv')
        result = find_and_sort_orders(df, min_value, max_value, SortType)
        return render_template("orders_sort.html",  tables=[result.to_html(classes='data')], titles=result.columns.values)
    else:
        return render_template("orders_sort.html")
    
if __name__ == "__main__":
    app.run(host="localhost",port=5050, debug=True)
