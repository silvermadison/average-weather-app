FROM python:3.8.10
  
RUN pip install Flask==2.2.2
RUN pip install requests==2.22.0

COPY average-weather-app.py /average-weather-app.py

CMD ["python", "average-weather-app.py"]

