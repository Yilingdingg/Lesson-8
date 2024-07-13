import cv2
import numpy

video1=cv2.VideoCapture("green.mp4")
print(video1.read())
for video in range(60):
    ret,bg=video1.read()

while video1.isOpened():
    ret,img=video1.read()
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_green=numpy.array([104,153,70])
    upper_green=numpy.array([30,30,0])
    #convert to range
    mask1=cv2.inRange(hsv,lower_green, upper_green)
    lower_green=numpy.array([50,100,100])
    upper_green=numpy.array([70,255,255])
    #convert to range
    mask2=cv2.inRange(hsv,lower_green, upper_green)
    mask1=mask1+mask2
    #unsigned integer
    mask1=cv2.morphologyEx(mask1, cv2.MORPH_OPEN,numpy.ones((3,3),numpy.uint8),iterations=2)
    mask1=cv2.dilate(mask1,numpy.ones((3,3),numpy.uint8), iterations=1)
    mask2=cv2.bitwise_not(mask1)
    res1=cv2.bitwise_and(bg,bg,mask=mask1)
    res2=cv2.bitwise_and(img,img, mask=mask2)
    final_output=cv2.addWeighted(res1,1,res2,1, 0)
    cv2.imshow("final",final_output)
    k=cv2.waitKey(10)
    if k==27:
        break

