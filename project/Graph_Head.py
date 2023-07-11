from ultralytics import YOLO
import numpy as np
import cv2

model = YOLO("models\\best.pt" , 'v8')
class FROZEN_GRAPH_HEAD():

        

    def count_students(self, output,image, im_width, im_height):
        
        tr = 0
        tl = 0
        br = 0
        bl = 0 

        for head in output:
            
            #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3) #draw rectangle on the faces (image,top left point,bottom right point, color, thickness)
            
            # ymin, xmin, ymax, xmax = box
            left = int((head[0]))
            top = int((head[1]))
            right = int((head[2]))
            bottom = int((head[3]))

            

            
            width = right - left
            height = bottom - top
            

            mid_width = (left + (left + width))/2
            mid_height = (bottom + (bottom - height))/ 2

            if mid_width <= im_width/2 and mid_height <= im_height /2:
                tl +=1
            elif  mid_width >= im_width/2 and mid_height <= im_height /2:
                tr +=1
            
            elif mid_width <= im_width/2 and mid_height >= im_height /2:
                bl +=1
            elif mid_width >= im_width/2 and mid_height >= im_height /2:
                br +=1

            cv2.rectangle(image, (left+3, top+7), (right-3, bottom-8), (255, 0, 0), 2, 8)
            cv2.line(image, (im_width//2, 0), (im_width//2, im_height), (0, 255, 0), 2)                
            cv2.line(image, (0, im_height//2), (im_width, im_height//2), (0, 255, 0), 2)                

        return image, tl, tr, bl, br


    def run(self,image, path, im_width, im_height):
        
        output = model.predict(source=path,conf=0.25,save=False)
        output=output[0].numpy()
        img, tl, tr, bl, br=self.count_students(output.boxes.data,image,im_width, im_height)
        return img, tl, tr, bl, br