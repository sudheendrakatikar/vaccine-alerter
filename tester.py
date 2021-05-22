import requests
import json
from datetime import datetime, timedelta
from playsound import playsound

date = f"{datetime.now()+timedelta(days = 1) :%d-%m-%Y}"
pincodes = [ 411001, 411007, 411017, 411018, 411027, 411033, 411034 ]

api = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id=363&date='+date
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
print(api)
try:
    response = requests.get(api, headers=headers).json()
    for center in response['centers']:
        for session in center['sessions']:
            if session['available_capacity'] == 0:
                playsound('S:\\Projects\\vaccine-alert\\alert.wav', block=False)
                print(center['name'])
                print(center['address'])
                print(session['available_capacity'])
except Exception as e:
    print(e)
