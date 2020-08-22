## Bootstrap Grid - adding style to the app
# -*- coding: utf-8 -*-
import io
from twilio.rest import Client
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
#import dash_table_experiments as dt
#import dash_table
#import base64
import webbrowser as wb
#import datetime
#import matplotlib.pyplot as plt
#import plotly.plotly as py
import dash_daq as daq
#import os,sys
import datetime
#import dash_table
#import numpy as np
#import numpy as np
#import pandas as pd
from bs4 import BeautifulSoup
import urllib3
#import json
#import plotly.graph_objs as go
#from flask import send_file
#import datafr
import urllib.request, json
#from win10toast import ToastNotifier
import gl
from flask import Flask, Response
import requests
import cv2
import pyttsx3
import json
import dash_dangerously_set_inner_html
import maps
import sms
import random


import cv2
import numpy as np
import Vehicle
import time
import globals



# import the necessary packages for drowsiness
from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2




account_sid = 'ACadce9a5af8f32f5df99026c01767cd8a'
auth_token = 'a8e3211584009c21cdc0843aae348033'
client = Client(account_sid, auth_token)

value=1.8
videos=['Downloads/1t.MP4','Downloads/2t.MP4','Downloads/3.MP4','Downloads/4.MP4']



l1r=['/home/beautisaurus/Desktop/hackverse/connected-cars-master/Code/Highway.mp4'] #[#"videoplayback.mp4",'Highway.mp4']

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(l1r[random.randint(0,0)])#'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self,x,y):
        success, image = self.video.read()
        if gl.c==5000:
            self.video.set(cv2.CAP_PROP_POS_MSEC,5000)
        image = cv2.line(image, (260, 0), (0, 350), (0, 255, 0), thickness=4)
        image = cv2.line(image, (580,0), (380, 720), (0, 255, 0), thickness=4)
        image = cv2.line(image, (870,0), (970,720), (0, 255, 0), thickness=4)
        image = cv2.circle(image, (x,y), 15, (0,0,255), 5)
        cv2.imwrite("manipalrun\\temp.jpg",image)
        ret, jpeg = cv2.imencode('.jpg', image)

        if gl.c>5000:
            self.video.set(cv2.CAP_PROP_POS_MSEC,gl.c)
        return jpeg.tobytes()


def gen(camera):
    gl.c = 5000
    c=0
    x = 0
    y = 0
    fp = "manipalrun\\temp.jpg"
    while True:
        gl.c += 500
        frame = camera.get_frame(x,y)

        if (c>1):
              
            with open('manipalrun\\temp.jpg', 'rb') as fp:
                response = requests.post(
                    'https://api.platerecognizer.com/v1/plate-reader/',
                    # data=dict(regions=regions),  # Optional
                    files=dict(upload=fp),
                    headers={'Authorization': 'Token 4276492405dad1a72f659131bdfc98219e7e3851'})
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
                    if not position1 and position3 and not position2:
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
                    ages.append("No zig zag detected")
                    if(ages==[]):
                        continue
                    else:
                        gl.number=ages
                        print(ages)
                except:
                    pass

        c+=1
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')




l1r=['/home/beautisaurus/Desktop/hackverse/connected-cars-master/Code/Highway.mp4'] #[#"videoplayback.mp4",'Highway.mp4']

class VideoCamera1(object):
    def __init__(self):
        self.video = cv2.VideoCapture('/home/beautisaurus/Desktop/hackverse/connected-cars-master/Code/Downloads/1t.mp4')#'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4')

    def __del__(self):
        self.video.release()

    def set_frame(self):
        return self.video

    def get_frame(self):
        success, image = self.video.read()
        try:
            ret, jpeg = cv2.imencode('.jpg', image)
        except:
            globals.excepts=1
        return image

class VideoCamera2(object):
    def __init__(self):
        self.video = cv2.VideoCapture('Downloads/2t.mp4')#'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4')

    def __del__(self):
        self.video.release()

    def set_frame(self):
        return self.video

    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return image


class VideoCamera3(object):
    def __init__(self):
        self.video = cv2.VideoCapture('/home/beautisaurus/Desktop/hackverse/connected-cars-master/Code/Downloads/3.mp4')#'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4')

    def __del__(self):
        self.video.release()

    def set_frame(self):
        return self.video

    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return image


class VideoCamera4(object):
    def __init__(self):
        self.video = cv2.VideoCapture('/home/beautisaurus/Desktop/hackverse/connected-cars-master/Code/Downloads/4.mp4')#'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4')

    def __del__(self):
        self.video.release()

    def set_frame(self):
        return self.video

    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return image


class VideoCamera5(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)#'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4')

    def __del__(self):
        self.video.release()

    def set_frame(self):
        return self.video

    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return image
    

