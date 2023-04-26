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
    city_list = []
    max_list = len(climate_data)
    for x in range(max_list):
        city_list.append(climate_data[x]['city'])
    return city_list

@app.route('/locations/<int:loc_num>', methods=['GET'])
def get_location_data(loc_num):
    if loc_num >= len(climate_data):
        return "Error: Location value is not in the data set" , 400
    return climate_data[loc_num]

@app.route('/locations/<int:loc_num>/high-month', methods=['GET'])
def get_month_high(loc_num):
    highT = []
    for x in range(12):
        highT.append(climate_data[loc_num]['monthlyAvg'][x]['high'])
    return highT

@app.route('/locations/<int:loc_num>/high-year', methods=['GET'])
def get_yr_high(loc_num):
    highT_list = get_month_high(loc_num)
    sum = 0
    for x in highT_list:
        sum = sum+x
    yr_highT = sum/12
    return str(yr_highT)

@app.route('/locations/<int:loc_num>/low-month', methods=['GET'])
def get_month_low(loc_num):
    lowT = []
    for x in range(12):
        lowT.append(climate_data[loc_num]['monthlyAvg'][x]['low'])
    return lowT

@app.route('/locations/<int:loc_num>/low-year', methods=['GET'])
def get_yr_low(loc_num):
    lowT_list = get_month_low(loc_num)
    sum = 0
    for x in lowT_list:
        sum = sum+x
    yr_lowT = sum/12
    return str(yr_lowT)

@app.route('/locations/<int:loc_num>/dry-month', methods=['GET'])
def get_month_dry(loc_num):
    dry = []
    for x in range(12):
        dry.append(climate_data[loc_num]['monthlyAvg'][x]['dryDays'])
    return dry

@app.route('/locations/<int:loc_num>/dry-year', methods=['GET'])
def get_yr_dry(loc_num):
    dry_list = get_month_dry(loc_num)
    sum = 0
    for x in dry_list:
        sum = sum+x
    yr_dry = sum/12
    return str(yr_dry)

@app.route('/locations/<int:loc_num>/snow-month', methods=['GET'])
def get_month_snow(loc_num):
    snow = []
    for x in range(12):
        snow.append(climate_data[loc_num]['monthlyAvg'][x]['snowDays'])
    return snow

@app.route('/locations/<int:loc_num>/snow-year', methods=['GET'])
def get_yr_snow(loc_num):
    snow_list = get_month_snow(loc_num)
    sum = 0
    for x in snow_list:
        sum = sum+x
    yr_snow = sum/12
    return str(yr_snow)

@app.route('/locations/<int:loc_num>/rainfall-month', methods=['GET'])
def get_month_rainfall(loc_num):
    rainfall = []
    for x in range(12):
        rainfall.append(climate_data[loc_num]['monthlyAvg'][x]['rainfall'])
    return rainfall

@app.route('/locations/<int:loc_num>/rainfall-year', methods=['GET'])
def get_yr_rainfall(loc_num):
    rain_list = get_month_rainfall(loc_num)
    sum = 0
    for x in rain_list:
        sum = sum+x
    yr_rainfall = sum/12
    return str(yr_rainfall)

@app.route('/locations/<int:loc_num>/year', methods=['GET'])
def get_yrly_avs(loc_num):
    yr_avs = {}
    yr_avs['highTemp'] = get_yr_high(loc_num)
    yr_avs['lowTemp']= get_yr_low(loc_num)
    yr_avs['dryDays']= get_yr_dry(loc_num)
    yr_avs['snowDays']= get_yr_snow(loc_num)
    yr_avs['rainfall']= get_yr_rainfall(loc_num)
    return yr_avs

#-----------------------------end of routes--------------------------------

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
