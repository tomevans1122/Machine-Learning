# Script is not operational - only needed to work once to create the desired csv file

import csv
from pandas import read_csv
import numpy as np
import ast


raw_data = 'weather_raw.csv'
data = read_csv(raw_data)


# for temperature
i = 0
all_temps = []
while i < 359448:
    main_dict = ast.literal_eval(data.main[i])
    temp_float = main_dict['temp']
    all_temps.append(temp_float)
    i += 1
    continue

temps_array = np.array(all_temps)
print(f" temps array len: {len(temps_array)}")


# for datetime
i = 0
all_dates = []
while i < 359448:
    dt_int64 = data.dt[i]
    all_dates.append(dt_int64)
    i += 1
    continue

dates_array = np.array(all_dates)
print(f" dates array len: {len(dates_array)}")


with open('temps.csv', 'w', newline='') as file:
    fieldnames = ['unixtime', 'temp']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    i = 0
    while i < 359448:
        writer.writerow({'unixtime': dates_array[i], 'temp': temps_array[i]})
        i += 1
        continue



