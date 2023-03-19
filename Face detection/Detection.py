import cv2
from tkinter import * 
from Interface import s,getMode,getMax,getTemp, Application_Interface
import _thread
from Graph_Head import FROZEN_GRAPH_HEAD
import time

top_left = 0
top_right = 0
bottom_left = 0
bottom_right = 0

TEMPERATURE = 14
Max_Number = getMax()

app = Application_Interface()
thread = _thread.start_new_thread(app.run,())


PATH_TO_CKPT_HEAD = 'models/HEAD_DETECTION_300x300_ssd_mobilenetv2.pb'


source = 'test.mp4'


tDetector = FROZEN_GRAPH_HEAD(PATH_TO_CKPT_HEAD)
#cap = cv2.VideoCapture(source)

while app.opened:
    
    if app.logged:
        auto = getMode()   
        while auto and app.opened:
            temp=getTemp()
            Max_Number = getMax()
            auto = getMode()  
            image = cv2.imread("Test/6.jpg")
            #ret, image = cap.read()
            # if ret == 0:
            #     break

            im_height, im_width, im_channel = image.shape
            image = cv2.flip(image, 1)

            boxes, scores, top_left, top_right, bottom_left, bottom_right = tDetector.run(image,im_width,im_height)
            cv2.imshow("HEAD DETECTION USING FROZEN GRAPH", image)

            k = cv2.waitKey(1) & 0xff
            if k == ord('q') or k == 27:
                break

            

                

                    #cv2.putText(img,"Count of faces:"+str(len(faces)),(width//3,heghit//6),font,.9,(0,0,255),3) 
                    #text (image, string, bottom left point, font, font size, color, thickness)
                #cv2.imshow('img',img)    # show image 

            print(f'Top Left: {top_left}', f" Top right: {top_right}",f"Bottom left: {bottom_left}",f"Bottom Right: {bottom_right}")

            if top_left >= Max_Number:
                if temp<= TEMPERATURE:#and 0 >= Max_Number:
                    fe = '1'
                    s.write(fe.encode('utf-8'))
                else:
                    fe = 'w'
                    s.write(fe.encode('utf-8'))
            else:
                fe = '5'
                s.write(fe.encode('utf-8'))


            if top_right >= Max_Number: #and 0 < Max_Number:
                if temp<= TEMPERATURE:#and 0 >= Max_Number:
                    fe = '2'
                    s.write(fe.encode('utf-8'))
                else:
                    fe = 'x'
                    s.write(fe.encode('utf-8'))

            else:
                fe = '6'
                s.write(fe.encode('utf-8'))


            if  bottom_left >= Max_Number: #and 0 >= Max_Number:
                if temp <= TEMPERATURE:#and 0 >= Max_Number:
                    fe = '3'
                    s.write(fe.encode('utf-8'))
                else:
                    fe = 'y'
                    s.write(fe.encode('utf-8'))

            else:
                fe = '7'
                s.write(fe.encode('utf-8'))

            if bottom_right >= Max_Number:
                if temp<= TEMPERATURE:#and 0 >= Max_Number:
                    fe = '4'
                    s.write(fe.encode('utf-8'))
                else:
                    fe = 'z'
                    s.write(fe.encode('utf-8'))
            else:
                fe = '8'
                s.write(fe.encode('utf-8'))

            print(fe)

            for i in range(100):
                if not app.opened:
                    break
                #time.sleep(0.1)
            #cap.release()

            #cv2.destroyAllWindows()
                    
        #cv2.waitKey(0) # wait for button or X 
        #cv2.destroyAllWindows()


