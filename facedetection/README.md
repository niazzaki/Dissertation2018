# Webcame face-detection
#scripted adapted from https://realpython.com/blog/python/face-recognition-with-python/

to run the code:

1) burn the raspberry Pi Image from the Image folder using win32diskmanager software on windows. 
the image contains all required software and can easily run the script

2) login to the raspberry machine with user pi and password test

3) open terminal and type 
   >>> source /.profile 

4) next type this command on the terminal to enter virtual environment

>>> workon cv

5) once you are in the virtual environment, run the script webcam.py passing to it the video path. it will detect faces
in the video and will draw rectangles around them


6) if you run the script on python3, use webcam_cv3







