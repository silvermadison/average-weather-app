# "Average" Weather App

## Objective
This API uses software design principles to help a user understand the climate of an area in the Climate Data database with over 100 cities accross the world.

## Contents
This folder includes 1 script of the api routes, 7 yaml files, 2 scripts (worker and jobs), 2 Dockerfiles, 1 docker-compose, and a README. 


## Required Modules
This project requires the installation of the requests, Flask, json, redis, matplotlib, os, numpy, and hotqueue modules. Install these modules with the ```pip install``` command in the command line (note: an additional ```-- user``` is needed after install and before the module name for both requests and flask). This project also requires a console with Kubernetes access.


## Climate Data
The data set itself contains 105 dictionaries, these are the cities and each dictionary contains dictionaries within those. There are twelve of these nested dictionaries, one for each month of the year, that each contain data for the corresponding month. Information for every month includes the average high temperature, the average lowest temperature, average dry days, average snow days, and the average rainfall. It is important to note that the temperatures are Celsius and the rainfall is in millimeters. This is also stated in the output of the code. 

More information about this climate data can be found at this website: https://michaelxander.com/climate-data/
The git repository being used in this project can also be accessed here: https://github.com/michaelx/climate


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
| ```/locations/<loc_num>/year``` | GET | returns the climates yearly averages for a specific location number/id in the dataset | 



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

### Accessing this Repository
In order to retrieve the data from this repository use the command
```
git clone git@github.com:DanielaLeticia/weather_restAPI.git
```
This will provide you with all the data in this repository. 

### Docker Image
#### Build a New Image from This Dockerfile
First, it is important that we are signed into DockerHub. This can be done through their website by using a simple username and password. Next, in the command line, you must have all of the files needed in one folder in order to push to DockerHub. Files that are necessary include the main API file, docker-compose.yml, and the Dockerfile. Then, type the command ```docker build -t <username>/<api_file>:<version> .```. The username should be your DockerHub username, the api_file should be the name of the main API script, and the version is the version of the image. In this case, create the image using the command ```docker build -t danielasanchez/aw_app:1.0 .```. It is always a good idea to start with version 1.0. Check to make sure the image is there using the command ```docker images```. Output should look similar to:
```
REPOSITORY                  TAG       IMAGE ID       CREATED          SIZE
danielasanchez/aw_app:1.0   1.0      9b88163e71e8   7 minutes ago    897MB
```
After executing this command and noticing the image has been created, you are ready to push to DockerHub. The next step is to log into DockerHub through the command line by using the command: ```docker login``` . You should get a “Login Succeeded” message when the command is executed. Lastly, push the image to DockerHub using the command: ```docker push <username>/<api_file>:<version>```. You should get a “Pushed” message and that is how you know the push was complete. You may now be able to go into DockerHub and see that the image is now stored. 

#### Pull the Image from DockerHub
Pulling an image from DockerHub is also quite simple, you must also be logged into Docker in order to retrieve images. The pull process takes one simple command: `docker pull <image_name>` or `docker image pull <image_name>`. These both will do the same thing. It is important to note that if there is no :<version> specified, docker will automatically assume that you are trying to pull the latest version. To get the image from Docker Hub use the command ```docker pull danielasanchez/aw_app:1.0```.

### Kubernetes
All the yaml files in the repository need to be created and uploaded to Kubernetes. Do so through the command ```kubectl apply -f <filename>``` on the Kubernetes accessible machine. After each command line you should get a statement saying the file was created. 
Ensure the files are running properly using ```kubectl get``` commands for the pvc, pods, and services. For the command ```kubectl get pods``` output should look like:
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

#### Note on Ports
Note the NodePort address for your service after the command  ```kubectl get services```. The IP following "5000:" for the ```weather-app-service-nodeport``` service, which in this case is 31863, will be used in the ```weather-prod-api-ingress.yml``` in port: number: . Make sure this is the correct port number for your machine or else you will not be able to use this API from any machine. 

### Accessing the API
This API can be curled from any machine using the command ```curl msilver.coe332.tacc.cloud/<ROUTE>```.

### API Command and Output Examples
The ```/data``` and ```... /plot``` routes include three different methods (POST, GET, DELETE). To specify which method use the notation ```-X <METHOD>``` after the curl command. If no method is specified, it is assumed to be a “GET” method. 
The ```/data``` will complete one of the three tasks based on the method given: **post** the data to Redis, return/**get** the data for the user, or **delete** the data from the Redis database. The ```.../plot``` routes will complete one of the three tasks based on the method given: **post** the image to Redis which is a histogram of monthly averages of a climate group(high temp, low temp, dry days, snow days, or rainfall) from a specific location in the databse, return/**get** the image to the user, or **delete** the image from the Redis database.


An example: ```curl msilver.coe332.tacc.cloud/data -X DELETE```
```
data deleted, there are [] keys in the database
```

The ```ROUTE``` route returns a list of all the countries in the data set. Use the command: ```curl msilver.coe332.tacc.cloud/countries```. Example output is:
```
[
  "United States",
  "India",
  "Morocco",
  "China",
  "Poland",
  "Spain",
  "Australia",
  "Chile",
  "Italy",
  "Canada",
  "Russia",
  "Portugal",
  "Ireland",
  "Mexico",
  "Belgium",
  "Turkey",
  "Iceland",
  "New Zealand",
  "Singapore",
  "Hong Kong",
  "Switzerland",
  "Brazil",
  "Thailand",
  "Netherlands",
  "Norway",
  "Hungary",
  "South Africa",
  "Indonesia",
  "Germany",
  "Czech Republic",
  "France",
  "Israel",
  "Argentina",
  "Bulgaria",
  "Japan",
  "Denmark",
  "Malaysia",
  "United Arab Emirates",
  "United Kingdom",
  "Sweden",
  "Vietnam",
  "Hawaii",
  "Greece",
  "Austria",
  "South Korea"
]
```

The ```ROUTE``` route returns ... Use the command: ```curl msilver.coe332.tacc.cloud/locations/0/high-year```.
```

```
