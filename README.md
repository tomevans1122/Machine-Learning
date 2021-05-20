# Machine-Learning

This repo contains my exploration and investigation of historical weather data using machine learning models. I purchased the hisotrical weather data for a set of coordinates every hour since 1/1/1980 until 1/1/2021. Naturally, the file is quite large at 109 MB.

## The data 
The original CSV file was nested. See below for a snippet of the data:
```
 ,dt,dt_iso,timezone,main,wind
0,315532800,1980-01-01 00:00:00 +0000 UTC,0,"{'temp': 0.72, 'temp_min': -1.42, 'temp_max': 2.16, 'feels_like': -3.27, 'pressure': 1013, 'humidity': 86}","{'speed': 2.6, 'deg': 180}".
```
It was tricky to retrieve the required data for usage, so I created a new CSV file with just the data I wanted (unix time and temperature) to ease the process. I did that via:  *creating_new_csv.py*

## The models

Temperature changes throughout the year intuitively follow a non-linear pattern. Nontheless I used both linear and non-linear machine learning models to see which models were more succesful. I used the sklearn library to employ these models: 

1. Linear Model
   - Linear Regression
2. Non linear models
   - Decision Tree Regression
   - Random Forrest Regression

I split the data into training and test sets and apply the models in: *MLmodels.py*

## Results
Running *MLmodels.py* shows clearly the superiority of running non-linear models compared to the linear model. Two indicators I have used to show model suitability are mean squared error and the coefficient of determination (r-squared). Running the script obtains:

Model                       |  MSE          | r-squared        |
| ------------------------- | ------------- | -------------    |
|    Linear regression      | 22.1746       |   0.0045         |
| Decision Tree regression  | 0.3940        |   0.9823         |
| Random Forrest regression | 0.3568        |   0.9840         |

When considering the best value for 0 and 1 for MSE and r-squared respectively, the results are clear. Both non-linear models yield similar results, however the Random Forrest Regression takes significantly longer to yeild results. After tinkering with the input variables (such as depth and number of estimations) I feel there is a theme of balancing accuracy of results with computational expense and time. 
However, there are many input variables to take into account with these models and I'm fully aware I have only scratched the surface of these models' capabilities. I will continue with analysis of the models as I investigate machine learning further.

