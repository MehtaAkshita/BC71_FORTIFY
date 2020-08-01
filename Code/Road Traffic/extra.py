import cv2
import numpy as np
import Vehicle
import time

value=1.8
videos=['./Downloads/1t.MP4','./Downloads/2t.MP4','./Downloads/3.MP4','./Downloads/4.MP4']


video=int(input())
cnt_up = 0
cnt_down = 0
UpMTR = 0
UpLV = 0
UpHV = 0
DownLV = 0
DownHV = 0

cap = cv2.VideoCapture(videos[video])


w = cap.get(3)
print('Width', w)
h = cap.get(4)
print('Height', h)


frameArea = h*w
areaTH = frameArea/800

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


fgbg = cv2.createBackgroundSubtractorMOG2()

kernelOp = np.ones((3,3), np.uint8)
kernelOp2 = np.ones((5,5), np.uint8)
kernelCl = np.ones((11,11), np.uint8)

#Variables
font = cv2.FONT_HERSHEY_SIMPLEX
vehicles = []
max_p_age = 5
pid = 1

while(cap.isOpened()):
    #read a frame
    ret, frame = cap.read()
    for i in vehicles:
        i.age_one()    # age every person on frame

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
        
        print('DOWN:', cnt_down)
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
                        print("ID:", i.getId(), 'crossed going down at', time.strftime("%c"))
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
        
        cv2.putText(frame, str(i.getId()), (i.getX(),i.getY()),font,0.3,i.getRGB(),1,cv2.LINE_AA)

    ##   IMAGE   
    str_up = 'cnt: ' + str(cnt_up)
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
    
    cv2.putText(frame, str_down, (10,90),font,2,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame, str_down, (10,90),font,2,(255,0,0),1,cv2.LINE_AA)
   
    cv2.imshow('Frame', cv2.resize(frame, (400, 300)))
    print('COUNT:', cnt_down)
    
  
    #Abort and exit with 'Q' or ESC
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break
    
    
    
print('COUNT:', cnt_down)
s1=str(cnt_down)
file1 = open("Density_Count.txt","a")
file1.write(s1+",") 
file1.close()

f1=open("Density_Count.txt","r+")
ou=f1.read()
l1=ou.split(",")
del l1[-1]
if(len(l1)==4):
    f1.truncate(0)
cap.release()
cv2.destroyAllWindows()



