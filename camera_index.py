import cv2

cams_test = int(input("Enter the number of cameras you want to test: "))
for i in range(0, cams_test):
    cap = cv2.VideoCapture(i)
    test, frame = cap.read()
    print("i : "+str(i)+" /// result: "+str(test))