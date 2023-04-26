from flask import Flask, request
import requests
#import redis
import json
#import os
#from matplotlib import pyplot as plt
#import numpy as np

app = Flask(__name__)

url = "https://raw.githubusercontent.com/michaelx/climate/master/climate.json"
data = requests.get(url)
climate_data = data.json()


@app.route('/data', methods=['GET'])
def handle_data():
    return climate_data
    
@app.route('/delete-data', methods=['DELETE'])
def delete_data():
    global climate_data
    climate_data = []
    return climate_data

@app.route('/post-data', methods=['POST'])
def post_data():
    global climate_data
    climate_data = data.json()
    return "the data has been posted"

@app.route('/countries', methods=['GET'])
def get_countries():
    '''
        This function gets a lsit of all the countries in the dataset
        Returns:
        countries (list): a list of countries in the climate dataset
    '''
    country_list = []
    max_list = len(climate_data)
    for x in range(max_list):
        country_list.append(climate_data[x]['country'])
    countries = []
    for item in country_list:
        if item not in countries:
            countries.append(item)
    return countries

@app.route('/locations', methods=['GET'])
def get_cities():
    '''
        This function gets a list of all the cities in the climate dataset
        Returns:
        city_list (list): a list of cities in the dataset
    '''
    city_list = []
    max_list = len(climate_data)
    for x in range(max_list):
        city_list.append(climate_data[x]['city'])
    return city_list

@app.route('/locations/<int:loc_num>', methods=['GET'])
def get_location_data(loc_num):
    '''
        This function returns all the information for 1 specific location given by a number from the user.
        Args:
            loc_num (int): the specific number (index) of the data set to look at
        Returns:
            climate_data[loc_num] (dict): a dictionary of location data include the ID, city, country, and monthlyAvg information for each month
    '''
    if loc_num >= len(climate_data):
        return "Error: Location value is not in the data set" , 400
    return climate_data[loc_num]

@app.route('/locations/<int:loc_num>/high-month', methods=['GET'])
def get_month_high(loc_num):
    '''
        This function returns the monthly average high tempature for 1 specific location given by a number from the user.
        Args:
            loc_num (int): the specific number (index) of the data set to look at
        Returns:
            highT (list): a list of the average high temperatures for each month in order for the chosen location
    '''
    highT = []
    if loc_num >= len(climate_data):
        return "Error: Location value is not in the data set" , 400
    for x in range(12):
        highT.append(climate_data[loc_num]['monthlyAvg'][x]['high'])
    return highT

@app.route('/locations/<int:loc_num>/high-year', methods=['GET'])
def get_yr_high(loc_num):
    '''
        This function returns the high temperature year average for 1 specific location given by a number from the user.
        Args:
            loc_num (int): the specific number (index) of the data set to look at
        Returns:
            yr_highT (int): the average high temperature for the chosen location for the year
    '''
    if loc_num >= len(climate_data):
        return "Error: Location value is not in the data set" , 400
    highT_list = get_month_high(loc_num)
    sum = 0
    for x in highT_list:
        sum = sum+x
    yr_highT = sum/12
    return str(yr_highT)

@app.route('/locations/<int:loc_num>/low-month', methods=['GET'])
def get_month_low(loc_num):
    '''
        This function returns the monthly average low tempatures for 1 specific location given by a number from the user.
        Args:
            loc_num (int): the specific number (index) of the data set to look at
        Returns:
            lowT (list): a list of the average low temperatures for each month in order for the chosen location
    '''
    if loc_num >= len(climate_data):
        return "Error: Location value is not in the data set" , 400
    lowT = []
    for x in range(12):
        lowT.append(climate_data[loc_num]['monthlyAvg'][x]['low'])
    return lowT

@app.route('/locations/<int:loc_num>/low-year', methods=['GET'])
def get_yr_low(loc_num):
    '''
        This function returns the avaerage low temperature for the year for 1 specific location given by a number from the user.
        Args:
            loc_num (int): the specific number (index) of the data set to look at
        Returns:
            yr_lowT (int): the average low temperature for the chosen location for the year
    '''
    if loc_num >= len(climate_data):
        return "Error: Location value is not in the data set" , 400
    lowT_list = get_month_low(loc_num)
    sum = 0
    for x in lowT_list:
        sum = sum+x
    yr_lowT = sum/12
    return str(yr_lowT)

@app.route('/locations/<int:loc_num>/dry-month', methods=['GET'])
def get_month_dry(loc_num):
    '''
        This function returns the monthly average dry days for 1 specific location given by a number from the user.
        Args:
            loc_num (int): the specific number (index) of the data set to look at
        Returns:
            dry (list): a list of the average dry days for each month in order for the chosen location
    '''
    if loc_num >= len(climate_data):
        return "Error: Location value is not in the data set" , 400
    dry = []
    for x in range(12):
        dry.append(climate_data[loc_num]['monthlyAvg'][x]['dryDays'])
    return dry

@app.route('/locations/<int:loc_num>/dry-year', methods=['GET'])
def get_yr_dry(loc_num):
    '''
        This function returns the average number of dry days a year for 1 specific location given by a number from the user.
        Args:
            loc_num (int): the specific number (index) of the data set to look at
        Returns:
            yr_dry (int): the average nunmber of dry days for the chosen location for the year
    '''
    if loc_num >= len(climate_data):
        return "Error: Location value is not in the data set" , 400
    dry_list = get_month_dry(loc_num)
    sum = 0
    for x in dry_list:
        sum = sum+x
    yr_dry = sum/12
    return str(yr_dry)

