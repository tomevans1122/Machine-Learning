# Machine-Learning

This repo contains my exploration and investigation of historical weather data using machine learning models.

## The data 
The original CSV file was nested. See below for a snippet of the nesting:
```
 ,dt,dt_iso,timezone,main,wind
0,315532800,1980-01-01 00:00:00 +0000 UTC,0,"{'temp': 0.72, 'temp_min': -1.42, 'temp_max': 2.16, 'feels_like': -3.27, 'pressure': 1013, 'humidity': 86}","{'speed': 2.6, 'deg': 180}".
```
It was tricky to retrieve the required data, so I created a new CSV file with just the data I wanted. I did that via:  *creating_new_csv.py*
This whittles down the data to two columns, unix time and the temperatures recorded at that time. Unfortunately the CSV file is far too large to upload to github as it has 359448 entries (every hour for 40 years).
