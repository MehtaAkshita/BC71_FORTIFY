import requests
from pprint import pprint
import cv2
import json


vidcap = cv2.VideoCapture('Highway.mp4')
#regions = ['fr', 'it']
c = 5000
fp = "manipalrun\\temp.jpg"
success,image = vidcap.read()
vidcap.set(cv2.CAP_PROP_POS_MSEC,5000)
while success==True:
    success,image = vidcap.read()
    c = c+500
    cv2.imshow("+500",image)
    cv2.imwrite("manipalrun\\temp.jpg", image)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
    vidcap.set(cv2.CAP_PROP_POS_MSEC,c)
    with open('manipalrun\\temp.jpg', 'rb') as fp:
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            # data=dict(regions=regions),  # Optional
            files=dict(upload=fp),
            headers={'Authorization': 'Token e51e886ac73bae80c70f612e573a77f7ca5b40df'})
        try:
            a=response.json()['results']
            

            ages = [li['plate'] for li in a]
            if(ages==[]):
                continue
            else:
                print(ages)


            
        except Exception:
            print('Not detected!')
    fp.close()
