##################################################################################################################################
#                                                       Adarsh , Gunjan , Jishnu                                                               #
##################################################################################################################################

import serial 
import sys
import os

ser = serial.Serial('/dev/ttyACM0',9600) 

path='/sys/class/backlight/intel_backlight/brightness' 



while(1):
	try:
		value  = ser.readline().split()
		val = int(value[0])
		print (val) 

		if(val <= 70):
			os.system('xrandr --output eDP-1 --brightness 0.5')
		if(val >=70 and val <= 200):
			os.system('xrandr --output eDP-1 --brightness 1.0')
		if(val > 200):
			os.system('xrandr --output eDP-1 --brightness 1.5')

	
	except KeyboardInterrupt:
		print('Interrupted')
		break
	# finally:
		# ser.close()
		# Just to take care of initial garbage values

		
############################################################# END ##################################################################
