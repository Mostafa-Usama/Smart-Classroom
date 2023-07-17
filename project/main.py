import cv2
from tkinter import * 
from Interface import lst,s,getfan,getMode,getMax,getTemp, Application_Interface
import _thread
from Graph_Head import FROZEN_GRAPH_HEAD
import time

top_left = 0
top_right = 0
bottom_left = 0
bottom_right = 0

# TEMPERATURE = 14
Max_Number = getMax()

app = Application_Interface()
thread = _thread.start_new_thread(app.run,())






tDetector = FROZEN_GRAPH_HEAD()
#cap = cv2.VideoCapture(source)

while app.opened:
    
    if app.logged:
        auto = getMode()   
        while auto and app.opened:
            temp=getTemp()
            Max_Number = getMax()
            auto = getMode()  
            path="Test/test.jpg"
            boxes = cv2.imread(path)
            #ret, image = cap.read()
            # if ret == 0:
            #     break

            im_height, im_width, im_channel = boxes.shape
            

            image,top_left, top_right, bottom_left, bottom_right = tDetector.run(boxes,path,im_width,im_height)
            cv2.imshow("HEAD DETECTION USING FROZEN GRAPH", image)

            k = cv2.waitKey(1) & 0xff
            if k == ord('q') or k == 27:
                break

            

                

                #cv2.putText(img,"Count of faces:"+str(len(faces)),(width//3,heghit//6),font,.9,(0,0,255),3) 
                #text (image, string, bottom left point, font, font size, color, thickness)
                #cv2.imshow('img',img)    # show image 

            print(f'Top Left: {top_left}', f" Top right: {top_right}",f"Bottom left: {bottom_left}",f"Bottom Right: {bottom_left}")
            total=100
            if app.ch.get()==0:
                total+=top_left+top_right+bottom_left+bottom_left
            
                
                if total>105 and top_left>=1:
                    fe = 't'
                    s.write(fe.encode('utf-8'))
                elif total>70 and top_right+top_left>=1:
                    fe = 's'
                    s.write(fe.encode('utf-8'))
                elif total>35 and bottom_left+top_right+top_left>=1:
                    fe = 'r'
                    s.write(fe.encode('utf-8'))
                elif total>=1:
                    fe = 'q'
                    s.write(fe.encode('utf-8'))


            elif app.ch.get()==1:

                if top_left >= Max_Number:
                    if getfan():#and 0 >= Max_Number: 
                        fe = '1'
                        lst[0]=False
                        lst[1]=False
                        s.write(fe.encode('utf-8'))
                    else:
                        fe = 'w'
                        lst[0]=False
                        lst[1]=True
                        s.write(fe.encode('utf-8'))
                else:
                    lst[0]=True
                    lst[1]=True
                    fe = '5'
                    s.write(fe.encode('utf-8'))


                if top_right >= Max_Number: #and 0 < Max_Number:
                    if getfan():#and 0 >= Max_Number:
                        lst[2]=False
                        lst[3]=False
                        fe = '2'
                        s.write(fe.encode('utf-8'))
                    else:
                        lst[2]=False
                        lst[3]=True
                        fe = 'x'
                        s.write(fe.encode('utf-8'))

                else:
                    lst[2]=True
                    lst[3]=True
                    fe = '6'
                    s.write(fe.encode('utf-8'))


                if  bottom_left >= Max_Number: #and 0 >= Max_Number:
                    if getfan():#and 0 >= Max_Number:
                        lst[4]=False
                        lst[5]=False
                        fe = '3'
                        s.write(fe.encode('utf-8'))
                    else:
                        lst[4]=False
                        lst[5]=True
                        fe = 'y'
                        s.write(fe.encode('utf-8'))

                else:
                    lst[4]=True
                    lst[5]=True
                    fe = '7'
                    s.write(fe.encode('utf-8'))

                if bottom_right >= Max_Number:
                    if getfan():#and 0 >= Max_Number:
                        lst[6]=False
                        lst[7]=False
                        fe = '4'
                        s.write(fe.encode('utf-8'))
                    else:
                        lst[6]=False
                        lst[7]=True
                        fe = 'z'
                        s.write(fe.encode('utf-8'))
                else:
                    lst[6]=True
                    lst[7]=True
                    fe = '8'
                    s.write(fe.encode('utf-8'))

                print(fe)

                for i in range(100):
                    if not app.opened:
                        break
                    time.sleep(0.01)
                #cap.release()

                #cv2.destroyAllWindows()
                    
        #cv2.waitKey(0) # wait for button or X 
        #cv2.destroyAllWindows()


