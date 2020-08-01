#original_loc=dest_loc

def mapsUrlGenerator(origin_loc, waypoints):
    url_ext_origin_loc = origin_loc.replace(',','%2C').replace(' ','+')
    url_ext_waypoints = (("%7C".join(waypoints)).replace(',','%2C')).replace(' ','+')

    maps_url = 'https://www.google.com/maps/dir/?api=1&origin={}&destination={}&travelmode=car&waypoints={}'.format(url_ext_origin_loc, url_ext_origin_loc, url_ext_waypoints)

    #return(maps_url)
    print(maps_url)



import requests
import json
from geopy.distance import great_circle 
send_url = 'http://api.ipstack.com/14.139.243.170?access_key=b6d88bf3e75b6649440117254013178d&format=1'
r = requests.get(send_url)
j = json.loads(r.text)
#print(j)
lat = j['latitude']
lon = j['longitude']
print(lat,lon)
a=str(lat)+', '+str(lon)
waypoints=['26.9098324, 75.8625336']
mapsUrlGenerator(a, waypoints)
    

import geopy.distance

coords_1 =(26.98801040649414,75.86103057861328)
coords_2 = (26.9898773,75.8679118)

print (geopy.distance.vincenty(coords_1, coords_2).meters)
k=geopy.distance.vincenty(coords_1, coords_2).meters
if(k<2000):
    import requests
    import json

    URL = 'https://www.way2sms.com/api/v1/sendCampaign'

    # get request
    def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
      req_params = {
      'apikey':apiKey,
      'secret':secretKey,
      'usetype':useType,
      'phone': phoneNo,
      'message':textMessage,
      'senderid':senderId
      }
      return requests.post(reqUrl, req_params)
    response = sendPostRequest(URL, 'CVLSWAI97NCO29DWSL3CGC5F5X13DQAE', 'HAW9SHMMYU7AZ1VV', 'stage', '9167184485', 'isha', 'move to the left, an Ambulance is coming' )
    """
      Note:-
        you must provide apikey, secretkey, usetype, mobile, senderid and message values
        and then requst to api
    """
    # print response if you want
    print ( response.text)
