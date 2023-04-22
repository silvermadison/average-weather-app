from flask import Flask, request
#import requests
#import redis
import json
#import os
#from matplotlib import pyplot as plt
#import numpy as np

app = Flask(__name__)

with open('climate.json', 'r') as f:
    climate_data = json.load(f)


@app.route('/data', methods=['GET'])
def handle_data():
    return climate_data
    

@app.route('/countries', methods=['GET'])
def get_countries():
    country_list = []
    for item in climate_data:
        country = climate_data['country']
        for x in country_list:
            if country!=x:
                country_list.append[country]
    return country_list

@app.route('/locations', methods=['GET'])
def get_cities():
    city_list = []
    for item in climate_data:
        city_list.append(climate_data['city'])
    return city_list

@app.route('/locations/<int:id_num>', methods=['GET'])
def get_location_data(id_num):
    if id_num >= len(climate_data):
        return "Error: ID value is not in the data set" , 400
    return climate_data[id_num]


#-----------------------------end of routes--------------------------------

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