def gen1(camera):

    globals.lane1=0
    globals.excepts=0

    cnt_up = 0
    cnt_down = 0
    UpMTR = 0
    UpLV = 0
    UpHV = 0
    DownLV = 0
    DownHV = 0
    w = 1280.0 #camera.set_frame.get(3)
    #print('Width', w)
    h = 720.0 #camera.set_frame.get(4)
    #print('Height', h)


    frameArea = h*w
    areaTH = frameArea/800


    # Input/Output Lines
    line_up = int(value*(h/5))
    line_down = int(1.7*(h/5))

    up_limit = int(1*(h/5))
    down_limit = int(4*(h/5))


    line_down_color = (255,0,0)

    pt1 = [0, line_down]

    pt2 = [w, line_down]
    pts_L1 = np.array([pt1,pt2], np.int32)
    pts_L1 = pts_L1.reshape((-1,1,2))


    pt5 = [0, up_limit]
    pt6 = [w, up_limit]
    pts_L3 = np.array([pt5,pt6], np.int32)
    pts_L3 = pts_L3.reshape((-1,1,2))
    pt7 = [0, down_limit]
    pt8 = [w, down_limit]
    pts_L4 = np.array([pt7,pt8], np.int32)
    pts_L4 = pts_L4.reshape((-1,1,2))

    # background subtractor
    fgbg = cv2.createBackgroundSubtractorMOG2()

    kernelOp = np.ones((3,3), np.uint8)
    kernelOp2 = np.ones((5,5), np.uint8)
    kernelCl = np.ones((11,11), np.uint8)

    #Variables
    font = cv2.FONT_HERSHEY_SIMPLEX
    vehicles = []
    max_p_age = 5
    pid = 1
    while True:

        try:
            frame = camera.get_frame()
        except:
            globals.excepts=1
        for i in vehicles:
            i.age_one()
        #################
        # PREPROCESSING #
        #################
        fgmask = fgbg.apply(frame)
        fgmask2 = fgbg.apply(frame)

        # Binary to remove shadow

        try:
            ret, imBin = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
            ret, imBin2 = cv2.threshold(fgmask2, 200, 255, cv2.THRESH_BINARY)
            #Opening (erode->dilate) to remove noise
            mask = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernelOp)
            mask2 = cv2.morphologyEx(imBin2, cv2.MORPH_OPEN, kernelOp)
            #Closing (dilate->erode) to join white region
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernelCl)
            mask2 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernelCl)
            #cv2.imshow('Image Threshold', cv2.resize(fgmask, (400, 300)))
            
        except:
            #If there is no more frames to show...
            print('EOF')
            print('down:', cnt_down)
            #print('DOWN:', cnt_down)
            break
        

        #
        ## FIND CONTOUR 

        contours0, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for cnt in contours0:
     
            cv2.drawContours(frame, cnt, -1, (0,255,0), 3, 8)
            area = cv2.contourArea(cnt)
            
            if area > areaTH:
           

                #   TRACKING   

                M = cv2.moments(cnt)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                x,y,w,h = cv2.boundingRect(cnt)


                new = True
                for i in vehicles:
                    if abs(x-i.getX()) <= w and abs(y-i.getY()) <= h:
                        new = False
                        i.updateCoords(cx,cy)   # Update the coordinates in the object and reset age
                        if i.going_UP(line_down, line_up) == True:
                            roi = frame[y:y + h, x:x + w]
                            rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            height = h
                            width = w
                            kll = 2 * (height + width)
                          
                            if kll < 300:
                                UpMTR += 1
                            elif kll < 500:
                                UpLV += 1
                            elif kll > 500:
                                UpHV += 1

                            
                            cnt_down += 1
                            print("ID:", i.getId(), 'crossed going up at', time.strftime("%c"))
                        elif i.going_DOWN(line_down, line_up) == True:
                            roi = frame[y:y+h, x:x+w]
                            rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            height = y+h
                            width = x+w
                            luas = height*width
                            
                            if luas < 600000:
                                DownLV += 1
                            elif luas > 600000:
                                DownHV += 1

                            
                            cnt_down += 1
                       
                        break
                    if i.getState() == '1':
                        if i.getDir() == 'down' and i.getY() > down_limit:
                            i.setDone()
                        elif i.getDir() == 'up' and i.getY() < up_limit:
                            i.setDone()
                    if i.timedOut():
                        # Remove from the list person
                        index = vehicles.index(i)
                        vehicles.pop(index)
                        del i
                if new == True:
                    p = Vehicle.MyVehicle(pid,cx,cy, max_p_age)
                    vehicles.append(p)
                    pid += 1

                ##################
                ##   DRAWING    ##
                ##################
                cv2.circle(frame,(cx,cy),5, (0,0,255), -1)
                img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                

        for i in vehicles:
            """
            if len(i.getTracks()) >= 2:
                pts = np.array(i.getTracks(), np.int32)
                pts = pts.reshape((-1,1,2))
                frame = cv2.polylines(frame, [pts], False, i.getRGB())
            if i.getId() == 9:
                print str(i.getX()), ',', str(i.getY())
            """
            #cv2.putText(frame, str(i.getId()), (i.getX(),i.getY()),font,0.3,i.getRGB(),1,cv2.LINE_AA)

        ##   IMAGE   
        str_up = 'CNT: ' + str(cnt_up)
        MTR_up = 'Up Motor: ' + str(UpMTR)
        LV_up = 'Up Mobil: ' + str(UpLV)
        HV_up = 'Up Truck/Bus: ' + str(UpHV)
        str_down = 'CNT: ' + str(cnt_down)
        LV_down = 'Down Mobil: ' + str(DownLV)
        HV_down = 'Down Truck/Bus: ' + str(DownHV)
        frame = cv2.polylines(frame, [pts_L1], False, line_down_color, thickness=2)
        #frame = cv2.polylines(frame, [pts_L2], False, line_up_color, thickness=2)
        globals.lane1=str_down
        frame = cv2.polylines(frame, [pts_L3], False, (255,255,255), thickness=1)
        frame = cv2.polylines(frame, [pts_L4], False, (255,255,255), thickness=1)
        cv2.putText(frame, str_down, (10,75),font,3,(0, 0, 255),5,cv2.LINE_AA)
        cv2.putText(frame, str_down, (10,75),font,3,(0, 0, 255),5,cv2.LINE_AA)

        ret, jpeg = cv2.imencode('.jpg', frame)

        frame=jpeg.tobytes()

        print('COUNT:', cnt_down,1)

        print(type(frame),1)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def gen2(camera):

    globals.lane2=0

    cnt_up = 0
    cnt_down = 0
    UpMTR = 0
    UpLV = 0
    UpHV = 0
    DownLV = 0
    DownHV = 0
    w = 1280.0 #camera.set_frame.get(3)
    #print('Width', w)
    h = 720.0 #camera.set_frame.get(4)
    #print('Height', h)



    frameArea = h*w
    areaTH = frameArea/800


    # Input/Output Lines
    line_up = int(value*(h/5))
    line_down = int(1.7*(h/5))

    up_limit = int(1*(h/5))
    down_limit = int(4*(h/5))


    line_down_color = (255,0,0)

    pt1 = [0, line_down]

    pt2 = [w, line_down]
    pts_L1 = np.array([pt1,pt2], np.int32)
    pts_L1 = pts_L1.reshape((-1,1,2))


    pt5 = [0, up_limit]
    pt6 = [w, up_limit]
    pts_L3 = np.array([pt5,pt6], np.int32)
    pts_L3 = pts_L3.reshape((-1,1,2))
    pt7 = [0, down_limit]
    pt8 = [w, down_limit]
    pts_L4 = np.array([pt7,pt8], np.int32)
    pts_L4 = pts_L4.reshape((-1,1,2))

    # background subtractor
    fgbg = cv2.createBackgroundSubtractorMOG2()

    kernelOp = np.ones((3,3), np.uint8)
    kernelOp2 = np.ones((5,5), np.uint8)
    kernelCl = np.ones((11,11), np.uint8)

    #Variables
    font = cv2.FONT_HERSHEY_SIMPLEX
    vehicles = []
    max_p_age = 5
    pid = 1
    while True:
        try:
            frame = camera.get_frame()
        except:
            globals.excepts=1
            
        for i in vehicles:
            i.age_one()
        #################
        # PREPROCESSING #
        #################
        fgmask = fgbg.apply(frame)
        fgmask2 = fgbg.apply(frame)

        # Binary to remove shadow

        try:
            ret, imBin = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
            ret, imBin2 = cv2.threshold(fgmask2, 200, 255, cv2.THRESH_BINARY)
            #Opening (erode->dilate) to remove noise
            mask = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernelOp)
            mask2 = cv2.morphologyEx(imBin2, cv2.MORPH_OPEN, kernelOp)
            #Closing (dilate->erode) to join white region
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernelCl)
            mask2 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernelCl)
            #cv2.imshow('Image Threshold', cv2.resize(fgmask, (400, 300)))
            
        except:
            #If there is no more frames to show...
            print('EOF')
            print('UP:', cnt_up)
            #print('DOWN:', cnt_down)
            break
        

        #
        ## FIND CONTOUR 

        contours0, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for cnt in contours0:
     
            cv2.drawContours(frame, cnt, -1, (0,255,0), 3, 8)
            area = cv2.contourArea(cnt)
            
            if area > areaTH:
           

                #   TRACKING   

                M = cv2.moments(cnt)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                x,y,w,h = cv2.boundingRect(cnt)


                new = True
                for i in vehicles:
                    if abs(x-i.getX()) <= w and abs(y-i.getY()) <= h:
                        new = False
                        i.updateCoords(cx,cy)   # Update the coordinates in the object and reset age
                        if i.going_UP(line_down, line_up) == True:
                            roi = frame[y:y + h, x:x + w]
                            rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            height = h
                            width = w
                            kll = 2 * (height + width)
                          
                            if kll < 300:
                                UpMTR += 1
                            elif kll < 500:
                                UpLV += 1
                            elif kll > 500:
                                UpHV += 1

                            
                            cnt_up += 1
                            print("ID:", i.getId(), 'crossed going up at', time.strftime("%c"))
                        elif i.going_DOWN(line_down, line_up) == True:
                            roi = frame[y:y+h, x:x+w]
                            rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            height = y+h
                            width = x+w
                            luas = height*width
                            
                            if luas < 600000:
                                DownLV += 1
                            elif luas > 600000:
                                DownHV += 1

                            
                            cnt_down += 1
                       
                        break
                    if i.getState() == '1':
                        if i.getDir() == 'down' and i.getY() > down_limit:
                            i.setDone()
                        elif i.getDir() == 'up' and i.getY() < up_limit:
                            i.setDone()
                    if i.timedOut():
                        # Remove from the list person
                        index = vehicles.index(i)
                        vehicles.pop(index)
                        del i
                if new == True:
                    p = Vehicle.MyVehicle(pid,cx,cy, max_p_age)
                    vehicles.append(p)
                    pid += 1

                ##################
                ##   DRAWING    ##
                ##################
                cv2.circle(frame,(cx,cy),5, (0,0,255), -1)
                img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                

        for i in vehicles:
            """
            if len(i.getTracks()) >= 2:
                pts = np.array(i.getTracks(), np.int32)
                pts = pts.reshape((-1,1,2))
                frame = cv2.polylines(frame, [pts], False, i.getRGB())
            if i.getId() == 9:
                print str(i.getX()), ',', str(i.getY())
            """
            #cv2.putText(frame, str(i.getId()), (i.getX(),i.getY()),font,0.3,i.getRGB(),1,cv2.LINE_AA)

        ##   IMAGE   
        str_up = 'CNT: ' + str(cnt_up)
        MTR_up = 'Up Motor: ' + str(UpMTR)
        LV_up = 'Up Mobil: ' + str(UpLV)
        HV_up = 'Up Truck/Bus: ' + str(UpHV)
        str_down = 'CNT: ' + str(cnt_down)
        LV_down = 'Down Mobil: ' + str(DownLV)
        HV_down = 'Down Truck/Bus: ' + str(DownHV)
        frame = cv2.polylines(frame, [pts_L1], False, line_down_color, thickness=2)
        #frame = cv2.polylines(frame, [pts_L2], False, line_up_color, thickness=2)
        frame = cv2.polylines(frame, [pts_L3], False, (255,255,255), thickness=1)
        frame = cv2.polylines(frame, [pts_L4], False, (255,255,255), thickness=1)
        globals.lane2=str_up
        cv2.putText(frame, str_up, (10,75),font,3,(0, 0, 255),5,cv2.LINE_AA)
        cv2.putText(frame, str_up, (10,75),font,3,(0, 0, 255),5,cv2.LINE_AA)


        ret, jpeg = cv2.imencode('.jpg', frame)

        frame=jpeg.tobytes()

        print('COUNT:', cnt_up,2)

        print(type(frame),2)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
