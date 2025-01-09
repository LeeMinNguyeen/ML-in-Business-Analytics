import sqlite3
import pandas as pd

sqliteConnection = sqlite3.connect('Dataset/databases/Chinook_Sqlite.sqlite')
cursor = sqliteConnection.cursor()

query = 'SELECT * FROM InvoiceLine'

cursor.execute(query)

df = pd.DataFrame(cursor.fetchall())

print(df)

cursor.close()