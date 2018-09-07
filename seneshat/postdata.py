import requests
import os
import json
from sense_hat	import SenseHat
from pushsafer import init, Client
import urllib3
import time 
import platform



flag=0
pid=0
if flag==0:
	pid=os.getpid()
	print(pid)
	flag=1
	
 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

sense=SenseHat()
	
start_time=time.asctime(time.localtime(time.time()))

st=1

def get_weather():
	
	weather_dic={}
	metrics=[]
	temptotal=0
	humtotal=0
	pretotal=0

	i=0
	while i<10:		
		temperature=round(sense.get_temperature(),1)
		humidity=round(sense.get_humidity(),1)
		pressure=round(sense.get_pressure(),1)
		metrics=temperature,humidity,pressure
		weather_dic[i]=metrics
	
		temptotal+=temperature
		humtotal+=humidity
		pretotal+=pressure
	
		i+=1
		time.sleep(1)

	url='http://ec2-54-149-229-195.us-west-2.compute.amazonaws.com:8080'

	avtemp=round(temptotal/60,1)
	avhumidity=round(humtotal/60,1)
	avpressure=round(pretotal/60,1)

	query={'Average temperature ':avtemp,'average humidity ':avhumidity,'Average Pressure ' : avpressure}
	
	res=requests.post(url,data=query)
	
	print(res.text)
	
	print (os.getpid())
	print (platform.python_version())
	#print (help())
	get_weather()

if st<10:	
	get_weather()
	st+=1