def gen3(camera):

    globals.lane3=0

    cnt_up = 0
    cnt_down = 0
    UpMTR = 0
    UpLV = 0
    UpHV = 0
    DownLV = 0
    DownHV = 0
    w = 1280.0 #camera.set_frame.get(3)
    #print('Width', w)
    h = 720.0 #camera.set_frame.get(4)
    #print('Height', h)



    frameArea = h*w
    areaTH = frameArea/800


    # Input/Output Lines
    line_up = int(value*(h/5))
    line_down = int(1.7*(h/5))

    up_limit = int(1*(h/5))
    down_limit = int(4*(h/5))


    line_down_color = (255,0,0)

    pt1 = [0, line_down]

    pt2 = [w, line_down]
    pts_L1 = np.array([pt1,pt2], np.int32)
    pts_L1 = pts_L1.reshape((-1,1,2))


    pt5 = [0, up_limit]
    pt6 = [w, up_limit]
    pts_L3 = np.array([pt5,pt6], np.int32)
    pts_L3 = pts_L3.reshape((-1,1,2))
    pt7 = [0, down_limit]
    pt8 = [w, down_limit]
    pts_L4 = np.array([pt7,pt8], np.int32)
    pts_L4 = pts_L4.reshape((-1,1,2))

    # background subtractor
    fgbg = cv2.createBackgroundSubtractorMOG2()

    kernelOp = np.ones((3,3), np.uint8)
    kernelOp2 = np.ones((5,5), np.uint8)
    kernelCl = np.ones((11,11), np.uint8)

    #Variables
    font = cv2.FONT_HERSHEY_SIMPLEX
    vehicles = []
    max_p_age = 5
    pid = 1
    while True:

        frame = camera.get_frame()
        for i in vehicles:
            i.age_one()
        #################
        # PREPROCESSING #
        #################
        fgmask = fgbg.apply(frame)
        fgmask2 = fgbg.apply(frame)

        # Binary to remove shadow

        try:
            ret, imBin = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
            ret, imBin2 = cv2.threshold(fgmask2, 200, 255, cv2.THRESH_BINARY)
            #Opening (erode->dilate) to remove noise
            mask = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernelOp)
            mask2 = cv2.morphologyEx(imBin2, cv2.MORPH_OPEN, kernelOp)
            #Closing (dilate->erode) to join white region
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernelCl)
            mask2 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernelCl)
            #cv2.imshow('Image Threshold', cv2.resize(fgmask, (400, 300)))
            
        except:
            #If there is no more frames to show...
            print('EOF')
            print('UP:', cnt_up)
            #print('DOWN:', cnt_down)
            break
        

        #
        ## FIND CONTOUR 

        contours0, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for cnt in contours0:
     
            cv2.drawContours(frame, cnt, -1, (0,255,0), 3, 8)
            area = cv2.contourArea(cnt)
            
            if area > areaTH:
           

                #   TRACKING   

                M = cv2.moments(cnt)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                x,y,w,h = cv2.boundingRect(cnt)


                new = True
                for i in vehicles:
                    if abs(x-i.getX()) <= w and abs(y-i.getY()) <= h:
                        new = False
                        i.updateCoords(cx,cy)   # Update the coordinates in the object and reset age
                        if i.going_UP(line_down, line_up) == True:
                            roi = frame[y:y + h, x:x + w]
                            rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            height = h
                            width = w
                            kll = 2 * (height + width)
                          
                            if kll < 300:
                                UpMTR += 1
                            elif kll < 500:
                                UpLV += 1
                            elif kll > 500:
                                UpHV += 1

                            
                            cnt_up += 1
                            print("ID:", i.getId(), 'crossed going up at', time.strftime("%c"))
                        elif i.going_DOWN(line_down, line_up) == True:
                            roi = frame[y:y+h, x:x+w]
                            rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            height = y+h
                            width = x+w
                            luas = height*width
                            
                            if luas < 600000:
                                DownLV += 1
                            elif luas > 600000:
                                DownHV += 1

                            
                            cnt_down += 1
                       
                        break
                    if i.getState() == '1':
                        if i.getDir() == 'down' and i.getY() > down_limit:
                            i.setDone()
                        elif i.getDir() == 'up' and i.getY() < up_limit:
                            i.setDone()
                    if i.timedOut():
                        # Remove from the list person
                        index = vehicles.index(i)
                        vehicles.pop(index)
                        del i
                if new == True:
                    p = Vehicle.MyVehicle(pid,cx,cy, max_p_age)
                    vehicles.append(p)
                    pid += 1

                ##################
                ##   DRAWING    ##
                ##################
                cv2.circle(frame,(cx,cy),5, (0,0,255), -1)
                img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                

        for i in vehicles:
            """
            if len(i.getTracks()) >= 2:
                pts = np.array(i.getTracks(), np.int32)
                pts = pts.reshape((-1,1,2))
                frame = cv2.polylines(frame, [pts], False, i.getRGB())
            if i.getId() == 9:
                print str(i.getX()), ',', str(i.getY())
            """
            #cv2.putText(frame, str(i.getId()), (i.getX(),i.getY()),font,0.3,i.getRGB(),1,cv2.LINE_AA)

        ##   IMAGE   
        str_up = 'CNT: ' + str(cnt_up)
        MTR_up = 'Up Motor: ' + str(UpMTR)
        LV_up = 'Up Mobil: ' + str(UpLV)
        HV_up = 'Up Truck/Bus: ' + str(UpHV)
        str_down = 'CNT: ' + str(cnt_down)
        LV_down = 'Down Mobil: ' + str(DownLV)
        HV_down = 'Down Truck/Bus: ' + str(DownHV)
        frame = cv2.polylines(frame, [pts_L1], False, line_down_color, thickness=2)
        #frame = cv2.polylines(frame, [pts_L2], False, line_up_color, thickness=2)
        frame = cv2.polylines(frame, [pts_L3], False, (255,255,255), thickness=1)
        frame = cv2.polylines(frame, [pts_L4], False, (255,255,255), thickness=1)
        globals.lane3=str_up
        cv2.putText(frame, str_up, (10,75),font,3,(0, 0, 255),5,cv2.LINE_AA)
        cv2.putText(frame, str_up, (10,75),font,3,(0, 0, 255),5,cv2.LINE_AA)


        ret, jpeg = cv2.imencode('.jpg', frame)

        frame=jpeg.tobytes()

        print('COUNT:', cnt_up,3)

        print(type(frame),3)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen4(camera):

    globals.lane4=0

    cnt_up = 0
    cnt_down = 0
    UpMTR = 0
    UpLV = 0
    UpHV = 0
    DownLV = 0
    DownHV = 0
    w = 1280.0 #camera.set_frame.get(3)
    #print('Width', w)
    h = 720.0 #camera.set_frame.get(4)
    #print('Height', h)


    frameArea = h*w
    areaTH = frameArea/800


    # Input/Output Lines
    line_up = int(value*(h/5))
    line_down = int(1.7*(h/5))

    up_limit = int(1*(h/5))
    down_limit = int(4*(h/5))


    line_down_color = (255,0,0)

    pt1 = [0, line_down]

    pt2 = [w, line_down]
    pts_L1 = np.array([pt1,pt2], np.int32)
    pts_L1 = pts_L1.reshape((-1,1,2))


    pt5 = [0, up_limit]
    pt6 = [w, up_limit]
    pts_L3 = np.array([pt5,pt6], np.int32)
    pts_L3 = pts_L3.reshape((-1,1,2))
    pt7 = [0, down_limit]
    pt8 = [w, down_limit]
    pts_L4 = np.array([pt7,pt8], np.int32)
    pts_L4 = pts_L4.reshape((-1,1,2))

    # background subtractor
    fgbg = cv2.createBackgroundSubtractorMOG2()

    kernelOp = np.ones((3,3), np.uint8)
    kernelOp2 = np.ones((5,5), np.uint8)
    kernelCl = np.ones((11,11), np.uint8)

    #Variables
    font = cv2.FONT_HERSHEY_SIMPLEX
    vehicles = []
    max_p_age = 5
    pid = 1
    while True:

        frame = camera.get_frame()
        for i in vehicles:
            i.age_one()
        #################
        # PREPROCESSING #
        #################
        fgmask = fgbg.apply(frame)
        fgmask2 = fgbg.apply(frame)

        # Binary to remove shadow

        try:
            ret, imBin = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
            ret, imBin2 = cv2.threshold(fgmask2, 200, 255, cv2.THRESH_BINARY)
            #Opening (erode->dilate) to remove noise
            mask = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernelOp)
            mask2 = cv2.morphologyEx(imBin2, cv2.MORPH_OPEN, kernelOp)
            #Closing (dilate->erode) to join white region
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernelCl)
            mask2 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernelCl)
            #cv2.imshow('Image Threshold', cv2.resize(fgmask, (400, 300)))
            
        except:
            #If there is no more frames to show...
            print('EOF')
            print('down:', cnt_down)
            #print('DOWN:', cnt_down)
            break
        

        #
        ## FIND CONTOUR 

        contours0, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for cnt in contours0:
     
            cv2.drawContours(frame, cnt, -1, (0,255,0), 3, 8)
            area = cv2.contourArea(cnt)
            
            if area > areaTH:
           

                #   TRACKING   

                M = cv2.moments(cnt)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                x,y,w,h = cv2.boundingRect(cnt)


                new = True
                for i in vehicles:
                    if abs(x-i.getX()) <= w and abs(y-i.getY()) <= h:
                        new = False
                        i.updateCoords(cx,cy)   # Update the coordinates in the object and reset age
                        if i.going_UP(line_down, line_up) == True:
                            roi = frame[y:y + h, x:x + w]
                            rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            height = h
                            width = w
                            kll = 2 * (height + width)
                          
                            if kll < 300:
                                UpMTR += 1
                            elif kll < 500:
                                UpLV += 1
                            elif kll > 500:
                                UpHV += 1

                            
                            cnt_up += 1
                            print("ID:", i.getId(), 'crossed going up at', time.strftime("%c"))
                        elif i.going_DOWN(line_down, line_up) == True:
                            roi = frame[y:y+h, x:x+w]
                            rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            height = y+h
                            width = x+w
                            luas = height*width
                            
                            if luas < 600000:
                                DownLV += 1
                            elif luas > 600000:
                                DownHV += 1

                            
                            cnt_down += 1
                       
                        break
                    if i.getState() == '1':
                        if i.getDir() == 'down' and i.getY() > down_limit:
                            i.setDone()
                        elif i.getDir() == 'up' and i.getY() < up_limit:
                            i.setDone()
                    if i.timedOut():
                        # Remove from the list person
                        index = vehicles.index(i)
                        vehicles.pop(index)
                        del i
                if new == True:
                    p = Vehicle.MyVehicle(pid,cx,cy, max_p_age)
                    vehicles.append(p)
                    pid += 1

                ##################
                ##   DRAWING    ##
                ##################
                cv2.circle(frame,(cx,cy),5, (0,0,255), -1)
                img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                

        for i in vehicles:
            """
            if len(i.getTracks()) >= 2:
                pts = np.array(i.getTracks(), np.int32)
                pts = pts.reshape((-1,1,2))
                frame = cv2.polylines(frame, [pts], False, i.getRGB())
            if i.getId() == 9:
                print str(i.getX()), ',', str(i.getY())
            """
            #cv2.putText(frame, str(i.getId()), (i.getX(),i.getY()),font,0.3,i.getRGB(),1,cv2.LINE_AA)

        ##   IMAGE   
        str_up = 'CNT: ' + str(cnt_up)
        MTR_up = 'Up Motor: ' + str(UpMTR)
        LV_up = 'Up Mobil: ' + str(UpLV)
        HV_up = 'Up Truck/Bus: ' + str(UpHV)
        str_down = 'CNT: ' + str(cnt_down)
        LV_down = 'Down Mobil: ' + str(DownLV)
        HV_down = 'Down Truck/Bus: ' + str(DownHV)
        frame = cv2.polylines(frame, [pts_L1], False, line_down_color, thickness=2)
        #frame = cv2.polylines(frame, [pts_L2], False, line_up_color, thickness=2)
        frame = cv2.polylines(frame, [pts_L3], False, (255,255,255), thickness=1)
        frame = cv2.polylines(frame, [pts_L4], False, (255,255,255), thickness=1)
        globals.lane4=str_down
        cv2.putText(frame, str_down, (10,75),font,3,(0, 0, 255),5,cv2.LINE_AA)
        cv2.putText(frame, str_down, (10,75),font,3,(0, 0, 255),5,cv2.LINE_AA)


        ret, jpeg = cv2.imencode('.jpg', frame)

        frame=jpeg.tobytes()

        print('COUNT:', cnt_down,4)

        print(type(frame),4)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def gen5(camera):
    globals.stoper=0
    globals.drowsiness=''
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate - 50)

    def eye_aspect_ratio(eye):
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])
        C = dist.euclidean(eye[0], eye[3])

        #Compute eye aspect ratio
        ear = (A+B)/(2*C)

        return ear

    def mouth_aspect_ratio(mouth):
        A = dist.euclidean(mouth[2],mouth[10])
        B = dist.euclidean(mouth[3],mouth[9])
        C = dist.euclidean(mouth[4],mouth[8])

        return (A+B+C)/3


    ##ap = argparse.ArgumentParser()
    ##ap.add_argument("-p", "--shape-predictor", required=True,
    ##	help="path to facial landmark predictor")
    ##ap.add_argument("-v", "--video", type=str, default="",
    ##	help="path to input video file")
    ##args = vars(ap.parse_args())

    args={'shape_predictor': 'faceland.dat', 'video': ''}

    EYE_AR_THRESH = 0.23  #threshold for blink
    EYE_AR_CONSEC_FRAMES = 25 #consecutive considered true
    sleep_flag = 0
    yawn_flag = 0
    count_mouth = 0

    counter = 0
    total = 0
    total_yawn = 0

    print("[INFO] loading facial landmark predictor...")
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(args["shape_predictor"])

    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
    (mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]

    print("[INFO] starting video stream thread...")
    #vs = FileVideoStream(args["video"]).start()
    #fileStream = True
    #vs = VideoStream(src=0).start()
    time.sleep(1.0)
    start_time = time.time()
    elapsed_time = start_time

    while True:
        if globals.stoper>=1:
            break
        frame = camera.get_frame()
        frame = imutils.resize(frame, width = 640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        rects = detector(gray,0)    #dlib’s built-in face detector.

        for rect in rects:
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            mouth = shape[mStart: mEnd]
            mouthEAR = mouth_aspect_ratio(mouth)

            ear = (leftEAR + rightEAR) / 2.0
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            mouthHull = cv2.convexHull(mouth)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [mouthHull], -1, (0, 255, 0), 1)

            if mouthEAR > 30:
                count_mouth += 1
                if count_mouth >= 10:
                    if yawn_flag < 0:
                        print("You are yawning")
                        globals.drowsiness="You are yawning 	\ud83d\ude32"
                        yawn_flag = 1
                        total_yawn += 1
                        cv2.putText(frame, "Yawn Detected", (150, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                    else:
                        yawn_flag = 1
                else:
                    yawn_flag = -1
            else:
                count_mouth = 0
                yawn_flag = -1
                globals.drowsiness="You are working 	\ud83c\udf87"
            # else:
            #     print("You are working")
                
            if ear <  EYE_AR_THRESH:
                counter += 1

                if counter >= EYE_AR_CONSEC_FRAMES:
                    if sleep_flag < 0:
                        print("You are sleeping.")
                        globals.drowsiness="You are sleeping \ud83d\ude2a"
                        cv2.putText(frame, "Sleep Detected", (150, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                        sleep_flag = 1
                        total += 1
                else:
                    sleep_flag = -1
                # if total > 0:
                #     elapsed_time  = time.time() - start_time
                #     if elapsed_time > 10:
                #         print("You are sleeping dear")
                #         start_time = time.time()
                #     else:
                #         print("You are working")

            else:
                counter = 0
                sleep_flag = -1

    ##        cv2.putText(frame, "Total Sleeps: {}".format(total), (10, 30),
    ##            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    ##        cv2.putText(frame, "Total Yawns: {}".format(total_yawn), (10, 70),
    ##            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    ##        cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
    ##			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    ##        cv2.putText(frame, "MAR: {:.2f}".format(mouthEAR), (540, 30),
    ##			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            if total > 0:
                print("playing sound")
                engine.say("You are sleeping. I recommend you going for a walk or listen to music")
                engine.runAndWait()
                total = 0
                total_yawn=0

            elif total_yawn > 0:
                print("playing sound")
                engine.say("You are yawning. I recommend you going for a walk or listen to music")
                engine.runAndWait()
                total_yawn = 0
                total=0

        
        ret, jpeg = cv2.imencode('.jpg', frame)
        frame=jpeg.tobytes()

        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


#server = Flask(__name__)
#app = dash.Dash(__name__, server=server)



# external JS
external_scripts = [
    'https://www.google-analytics.com/analytics.js',
    "https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js",
    {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
        'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
        'crossorigin': 'anonymous'
    }
]

# external CSS stylesheets
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    'https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2/animate.min.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    },

    {
        'href': 'https://fonts.googleapis.com/css?family=Varela',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }

    
]



# Making app as an object of dash class. Invoking Dash function.

# Provide your name and content.

##meta_tags=[
##    {
##        'name': 'description',
##        'content': 'My description'
##    },
##    {
##        'http-equiv': 'X-UA-Compatible',
##        'content': 'IE=edge'
##    }
##]


app = dash.Dash(__name__,    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)

server = app.server
app.title = 'Fortify 	&#127950;&#65039;'
#app.config['suppress_callback_exceptions']=True
#app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})  # noqa: E501
#dcc._css_dist[0]['/assets'].append('stylesheet.css')
app.config['suppress_callback_exceptions']=True
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

PLOTLY_LOGO = "/"


@server.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@server.route('/video_feed1')
def video_feed1():
    return Response(gen1(VideoCamera1()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@server.route('/video_feed2')
def video_feed2():
    return Response(gen2(VideoCamera2()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@server.route('/video_feed3')
def video_feed3():
    return Response(gen3(VideoCamera3()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@server.route('/video_feed4')
def video_feed4():
    return Response(gen4(VideoCamera4()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@server.route('/video_feed5')
def video_feed5():
    return Response(gen5(VideoCamera5()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')








app.config['suppress_callback_exceptions']=True

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':

        # Default path is / . It will render Page_1_layout
        
        return page_0_layout

    elif pathname=='/congestion':

        return page_1_layout

    elif pathname=='/Emergency':

        return page_2_layout

    elif pathname=='/drowsiness':

        return page_3_layout

    elif pathname=='/pothole':

        return page_4_layout

    else:
        return []
    # You could also return a 404 "URL not found" page here



page_0_layout= html.Div(

            html.Div([

##
##                            html.Div([
##                            html.Div(
##
##                                    html.Img(src="assets/tr.gif", width="70%"), className="new_footer_area bg_color"
##                                
##                                ),],className="ten columns offset-by-two"),


                            html.Div([


                                    dbc.Navbar(
        [   
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="assets/s2.png", height="70px")),
                        dbc.Col(dbc.NavbarBrand("BC71", className="ml-4",style={"color":"#00ff00"})),
                        dbc.Col(dbc.NavLink("Congestion",href="/congestion", className="ml-4",style={"color":"#fff","font-size": "135%"})),
                        dbc.Col(dbc.NavLink("Emergency",href="/Emergency", className="ml-4",style={"color":"#fff","font-size": "135%"})),
                        dbc.Col(dbc.NavLink("Drowsiness",href="/drowsiness", className="ml-4",style={"color":"#fff","font-size": "135%"})),
                        dbc.Col(dbc.NavLink("Pothole",href="/pothole", className="ml-4",style={"color":"#fff","font-size": "135%"})),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/",
            ),

           
            
            dbc.NavbarToggler(id="navbar-toggler"),
           
        ],
        color="dark",      
        dark=True,
        ),
# <!--<script type="text/javascript" src="assets/jsbat.js"></script> -->      
                            dash_dangerously_set_inner_html.DangerouslySetInnerHTML(
                                '''

<div style="text-align:center; margin-top: 5%;"><img  class="animated infinite tada slow delay-2s" src="assets/c2.png" width="40%"/></div>
<script type="text/javascript" src="jsbat.js"></script>

  '''
                                ),



     dash_dangerously_set_inner_html.DangerouslySetInnerHTML(
                                '''


  
  <footer class="new_footer_area bg_color" style="margin-top: -4%">
              <div class="new_footer_top">
                  <div class="container">
                  </div>
                  <div class="footer_bg">
                      <div class="footer_bg_one"></div>
                      <div class="footer_bg_two"></div>
                  </div>
              </div>
              <div class="footer_bottom">
                  <div class="container">
                      <div class="row align-items-center">
                          <div class="col-lg-6 col-sm-7">
                              <p class="mb-0 f_400">© Connected Cars Inc.. 2019 All rights reserved.</p>
                          </div>
                          <div class="col-lg-6 col-sm-5 text-right">
                              <p>Made with 	&#x1F60D; by Team Fortify</p>
                          </div>
                      </div>
                  </div>
              </div>
          </footer>

                                '''
                                

                                )
                            ],className="twelve columns new_footer_area bg_color")
                
                ],className="new_footer_area bg_color")

    ,className="new_footer_area bg_color") #style={'height':'100%',"background":'url("https://digitalsynopsis.com/wp-content/uploads/2016/05/sci-fi-monochromatic-gif-animations-carl-burton-23.gif")'})


page_4_layout=html.Div(

         html.Div([

        html.Div([

        dbc.Navbar(
        [   
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="assets/s2.png", height="70px")),
                        dbc.Col(dbc.NavbarBrand("BC71", className="ml-4",style={"color":"#00ff00"})),
                        dbc.Col(dbc.NavLink("Congestion",href="/congestion", className="ml-4",style={"color":"#fff","font-size": "135%"})),
                         dbc.Col(dbc.NavLink("Emergency",href="/Emergency", className="ml-4",style={"color":"#fff","font-size": "135%"})),
                        dbc.Col(dbc.NavLink("Drowsiness",href="/drowsiness", className="ml-4",style={"color":"#fff","font-size": "135%"})),
                        dbc.Col(dbc.NavLink("Pothole",href="/pothole", className="ml-4",style={"color":"#fff","font-size": "135%"})),
      
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/",
            ),

            dbc.NavbarToggler(id="navbar-toggler"),
           
        ],
        color="dark",      
        dark=True,
        )

     ]),

        html.Div([
          dbc.Card([
                dbc.CardBody(
            [
                html.Div(html.Img(src="assets/gif/pothole.gif", width="100%")),
                html.H4("Poth Hole Identification 	\ud83d\udd73\ufe0f"),
                
            ],className='twelve columns'
        )],style={"border": "#ffaa00 1px solid"},className='seven columns offset-by-two')
          ]),
          
         

          ]),

         )



page_3_layout=html.Div(

         html.Div([

          dbc.Navbar(
        [   
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="assets/s2.png", height="70px")),
                        dbc.Col(dbc.NavbarBrand("BC71", className="ml-4",style={"color":"#00ff00"})),
                        dbc.Col(dbc.NavLink("Congestion",href="/congestion", className="ml-4",style={"color":"#fff","font-size": "135%"})),
                         dbc.Col(dbc.NavLink("Emergency",href="/Emergency", className="ml-4",style={"color":"#fff","font-size": "135%"})),
                        dbc.Col(dbc.NavLink("Drowsiness",href="/drowsiness", className="ml-4",style={"color":"#fff","font-size": "135%"})),
                        dbc.Col(dbc.NavLink("Pothole",href="/pothole", className="ml-4",style={"color":"#fff","font-size": "135%"})),

                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/",
            ),

           
            
            dbc.NavbarToggler(id="navbar-toggler"),
           
        ],
        color="dark",      
        dark=True,
        ),

                     
         html.Div([


              html.Div([dcc.Interval(
                    id='interval-componentsD',
                    interval=1*1000, # in milliseconds
                    n_intervals=0
                )]),


              
         dbc.Card(
    [
        dbc.CardBody(
            [

                html.Div([

                html.Div([    
                html.H4("Drowsiness Detection 	\ud83d\ude34", className="card-title"),
                html.Img(src="/video_feed5",style={"width":"90%"}),], className="seven columns"),


                html.Div([

                        html.Div([

                        html.Div(id="drowsiness-output"),

                        ], style={"margin-top": "20%"}),
                        
                    ],className="five columns")

            

                ],className='row'),

               
               
                
            ]
        ),
    ],style={"border": "#ffaa00 1px solid"}
)
], className="seven columns offset-by-two")


         ], className="twelve columns"),
    )

page_2_layout=html.Div(

      

          html.Div(
            [

  html.Div(
            [    html.Div([

        dbc.Navbar(
        [   
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="assets/s2.png", height="70px")),
                        dbc.Col(dbc.NavbarBrand("BC71", className="ml-4",style={"color":"#00ff00"})),
                        dbc.Col(dbc.NavLink("Congestion",href="/congestion", className="ml-4",style={"color":"#fff","font-size": "135%"})),
                         dbc.Col(dbc.NavLink("Emergency",href="/Emergency", className="ml-4",style={"color":"#fff","font-size": "135%"})),
                        dbc.Col(dbc.NavLink("Drowsiness",href="/drowsiness", className="ml-4",style={"color":"#fff","font-size": "135%"})),
                        dbc.Col(dbc.NavLink("Pothole",href="/pothole", className="ml-4",style={"color":"#fff","font-size": "135%"})),

                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/",
            ),

           
            
            dbc.NavbarToggler(id="navbar-toggler"),
           
        ],
        color="dark",      
        dark=True,
        )



     ]),
                ]),
    html.Div([
         html.Div([dcc.Interval(
                    id='interval-component',
                    interval=1*1000, # in milliseconds
                    n_intervals=0
                )]),

]),
 html.Div([html.Div([
          html.Div([
                         html.Div([html.H3('Select Emergency Vehicle 	\ud83d\udea8')]),     
                         html.Div([
                         html.Div([    
                         html.Div(dcc.Dropdown(id='input-box',options=[],value=None,placeholder='Select Survey'))],className="five columns"),
                         html.Div([
                         html.Button(id='my-button-1', n_clicks=0,children='Refresh',style={'display':'none','border': 'solid #0069D9 1px', 'color': 'black'})],className="four columns"),
                         ],className='row'),
                         ],className='twelve columns'),
                    ],style={'margin-top': '1.0%'}),
          ],className='ten columns offset-by-one'),

   html.Div([

               html.Div(id='output-1'),
        
              ],className='ten columns offset-by-one',style={'margin-top': '1.0%'}),
  html.Div([
                   
                ])

        ]  ))
        

page_1_layout = html.Div(
    

      

          html.Div(
            [

 

    html.Div([
         html.Div([dcc.Interval(
                    id='interval-components',
                    interval=1*1000, # in milliseconds
                    n_intervals=0
                )]),

]),

 html.Div([

        dbc.Navbar(
        [   
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="assets/s2.png", height="70px")),
                        dbc.Col(dbc.NavbarBrand("BC71", className="ml-4",style={"color":"#00ff00"})),
                        dbc.Col(dbc.NavLink("Congestion",href="/congestion", className="ml-4",style={"color":"#fff","font-size": "135%"})),
                         dbc.Col(dbc.NavLink("Emergency",href="/Emergency", className="ml-4",style={"color":"#fff","font-size": "135%"})),
                        dbc.Col(dbc.NavLink("Drowsiness",href="/drowsiness", className="ml-4",style={"color":"#fff","font-size": "135%"})),
                        dbc.Col(dbc.NavLink("Pothole",href="/pothole", className="ml-4",style={"color":"#fff","font-size": "135%"})),
      
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/",
            ),

            dbc.NavbarToggler(id="navbar-toggler"),
           
        ],
        color="dark",      
        dark=True,
        )

     ]),

    
 html.Div([html.Div([
          html.Div([
                         html.Div([html.H3('Congestion Control 	\ud83d\udea5')]),     
                    ],style={'margin-top': '1.0%',"margin-bottom": "-3%"}),
          ],className='ten columns offset-by-one'),

   html.Div([

               html.Div([

                    
            html.Div([


            html.Div([


            html.Div([


            html.Div([
            html.Div([

            html.Div([

            dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Lane 1 	\ud83d\udee3\ufe0f", className="card-title"),
                html.Img(src="/video_feed1",style={"width":"100%"}),
                
            ]
        ),
    ],style={"border": "#ffaa00 1px solid"}
    
),
           ],className="six columns"),

             html.Div([           dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Lane 2 	\ud83d\udee3\ufe0f", className="card-title"),
                html.Img(src="/video_feed2",style={"width":"100%"}),
                
            ]
        ),
    ],style={"border": "#ffaa00 1px solid"}
),],className="six columns"),
            

            ],className="row"),

            ],className="twelve columns"),


            html.Div([
            html.Div([

            html.Div([    
                      dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Lane 3 	\ud83d\udee3\ufe0f", className="card-title"),
                html.Img(src="/video_feed3",style={"width":"100%"}),
                
            ]
        ),
    ],style={"border": "#ffaa00 1px solid"}

),],className="six columns"),

            html.Div([
                      dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Lane 4 	\ud83d\udee3\ufe0f", className="card-title"),
                html.Img(src="/video_feed4",style={"width":"100%"}),
                
            ]
        ),
    ],style={"border": "#ffaa00 1px solid"}
),],className="six columns"),


            ],className="row"),

            ],className="twelve columns"),
        ]),
            

            ],className="twelve columns"),
            ],className='row'),



            html.Div([
    
             html.Div([

                    html.Div(id='outGraph',style={"margin-bottom":"5%"}),


                 ],className='twelve columns'),

             

             ],className='row'),
            




                   ]),
        
              ],className='ten columns offset-by-one',style={'margin-top': '1.0%'}),])]))




        

