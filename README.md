## Face-Recognition-in-Live-Video-using-OpenCV-Project

Steps to run 
1. Edit the camera device number in camera.txt. You can find the camera index number by running camera_index.py
2. Now run video read.py to check that your webcam is running or not.
3. Run face_detection.py to check that whether camera is able to capture your face or not, with the help of haar cascase classifier
4. Now, run face_data.py --> this will open up the camera and extract your face from video frames multiple time. Test and store faces of multiple people.
5. At last, run face_recognition.py --> this will detect your face from the dataset made and form a bounding box with you name writtern around your face.
