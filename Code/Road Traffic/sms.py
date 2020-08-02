import requests
import json

def send_sms():
        url = "https://www.fast2sms.com/dev/bulk"

        querystring = {"authorization":"FPAv82Qgexoyqdika4lmnY7ERrHh6Ww10KZcXUJNL9bV3IBzuGP8wB4Neu2lQUpYOcM3Tj1VKXSHJnFi","sender_id":"FSTSMS","message":"Move to the left ambulance is coming","language":"english","route":"p","numbers":"9971197421"}

        headers = {
            'cache-control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

<<<<<<< HEAD
=======
print(response.text)
>>>>>>> 684307752e7f78fca3b61cb672de43d6ff0a19f2
