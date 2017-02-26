from picamera import PiCamera
from time import sleep
from time import time
from time import localtime
from time import strftime

def shutdownpi():
    command = "/usr/bin/sudo /sbin/shutdown -h 1"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output
sleep(60)
if localtime()[3] == 12:
	with PiCamera() as camera:
		camera.resolution = (2592,1944)
		camera.framerate = 15
		sleep(5)
		camera.capture('/home/pi/TimeLapseHerve/image' + strftime('%Y-%m-%d_%H%M%S') + '.jpg')
else:
	with PiCamera() as camera:
		camera.resolution = (2592,1944)
		camera.framerate = 15
		sleep(5)
		camera.capture('/home/pi/TimeLapseHerve/image' + strftime('%Y-%m-%d_%H%M%S') + '.jpg')
	#sleep(294)	
sleep(180)
shutdownpi()