@app.callback(
        dash.dependencies.Output('output-1', 'children'),
        [dash.dependencies.Input('input-box', 'value')])
def update_image_src(value):
        
    if value is not None:

        print(value)

        to=value[0].split("\n")
        toLan=float(to[0])
        toLon=float(to[1])


        froms=value[1].split("\n")
        fromsLan=float(froms[0])
        fromsLon=float(froms[1])

        print(toLan,toLon,fromsLan,fromsLon)


        #geolocator = Nominatim(user_agent="specify_your_app_name_here")
        #location = geolocator.reverse("52.509669, 13.376294")
        #flocation = geolocator.reverse(str(fromsLan)+', '+str(fromsLon))
        #tlocation=  geolocator.reverse(str(toLan)+', '+str(toLon))


        
        return [



            html.Div([

            html.Div([    
            html.Div([


                    html.Div([

                    html.Div([    



                    dbc.Card(
    [
        dbc.CardBody(
            [
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML(str(maps.mapsUrlGenerator(str(fromsLan)+','+str(fromsLon),str(toLan)+','+str(toLon))))
])],style={"border": "#ffaa00 1px solid"}),
                    ],className="eleven columns"),


                    ],className="row")

                    

                ]),

            ],className="four columns"),

            html.Div([

             dbc.Card(
    [
        dbc.CardImg(src="/video_feed",style={"width":"90%"}),
        dbc.CardBody(
            [
                
            html.H4("Live Feed of CCTV 	\ud83d\udcf9", className="card-title"),

            ])],style={"border": "#ffaa00 1px solid"}),

            ],className="eight columns"),
            ],className='row'),



            html.Div([
             html.Div([


                 html.P("some random text is written",style={"display":'none'})


                        ],className='six columns'),


             html.Div([

                    html.Div(id='output-plate',style={"margin-bottom":"5%"}),


                 ],className='twelve columns'),

             

             ],className='row'),
            
            ]


        
   

