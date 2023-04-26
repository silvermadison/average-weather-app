# "Average" Weather App

## Objective
This API uses software design principles to help a user understand the climate of an area in the Climate Data database with over 100 cities accross the world.

## Contents
This folder includes ... 


## Required Modules
This project requires the installation of the requests, Flask, json, redis, matplotlib, os, numpy, and hotqueue modules. Install these modules with the ```pip install``` command in the command line (note: an additional ```-- user``` is needed after install and before the module name for both requests and flask). This project also requires a console with Kubernetes access.


## Climate Data
... take from writeup


### Part 1 - Routes
Below are app routes to navigate this API. The requests, json, and redis modules are used to turn the climate data into a usable dictionary that is then stored in redis. 


| Route | Method | What it should return | 
| ---------------------------- | ---------------------------- | ---------------------------- |
| ```/data``` | GET | return all data from redis |
| ```/data``` | POST |  put data into redis | 
| ```/data``` | DELETE | delete data in redis | 
| ```/countries``` | GET | returns a list of all the countries in the data set |
| ```/locations``` | GET | returns a list of cities in the dataset |
| ```/locations/<loc_num>``` | GET | returns a dictionary of climate data associated with a given location number/id in the dataset |
| ```/locations/<loc_num>/high-month``` | GET | returns the average high temperatures for each month given a specific location number/id in the dataset | 
| ```/locations/<loc_num>/high-year``` | GET | returns the yearly average high temperature for a specific location number/id in the dataset |
| ```/locations/<loc_num>/high-month/plot``` | GET | retrieves the histogram image from redis if there is one | 
| ```/locations/<loc_num>/high-month/plot``` | POST | posts a histogram of the average high temperatures by month for a given location num/ID to redis | 
| ```/locations/<loc_num>/high-month/plot``` | DELETE | deletes an image from redis | 
| ```/locations/<loc_num>/low-month``` | GET | returns the average low temperatures for each month given a specific location number/id in the dataset | 
| ```/locations/<loc_num>/low-year``` | GET | returns the yearly average low temperature for a specific location number/id in the dataset |
| ```/locations/<loc_num>/low-month/plot``` | GET | retrieves the histogram image from redis if there is one | 
| ```/locations/<loc_num>/low-month/plot``` | POST | posts a histogram of the average low temperatures by month for a given location num/ID to redis | 
| ```/locations/<loc_num>/low-month/plot``` | DELETE | deletes an image from redis | 
| ```/locations/<loc_num>/dry-month``` | GET | returns the average number of dry days for each month given a specific location number/id in the dataset | 
| ```/locations/<loc_num>/dry-year``` | GET | returns the yearly average average number of dry days for a specific location number/id in the dataset |
| ```/locations/<loc_num>/dry-month/plot``` | GET | retrieves the histogram image from redis if there is one | 
| ```/locations/<loc_num>/dry-month/plot``` | POST | posts a histogram of the average number of dry days by month for a given location num/ID to redis | 
| ```/locations/<loc_num>/dry-month/plot``` | DELETE | deletes an image from redis | 
| ```/locations/<loc_num>/snow-month``` | GET | returns the average number of snow days for each month given a specific location number/id in the dataset | 
| ```/locations/<loc_num>/snow-year``` | GET | returns the yearly average average number of snow days for a specific location number/id in the dataset |
| ```/locations/<loc_num>/snow-month/plot``` | GET | retrieves the histogram image from redis if there is one | 
| ```/locations/<loc_num>/snow-month/plot``` | POST | posts a histogram of the average number of snow days by month for a given location num/ID to redis | 
| ```/locations/<loc_num>/snow-month/plot``` | DELETE | deletes an image from redis | 
| ```/locations/<loc_num>/rainfall-month``` | GET | returns the average rainfall for each month given a specific location number/id in the dataset | 
| ```/locations/<loc_num>/rainfall-year``` | GET | returns the yearly average rainfall for a specific location number/id in the dataset |
| ```/locations/<loc_num>/rainfall-month/plot``` | GET | retrieves the histogram image from redis if there is one | 
| ```/locations/<loc_num>/rainfall-month/plot``` | POST | posts a histogram of the average rainfall by month for a given location num/ID to redis | 
| ```/locations/<loc_num>/rainfall-month/plot``` | DELETE | deletes an image from redis | 
| ```/locations/<loc_num>/year``` | GET | returns the cliamtes yearly averages for a specific location number/id in the dataset | 



