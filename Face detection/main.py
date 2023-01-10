import cv2
import numpy as np
import serial 

#capture = cv2.VideoCapture('1.jpg')
#
#
# def rescale(frame, scale=.75):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
#     dimensions = (width, height)
#
#     return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
#
#
# # show image
#
# blank = np.zeros((500, 500,3), dtype='uint8')
# blank[100:200, 300:500] = 255, 0, 0
#
# cv2.rectangle(blank, (0, 0), (250, 250), (0, 0, 255), thickness=-1)
# cv2.circle(blank,(250,250),50,(0,255,0),-1)
# #cv2.imshow("blank", blank)
# cat = "E:\\Sezor\\Photos\\FB_IMG_1489270880141.jpg"
# ggx = "E:\\Sezor\\Videos\\GUILTY GEAR XX ΛCORE PLUS R 2022-01-25 01-40-26.mp4"
# img = cv2.imread("E:\\Sezor\\Photos\\FB_IMG_1489270880141.jpg")
#
# img_resize = rescale(img)
# #cv2.imshow("cat", img_resize)
# #cv2.waitKey(0)
# # video

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #pretrained model to detect faces
s = serial.Serial('COM3',9600)

#while True:
    #isTrue, f = capture.read()
    #width = int(capture.get(3))
    #height = int(capture.get(4))



img = cv2.imread('4.jpg') #read image
font = cv2.FONT_HERSHEY_SIMPLEX # font used to display text
#img =cv2.resize(img,(0,0),fx=0.5,fy=.5) # resize the image to half
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image to grey scale (algorithm only works for grey scale images)
heghit, width = gray.shape  # get width and height of the image after resizing
faces = face_cascade.detectMultiScale(gray,1.18,5)
fe = str(len(faces)) 
# detect faces (source image, scale factor, quality and performance). returns ((top left x, top left y), width , height) 
left = 0
right = 0
cv2.line(img, (width//2, 0), (width//2, heghit), (0, 255, 0), 2)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3) #draw rectangle on the faces (image,top left point,bottom right point, color, thickness)
    if (x+(x+w))/2 >= width/2:
        right +=1
    else:
        left +=1

    cv2.putText(img,"Count of faces:"+str(len(faces)),(width//3,heghit//6),font,1.5,(0,0,255),3) 
    #text (image, string, bottom left point, font, font size, color, thickness)
cv2.imshow('img',img)    # show image 

print(f'Left: {left}', f"right: {right}")

if left >= 4 and right >= 4:
    fe = '1'
    s.write(fe.encode('utf-8'))
elif left >= 4 and right < 4:
    fe = '2'
    s.write(fe.encode('utf-8'))
elif left < 4 and right >= 4:
    fe = '3'
    s.write(fe.encode('utf-8'))
else:
    fe = '4'
    s.write(fe.encode('utf-8'))
print(fe)
    
cv2.waitKey(0) # wait for button or X 
cv2.destroyAllWindows()



    # Draw shapes
    # cv2.line(f, (0, 0), (width, height), (0, 255, 0), 10)
    # cv2.line(f, (0, height), (width, 0), (0, 255, 0), 10)
    # cv2.rectangle(f,(100,100),(200,200),(128,128,128),5)
    # cv2.circle(f,(width//2,height//2),50,(0,0,255),5)
    # cv2.putText(f,"Sfsf",(100,height-10),font,4,(0,200,100),5,cv2.LINE_AA)

    # 4 screens
    # blank = numpy.zeros(f.shape, numpy.uint8)
    # smallerF = cv2.resize(f, (0, 0), fx=0.5, fy=0.5)
    # blank[:height//2, :width//2] = cv2.rotate(smallerF, cv2.cv2.ROTATE_180)
    # blank[height//2:height, :width//2] = smallerF
    # blank[:height//2, width//2:width] = cv2.rotate(smallerF, cv2.cv2.ROTATE_180)
    # blank[height//2:height, width//2:width] = smallerF

    # detect yellow
    # hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
    # yellow_lower = np.array([15, 150, 20])
    # yellow_upper = np.array([35, 255, 255])
    # mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    # result = cv2.bitwise_and(f, f, mask=mask)


