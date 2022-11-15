# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Matthew McCabe
# Section: 538 102
# Assignment: lab 11b
# Date: 11/07/22
import matplotlib.pyplot as plt
import numpy as np
import csv

'''
Act I
'''
#
# m = np.array([1.00583, -0.087156, 0.087156, 1.00583]).reshape(2, 2)
# v = np.array([1, 0]).reshape(2, 1)
# v_list = np.array([])
#
# for i in range(250):
#     vp = np.dot(m, v)
#     v = vp
#     v_list = np.append(v_list, v)
#
# plt.plot(v_list, 'b')
# plt.title('Tornado')
# plt.ylabel('Y Axis')
# plt.xlabel('X Axis')
# plt.show()

'''
Act II
'''

# open csv as generic var.
with open('CLLWeatherData (1).csv', mode='r') as file:

    # reading csv data as dicts and creating lists for later purpose
    datafile = csv.DictReader(file)
    avg_temp = []
    avg_windspeed = []
    precip = []

    # for loop to loop through each line in weather data file
    for lines in datafile:
        # transforming weather data to approp. data type, and adding to list
        avg_temp.append(float(lines['Average Temperature (F)']))
        avg_windspeed.append(float(lines['Average Daily Wind Speed (mph)']))
        precip.append(float(lines['Precipitation (in)']))

# ####Plot 1#####

# plots of csv data with labels and legend
plt.plot(avg_temp, label='Temp avg')
plt.plot(avg_windspeed, label='Wind avg')
plt.title('Average Temperature and Wind Speed')
plt.ylabel('Average Temperature F')
plt.xlabel('date')
plt.legend(shadow='True', loc='lower left')
plt.show()

# ####Plot 2#####

# variable for data, title, limits on axes, and histogram method use
x = precip
plt.title('Histogram of Precipitation')
plt.ylabel('Number of Days')
plt.xlabel('Precipitation, in')
plt.ylim(0, 50)
plt.xlim(0, 5)
plt.hist(x)
plt.show()

# ####Plot 3#####

x = avg_windspeed
y = avg_temp
plt.title('Average Wind Speed vs Minimum Temperature')
plt.ylabel('Average Wind Speed, mph')
plt.xlabel('Minimum Temperature, F')
#plt.ylim(2.5, 20, 2.5)
#plt.xlim(20, 80, 10)
plt.scatter(x, y)
plt.show()

# ####Plot 4#####

x = np.linspace(2, 12, 1)
months = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

plt.plot(x, label='High T')
plt.title('Average Temperature by Month')
plt.ylabel('Average Temperature, F')
plt.xlabel('Month')
plt.legend(shadow='True')
#plt.ylim(0, 50)
plt.plot(x)
plt.bar(months, x)
plt.show()