@app.route('/locations/<int:loc_num>/snow-month', methods=['GET'])
def get_month_snow(loc_num):
    '''
        This function returns the monthly average snow days for 1 specific location given by a number from the user.
        Args:
            loc_num (int): the specific number (index) of the data set to look at
        Returns:
            snow (list): a list of the average snow days for each month in order for the chosen location
    '''
    if loc_num >= len(climate_data):
        return "Error: Location value is not in the data set" , 400
    snow = []
    for x in range(12):
        snow.append(climate_data[loc_num]['monthlyAvg'][x]['snowDays'])
    return snow

@app.route('/locations/<int:loc_num>/snow-year', methods=['GET'])
def get_yr_snow(loc_num):
    '''
        This function returns the average number of snow days a year for 1 specific location given by a number from the user.
        Args:
            loc_num (int): the specific number (index) of the data set to look at
        Returns:
            yr_snow (int): the average nunmber of snow days for the chosen location for the year
    '''
    if loc_num >= len(climate_data):
        return "Error: Location value is not in the data set" , 400
    snow_list = get_month_snow(loc_num)
    sum = 0
    for x in snow_list:
        sum = sum+x
    yr_snow = sum/12
    return str(yr_snow)

@app.route('/locations/<int:loc_num>/rainfall-month', methods=['GET'])
def get_month_rainfall(loc_num):
    '''
        This function returns the monthly average rainfall for 1 specific location given by a number from the user.
        Args:
            loc_num (int): the specific number (index) of the data set to look at
        Returns:
            rainfall (list): a list of the average rainfall for each month in order for the chosen location
    '''
    if loc_num >= len(climate_data):
        return "Error: Location value is not in the data set" , 400
    rainfall = []
    for x in range(12):
        rainfall.append(climate_data[loc_num]['monthlyAvg'][x]['rainfall'])
    return rainfall

@app.route('/locations/<int:loc_num>/rainfall-year', methods=['GET'])
def get_yr_rainfall(loc_num):
    '''
        This function returns the average rainfall in a year for 1 specific location given by a number from the user.
        Args:
            loc_num (int): the specific number (index) of the data set to look at
        Returns:
            yr_rainfall (int): the average rainfall for the chosen location for the year
    '''
    if loc_num >= len(climate_data):
        return "Error: Location value is not in the data set" , 400
    rain_list = get_month_rainfall(loc_num)
    sum = 0
    for x in rain_list:
        sum = sum+x
    yr_rainfall = sum/12
    return str(yr_rainfall)

@app.route('/locations/<int:loc_num>/year', methods=['GET'])
def get_yrly_avs(loc_num):
    '''
        This function returns the cliamtes yearly averages for 1 specific location given by a number from the user.
        Args:
            loc_num (int): the specific number (index) of the data set to look at
        Returns:
            yr_avs (dict): a dictionary of the averages for the year which includes highTemp, lowTemp, dryDays, snowDays, and rainfall
    '''
    if loc_num >= len(climate_data):
        return "Error: Location value is not in the data set" , 400
    yr_avs = {}
    yr_avs['highTemp'] = get_yr_high(loc_num)
    yr_avs['lowTemp']= get_yr_low(loc_num)
    yr_avs['dryDays']= get_yr_dry(loc_num)
    yr_avs['snowDays']= get_yr_snow(loc_num)
    yr_avs['rainfall']= get_yr_rainfall(loc_num)
    return yr_avs

@app.route('/help', methods=['GET'])
def all_routes():
    '''
        This function returns a list of all the possible routes in this API and a short description of what they each return.
     Returns:
            (str): a string with routes and what they return
    '''
    welcome = "Welcome to Help! Below are available routes and their return statements. \n \n"
    r1 = ("The route '/data' returns the entire data set. \n") 
    r2 = ("The route '/countries' returns a list of all the countries in the data set. \n") 
    r3= ("The route '/locations' returns a list of epochs in the data set between offset and limit. If offset is not given then the list will start at the first epoch and if limit is not given the list will end at the last epoch. \n")
    r4 =("The route '/locations/<loc_num>' returns a dictionary of the specific epoch data set requested with unique keys about its position and velocity data. \n")
    r5 = ("The route '/locations/<loc_num>/high-month' returns the average high temperatures for each month given a specific location number/id in the dataset \n")
    r6 =("The route '/locations/<loc_num>/high-year' returns the yearly average high temperature for a specific location number/id in the dataset \n")
    r7 =("The route '/locations/<loc_num>/low-month' returns the average low temperatures for each month given a specific location number/id in the dataset \n")
    r8 = ("The route '/locations/<loc_num>/low-year' returns the yearly average low temperature for a specific location number/id in the dataset \n")
    r9 = ("The route '/locations/<loc_num>/dry-month' returns the average number of dry days for each month given a specific location number/id in the dataset  \n")
    r10 = ("The route '/locations/<loc_num>/dry-year' returns the yearly number of dry days for a specific location number/id in the dataset \n")
    r11 = ("The route '/locations/<loc_num>/snow-month' returns the average number of snow days for each month given a specific location number/id in the dataset \n")
    r12 = ("The route '/locations/<loc_num>/snow-year' returns the yearly number of snow days for a specific location number/id in the dataset \n")
    r13 = ("The route '/locations/<loc_num>/rainfall-month' returns the average rainfall for each month given a specific location number/id in the dataset \n")
    r14 = ("The route '/locations/<loc_num>/rainfall-year' returns the yearly rainfall for a specific location number/id in the dataset \n")
    r15 = ("The route '/locations/<loc_num>/year' returns the cliamtes yearly averages for a specific location number/id in the dataset \n")
    
    return welcome +r1 + r2 +r3 +r4 +r5 +r6+r7+r8+r9+r10+r11+r12+r13+r14+r15
    
    
#-----------------------------end of routes--------------------------------

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
