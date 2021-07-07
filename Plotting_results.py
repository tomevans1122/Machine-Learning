from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from MLmodels import weather_X, weather_y

#defining test size globally so can be used in tests
test_size = 0.2

train_X, test_X, train_y, test_y = train_test_split(weather_X, weather_y, test_size=test_size, random_state=4)


def actual_data_array():
    g = np.array(test_y)
    return g[:21]

def train_model(x):
    model = x
    abc = model.fit(train_X, train_y)
    return joblib.dump(abc, 'weather_predictor.pkl'), print(f"*** Training done! ***")

def prediction_data_array(model):
    model = joblib.load('weather_predictor.pkl')
    prediction = model.predict(test_X)
    y = pd.DataFrame({'actual': test_y,
                      'prediction': prediction})
    x = y.to_numpy()
    prediction_lst = []
    i = 0

    while i < 21:
        prediction_lst.append(x[i][1])
        i += 1
        continue
    # Make both lists into an array
    prediction_array = np.array(prediction_lst)

    return prediction_array

################################################

print(actual_data_array())

temps = actual_data_array()
print(f"Actual temps: {temps}")

train_model(LinearRegression())
b = prediction_data_array(LinearRegression())
print(f"LR Prediction: {b}")

train_model(DecisionTreeRegressor(random_state=0))
c = prediction_data_array(DecisionTreeRegressor(random_state=0))
print(f"DTR Prediction: {c}")


plt.grid(True)
plt.plot(temps, 'o', color='r', label='Actual temp')
plt.plot(b, 'r-', color='k', label='LR')
plt.plot(c, 'o', color='b', label='DTR')
plt.title('Comparison of different models at predicting temperature')
plt.xlabel('Collected temperature points')
plt.ylabel(f'Temperature (\u00B0C)')
plt.legend()
plt.show()