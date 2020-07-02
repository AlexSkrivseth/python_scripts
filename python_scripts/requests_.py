import requests
import datetime


url_endpoint = "http://127.0.0.1:3000/get_data/1/write_file/kiln_data_txt"
now = datetime.datetime.now()
now = str(now)
payload = {"Kiln1_TEMP":"156", "Kiln1_HUMID":"28", "Kiln2_TEMP":"79", "Kiln_HUMID":"80", "Time":now}

r = requests.post(url_endpoint, params=payload)
