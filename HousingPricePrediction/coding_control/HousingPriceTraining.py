import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pickle

df = pd.read_csv('./HousingPricePrediction/dataset/USA_Housing.csv')

x = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms','Avg. Area Number of Bedrooms', 'Area Population']]
y = df['Price']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=101)

lm = LinearRegression()
lm.fit(x_train,y_train)

predictions = lm.predict(x_test)

pre1=lm.predict([x_test.iloc[0]])
print("kết quả =",pre1)

pre2=lm.predict([[66774.995817,5.717143,7.795215,4.320000,36788.980327]])
print("kết quả 2 =",pre2)

# print the intercept
print(lm.intercept_)
coeff_df = pd.DataFrame(lm.coef_,x.columns,columns=['Coefficient'])
print(coeff_df)

print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

modelname="./HousingPricePrediction/trainedmodel/housingmodel.zip"
pickle.dump(lm, open(modelname, 'wb'))

