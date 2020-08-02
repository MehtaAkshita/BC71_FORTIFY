import requests
from pprint import pprint
import cv2
import json


vidcap = cv2.VideoCapture('Highway.mp4')
#regions = ['fr', 'it']
c = 5000
x = 0
y = 0

fp = "manipalrun\\temp.jpg"
success,image = vidcap.read()
vidcap.set(cv2.CAP_PROP_POS_MSEC,5000)
while success==True:
    success,image = vidcap.read()
    c = c+500
###################################################
    #center_coordinates = (260,0)
    #center_coordinates = (0,350)
    #center_coordinates = (580,0)
    #center_coordinates = (380,720)
    #center_coordinates = (870,0)
    #center_coordinates = (970,720)
    image = cv2.line(image, (260, 0), (0, 350), (0, 255, 0), thickness=4)
    image = cv2.line(image, (580,0), (380, 720), (0, 255, 0), thickness=4)
    image = cv2.line(image, (870,0), (970,720), (0, 255, 0), thickness=4)
    image = cv2.circle(image, (x,y), 15, (0,0,255), 5)
###############################################
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
            ages2 = [li['box'] for li in a]
            xmin = [li['xmin'] for li in ages2]
            xmax = [li['xmax'] for li in ages2]
            ymin = [li['ymin'] for li in ages2]
            ymax = [li['ymax'] for li in ages2]
            x = (xmin[0] + xmax[0])//2
            y = (ymin[0] + ymax[0])//2
            position1 = ((0 - 260) * (y - 0) - (350 - 0) * (x- 260)) > 0
            position2 = ((380 - 580) * (y - 0) - (720 - 0) * (x - 580)) > 0 
            position3 = ((970 - 870) * (y - 0) - (720 - 0) * (x - 870)) > 0 
            if(position1 == False and position3 ==True and position2 ==False):
                temp = "lane3"
            elif(position1 == False and position3 ==True and position2 ==True):
                temp = "lane2"
            elif(position1 == False and position3 ==False and position2 ==False):
                temp = "lane4"
            elif(position1 == True and position3 ==True and position2 ==True):
                temp = "lane1"
            else:
                temp = "NaN"
            ages.append(temp)
            if(ages==[]):
                continue
            else:
                print(ages)

        except Exception as e:
            continue
    fp.close()