@app.callback(
        dash.dependencies.Output('output-plate', 'children'),
        [dash.dependencies.Input('interval-component', 'n_intervals')]
    )
def update_output(value):
    if gl.number=='':
        return ''
    else:


            #print(gl.plate)

        for i in gl.number:
            if i in gl.plate and i not in gl.stack:
                user,mob=gl.plate[i].split(" ")
                gl.stack.append(i)
                try:
                        send_sms()
                except:
                    return [

                        html.Div([
                        html.H6('       \u2b50 Detected Number \ud83d\udd22 Plate '+str(", ".join(gl.number)))
                        ],style={"text-align":"center"})
                        ]

                return [

                    html.Div([
                    html.Div(html.P('	\ud83d\udce7 Message has been delivered to '+user)),html.H6('\u2b50 Detected Number \ud83d\udd22 Plate'+str(", ".join(gl.number)))
                    ],style={"text-align":"center"}),


                    ]
        return [


            html.Div([
            html.H6('	\u2b50 Detected Number 	\ud83d\udd22 Plate '+str(", ".join(gl.number)))

            ],style={"text-align":"center"})
            ]









@app.callback(
        dash.dependencies.Output('input-box', 'options'),
        [dash.dependencies.Input('my-button-1', 'n_clicks')]
    )
