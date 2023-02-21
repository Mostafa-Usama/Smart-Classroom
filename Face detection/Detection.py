import cv2
import numpy as np
# import serial 
from tkinter import * 
from Interface import draw,s
import _thread

MAX_NUMBER = 3

capture = cv2.VideoCapture('img5.jpg')
#s = serial.Serial('COM3',9600)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #pretrained model to detect faces
thread = _thread.start_new_thread(lambda:draw(),())


while True:
    

    capture = cv2.VideoCapture('img5.jpg')
    isTrue, f = capture.read()
    #width = int(capture.get(3))
    #height = int(capture.get(4))



    #img = cv2.imread('img5.jpg') #read image
    font = cv2.FONT_HERSHEY_SIMPLEX # font used to display text
    #img =cv2.resize(img,(0,0),fx=0.5,fy=.5) # resize the image to half
    gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY) # convert image to grey scale (algorithm only works for grey scale images)
    heghit, width = gray.shape  # get width and height of the image after resizing
    faces = face_cascade.detectMultiScale(gray,1.18,5)
    fe = str(len(faces)) 
    # detect faces (source image, scale factor, quality and performance). returns ((top left x, top left y), width , height) 
    left = 0
    right = 0
    #cv2.line(img, (width//2, 0), (width//2, heghit), (0, 255, 0), 2)

    for (x, y, w, h) in faces:
        #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3) #draw rectangle on the faces (image,top left point,bottom right point, color, thickness)
        if (x+(x+w))/2 >= width/2:
            right +=1
        else:
            left +=1

        #cv2.putText(img,"Count of faces:"+str(len(faces)),(width//3,heghit//6),font,.9,(0,0,255),3) 
        #text (image, string, bottom left point, font, font size, color, thickness)
    #cv2.imshow('img',img)    # show image 

    print(f'Left: {left}', f"right: {right}")

    if left >= 3 and right >= 3:
        fe = '1'
        s.write(fe.encode('utf-8'))
    elif left >= 3 and right < 3:
        fe = '2'
        s.write(fe.encode('utf-8'))
    elif left < 3 and right >= 3:
        fe = '3'
        s.write(fe.encode('utf-8'))
    else:
        fe = '4'
        s.write(fe.encode('utf-8'))
    print(fe)
    
    #cv2.waitKey(0) # wait for button or X 
    #cv2.destroyAllWindows()


