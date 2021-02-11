# coding: utf-8

echo "# api-filler.py" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/tomhubert50400/api-filler.py.git
git push -u origin main

import time
import requests
from random import seed
from random import random

seed(1)
# generate random numbers between 0-1
while True:
        res = requests.get('http://api.weatherstack.com/current?access_key=7f4390e1e5c441bce30e182c61227707&query=Rouen')
        res = res.json()
        temp = res["current"]["temperature"]
        humidity = res["current"]["humidity"]
        parameters = {"temperature": temp, "humidity": humidity}
        print(parameters)
        res = requests.post('http://192.168.202.252:8080/create', json={"temperature": temp, "humidity": humidity})
        res = res.json()
        print(res)
        time.sleep(60*5)