def update_output(n):

    gl.stack=[]
    gl.c=5000
    gl.number=''
    gl.plate=''


    with urllib.request.urlopen("https://ambulance-da553.firebaseio.com/user.json") as url:
        data = json.loads(url.read().decode())
        

    

    trying=[]

    blank_d={}


    with urllib.request.urlopen("https://ambulance-da553.firebaseio.com/data.json") as url:
        datas = json.loads(url.read().decode())


    gl.plate=datas        



    try:
        for i in data['Users']:
            usa=[]
            for j,k in data['Users'][i].items():
                usa.append(k)
                
                
            trying.append( {'label':i, 'value': usa})
    except:
        return []
                

    return trying







@app.callback(
        dash.dependencies.Output('drowsiness-output', 'children'),
        [dash.dependencies.Input('interval-componentsD', 'n_intervals')]
    )
def update_output(value):

    if globals.drowsiness!='':

        return [html.H5(globals.drowsiness)]
    else:
        return []
     




@app.callback(
        dash.dependencies.Output('outGraph', 'children'),
        [dash.dependencies.Input('interval-components', 'n_intervals')]
    )
def update_output(value):

        if globals.excepts==1:

            
            y=[int(globals.lane1.split(": ")[1]),int(globals.lane2.split(": ")[1]),int(globals.lane3.split(": ")[1]),int(globals.lane4.split(": ")[1])]
            mylist=y
            sl=sum(mylist)
            lst=[]

            def myround(x, base=4):
                return  round(x*base)/base
            for a in range(4):
                j=mylist[a]*4/sl
                j=myround(j)
                lst.append(j)
            #print(lst[a])

            
            x=['Lane1','Lane2','Lane3','Lane4']
            fig=dcc.Graph(
            id='example-graph-1',
            figure={
            'data': [
            {'x': x, 'y': y, 'type': 'bar', 'name': 'Density'},
            ],
            'layout': {
            'title': 'Vehicle Count v/s Lane',
             'xaxis':{
                    'title':'Lane'
                },
                'yaxis':{
                     'title':'No. of Vehicles'
                }
            }
            }
            )

            y=lst
            x=['Lane1','Lane2','Lane3','Lane4']
            figs=dcc.Graph(
            id='example-graph-2',
            figure={
            'data': [
            {'x': x, 'y': y, 'type': 'bar', 'name': 'Density1'},
            ],
            'layout': {
            'title': 'Time Alloted v/s Lane',
             'xaxis':{
                    'title':'Lane'
                },
                'yaxis':{
                     'title':'Time in Minutes'
                }
            
            
            }
            }
            )



            return [

            html.Div([
            html.Div([
            html.Div([
            html.Div([
            
            dbc.Card([
            dbc.CardBody(
            [
                fig
        
                
            ],className='twelve columns'
        )],style={"border": "#ffaa00 1px solid"}, className='twelve columns'),
            
            ],className='six columns'),


            html.Div([

                
            dbc.Card([
             dbc.CardBody(
            [
                figs
        
                
            ],className='twelve columns'
        )
             ],style={"border": "#ffaa00 1px solid"}, className='twelve columns'),

            
            ],className='six columns'),],className='twelve  columns'),
            ],className='row')],className='twelve columns'),


            ]

            
            

        else:

            y=[int(globals.lane1.split(": ")[1]),int(globals.lane2.split(": ")[1]),int(globals.lane3.split(": ")[1]),int(globals.lane4.split(": ")[1])]
            x=['Lane1','Lane2','Lane3','Lane4']
            fig=[ dcc.Graph(
            id='example-graph-1',
            figure={
                'data': [
                    {'x': x, 'y': y, 'type': 'bar', 'name': 'Density'},
                ],
                'layout': {
                    'title': 'Car Count v/s Lane'
                }
            }
        )]
            return   [

                dbc.Card([
                dbc.CardBody(
            [
                html.Div(fig)
        
                
            ],className='twelve columns'
        )],style={"border": "#ffaa00 1px solid"},className='twelve columns')]




wb.open('http://127.0.0.1:8050/')
if __name__ == '__main__':
    app.run_server(debug=False,threaded=True,use_reloader=False)

    
        

