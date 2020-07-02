import json
#import Adafruit_DHT as dht
import datetime
import requests
import time

# all of this running in  while loop every 10 seconds
#Read the sensor and store the Temp and Humid in variables.
def celcius_farenheit(x):
    f = (x * 1.8) + 32
    return f
while True:
    try:
        #h,t = dht.read_retry(dht.DHT22, 4)

        #temp = str(round(celcius_farenheit(t),2))
        temp = "143"
        #humid = str(round(h,2))
        humid = "45"
        # create the time stamp
        now = str(datetime.datetime.now())

        #store all the data in a dictionary
        data = {}
        data["Kiln #2"] = []

        data["Kiln #2"].append({
        "Temperature":temp,
        "Humidity":humid,
        "Time":now
        })

        # converting the python dictionary to json
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)

        #uploading the data to the server 
        url_endpoint = "http://cclhkilns.ngrok.io/get_data/2/write_file/kiln-2-data"

        r = requests.post(url_endpoint, json=data)
        time.sleep(10)
    except:
        print(Exception)
        time.sleep(20)
        continue
