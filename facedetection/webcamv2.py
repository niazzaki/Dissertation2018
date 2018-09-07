import cv2
import sys
#import urllib3
from picamera.array import PiRGBArray
from picamera import PiCamera
import time 
import platform
import os
import requests

#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

flag=0
if flag==0:
	print(os.getpid())
	flag=1

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

#video_capture = cv2.VideoCapture("Obama.mov")

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	f=frame.array
	
	gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		#flags=cv2.cv.CV_HAAR_SCALE_IMAGE
		flags= cv2.CASCADE_SCALE_IMAGE
		)	
		
		
	# Draw a rectangle around the faces
	
	for (x, y, w, h) in faces:
		cv2.rectangle(f, (x, y), (x+w, y+h), (0, 255, 0), 2)
			
		# Display the resulting frame
		
	cv2.imshow('Video', f)
	
	
	#send warning to server 
	
	if len(faces)!=0:
		print(True)
		url='http://ec2-54-149-229-195.us-west-2.compute.amazonaws.com:8081'
		query={'Warning!':'Face detected! Check for security'}
		res=requests.post(url,data=query)
		print(res.text)
		time.sleep(10)
		
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	# When everything is done, release the capture
	
	rawCapture.truncate(0)
	
