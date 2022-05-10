# -*- coding: utf-8 -*-
"""
Created on 
"""

import cv2

with open('camera.txt') as f:
    cam_input = int(f.read())

cap=cv2.VideoCapture(cam_input)  #Set the camera to use

while(cap.isOpened()):
    while True:
        ret,frame = cap.read()
        
        if ret == False:
            continue
        
        cv2.imshow("Video Frame",frame)
    
        key_pressed = cv2.waitKey(1) & 0xFF
        
        if key_pressed == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
else:
    print("Alert! Camera disconnected")
    

    