### Part 2 - Dockerfile 
The Dockerfile contains commands for building a new image. When creating the Dockerfile the image should contain the same versions of modules as you are using on the Jetstream VM; this will be reflected in the ```FROM``` and ```RUN``` instructions. We will do this for the modules python, flask, and requests.


To check your version of python run ```python3``` in the VM command line. Output should look similar to:
```
Python 3.8.10 (default, Nov 14 2022, 12:59:47) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
The first line shows you the version of python you are using, in this case I am using Python 3.8.10. This same version is contained in the ```FROM``` instruction in the Dockerfile.

To check your version of flask, in the VM command line run ```pip freeze | grep Flask```. Output should look similar to:
```
Flask==2.2.2
```
The version of Flask I am using is 2.2.2 and this version is also used in the ```RUN``` instruction in the Dockerfile.

Follow similar instruction above for the remaining RUN commands in the Dockerfile (requests, matplotlib, redis, and HotQueue modules). 


## Instructions
### Pull the Image from Docker Hub
To get the image from Docker Hub use the command ```docker pull danielasanchez/aw_app:1.0```.


### Build a New Image from This Dockerfile
In order to retrieve the data from this repository use the command
```
git clone git@github.com:DanielaLeticia/weather_restAPI.git
```
This will provide you with all the data in this repository. 


Create the image using the command ```docker build -t danielasanchez/aw_app:1.0 .```.


Check to make sure the image is there using the command ```docker images```. Output should look similar to:
```
REPOSITORY                  TAG       IMAGE ID       CREATED          SIZE
danielasanchez/aw_app:1.0   1.0      9b88163e71e8   7 minutes ago    897MB
```


### Kubernetes
All the yaml files in the repository need to be created and uploaded to Kubernetes. Do so through the command ```kubectl apply -f <filename>``` on the Kubernetes accessible machine. After each command line you should get a statement saying the file was created. 
Ensure the files are running properly. For the command ```kubectl get pods``` output should look like:
```
NAME                                            READY   STATUS    RESTARTS        AGE
weather-app-api-deployment-686fd5ff69-h6vkk     1/1     Running   0               2h
weather-app-redis-deployment-57667bb9f6-n5xhg   1/1     Running   0               3h
weather-app-wrk-deployment-686fd5ff69-trhlw     1/1     Running   0               3h
py-debug-deployment-f484b4b99-wxdsx             1/1     Running   0               8d
```
And, for the command ```kubectl get services``` output should look similar to:
```
NAME                           TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
weather-app-redis-service      ClusterIP   10.233.7.221    <none>        5000/TCP         58m
weather-app-service-nodeport   NodePort    10.233.9.14     <none>        5000:31863/TCP   59m

``` 


### Accessing the API
After running the ```kubectl get pods``` command, notice the python debug deployment pod. In order to make commands on the API, we will need to run a shell in this pod. Do so with: ```kubectl exec -it <python debug deployment pod name> – /bin/bash```.
The shell prompt should change to the following, which shows that you are “inside” the container: ```root@py-debug-deployment-f484b4b99-wxdsx:/#```. From here, run an API route. Note the Cluster-IP address for your service after the command  ```kubectl get services```. This IP will be used in replacement for “localhost”.

### API Command Examples
The ```/data``` and ```/image``` routes include three different methods (POST, GET, DELETE). To specify which method use the notation ```-X <METHOD>``` after the curl command. If no method is specified, it is assumed to be a “GET” method. The ```/data``` will complete one of the three tasks based on the method given: **post** the data to Redis, return/**get** the data for the user, or **delete** the data from the Redis database. 

Similarly all the routes with "/plot" at the end of the route will need a method specified. These routes will complete one of the three tasks based on the method given: **post** the image to Redis which is a histogram of monthly averages of a climate group(high temp, low temp, dry days, snow days, or rainfall) from a specific location in the databse, return/**get** the image to the user, or **delete** the image from the Redis database.
An example: ```curl -X DELETE 10.233.7.221:5000/ ....```
```
data deleted, there are 0 keys in the database
```
The ```ROUTE``` route returns ... Use the command: ```curl 10.233.7.221:5000/ ....```.

The ```ROUTE``` route returns ... Use the command: ```curl 10.233.7.221:5000/ ....```.
