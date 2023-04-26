from flask import Flask, request, send_file
import requests
import redis
import json
import os
from matplotlib import pyplot as plt
import numpy as np
import hotqueue
import jobs

app = Flask(__name__)
def get_redis_client(db_numb:int,decode_ans:bool):
    '''
    This function connects to the redis database
    '''
    redis_ip = os.environ.get('REDIS_IP')
    if not redis_ip:
        raise Exception()
    return redis.Redis(host=redis_ip, port=6379, db=db_numb, decode_responses=decode_ans)
rd = get_redis_client(0, True)
rd_img = get_redis_client(1, False)

redis_ip = os.environ.get('REDIS_IP', '172.17.0.1')
q = HotQueue("queue", host=redis_ip, port=6379, db=1)


@app.route('/jobs', methods=['POST'])
def jobs_api():
    '''
      API route for creating a new job to do some analysis. This route accepts a JSON payload
      describing the job to be created.
    '''
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(jobs.add_job(job['start'], job['end']))


@app.route('/data', methods=['POST','GET','DELETE'])
def handle_data():
    '''
        This function will get, post, or delete a dataset about climate averages for various locations based on the method verb provided by the user.
        Returns:
            output_list (list): returns the dataset (for GET)
                OR
            (str) : stating that the data was loaded (for POST) or deleted (for DELETE)
    '''
    if request.method =='GET':
        output_list = []
        for item in rd.keys():
            output_list.append(json.loads(rd.get(item)))
        return output_list
    elif request.method =='POST':
        response = requests.get('https://raw.githubusercontent.com/michaelx/climate/master/climate.json')
        for item in response.json()['response']['docs']:
            key = f'{item["hgnc_id"]}'
            rd.set(item.get('hgnc_id'),json.dumps(item))
        return "data loaded into redis"
    elif request.method == 'DELETE':
        rd.flushdb()
        return f"data deleted, there are {rd.keys()} keys in the database"
    else:
        return "the method you tried does not work"

@app.route('/countries', methods=['GET'])
def get_countries():
    '''
        This function gets a lsit of all the countries in the dataset
        Returns:
        countries (list): a list of countries in the climate dataset
    '''
    country_list = []
    alldata = []
    for item in rd.keys():
        alldata.append()json.loads(rd.get(item)))
    max_list = len(alldata)
    for x in range(max_list):
        country_list.append(alldata[x]['country'])
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
    alldata = []
    for item in rd.keys():
        alldata.append()json.loads(rd.get(item)))
    max_list = len(alldata)
    for x in range(max_list):
        city_list.append(alldata[x]['city'])
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
    alldata = []
    for item in rd.keys():
        alldata.append()json.loads(rd.get(item)))
    if loc_num >= len(alldata):
        return "Error: Location value is not in the data set" , 400
    return alldata[loc_num]

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
    for item in rd.keys():
        alldata.append()json.loads(rd.get(item)))
    if loc_num >= len(alldata):
        return "Error: Location value is not in the data set" , 400
    for x in range(12):
        highT.append(alldata[loc_num]['monthlyAvg'][x]['high'])
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
    for item in rd.keys():
        alldata.append()json.loads(rd.get(item)))
    if loc_num >= len(alldata):
        return "Error: Location value is not in the data set" , 400
    highT_list = get_month_high(loc_num)
    sum = 0
    for x in highT_list:
        sum = sum+x
    yr_highT = sum/12
    return str(yr_highT)

@app.route('/locations/<int:loc_num>/high-month/plot', methods=['GET', 'POST', 'DELETE'])
def get_month_high(loc_num):
    '''
    This function will get, post, or delete an image from the dataset based on the method verb provided by the user.
    Returns:
        image(png): histogram of the average high temperatures by month for a given location num/ID
        OR
        (str): stating the the image in the database has been posted or deleted
    '''
    if request.method == 'GET':
        if rd_img.exists('highT_avs'):
            with open('./highT_avs.png', 'wb') as f:
                f.write(rd_img.get('highT_avs'))
            return send_file('./highT_avs.png', minetype='highT_avs/png', as_attachment=True)#send image to user
        else:
            return 'there is no image in the database'

    elif request.method == 'POST':
        for item in rd.keys():
            alldata.append()json.loads(rd.get(item)))
        if loc_num >= len(alldata):
            return "Error: Location value is not in the data set" , 400
        highT = get_month_high(loc_num)
        #bar_labels = ['Jaunary','February', 'March', 'April', 'May', 'June', 'July', 'August', 'September','October', 'November', 'December' ]
        plt.hist(highT, 5)
        title = f'Average High Temperatures in {alldata[loc_num]["city"]}'
        plt.title(title)
        plt.xlabel('Months (Jan to Dec)')
        plt.ylabal('Temperature in Celsius')
        plt.savefig('./highT_avs.png')
        filebytes = open('./highT_avs.png','rb').read()
        rd_img.set('highT_avs', filebytes)
        return 'the image has been uploaded to the database.\n'

    elif request.method == 'DELETE':
        rd_img.flushdb()
        return 'the image has been deleted from the database'
    
    else:
        return 'error in requested method', 400

#______________________end of routes________________________
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
