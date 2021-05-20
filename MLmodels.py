from pandas import read_csv
import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor

# Prepare data into training and testing sets
raw_data = 'temps.csv'
data = read_csv(raw_data)

weather_y = data.pop('temp')        # validation data set
weather_X = data                    # training data set

train_X, test_X, train_y, test_y = train_test_split(weather_X, weather_y, test_size=0.2, random_state=4)

# Training the different models
def train_model(x):
    model = x
    model.fit(train_X, train_y)

    joblib.dump(model, 'weather_predictor.pkl')
    return print(f"*** Training done! ***")

# Predicting temperatures
def predict_temp(model):
    model = joblib.load('weather_predictor.pkl')
    prediction = model.predict(test_X)
    y = pd.DataFrame({'actual': test_y,
                      'prediction': prediction})
    return print(y[:5]), print(f" Mean Squared Error: {mean_squared_error(test_y, prediction)}"), \
           print(f" r\u00b2 score: {r2_score(test_y, prediction)}")


if __name__ == "__main__":
    train_model(LinearRegression())
    predict_temp(LinearRegression())
    print("*" * 20)
    train_model(DecisionTreeRegressor(random_state=0))
    predict_temp(DecisionTreeRegressor(random_state=0))
    print("*" * 20)
    train_model(RandomForestRegressor(max_depth=50, random_state=0, n_estimators=100))
    predict_temp(RandomForestRegressor(max_depth=50, random_state=0, n_estimators=100))
