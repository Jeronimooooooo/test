import ablib
import time
import os
import commands

from ablib import Pin
from time import sleep
 
print "**********************************"
print "*"
print "*  Test ACS AriaG25 Board"
print "*"
print "*"
print "* Test Output"
print "* Test Input"
print "* Test Modem"
print "* Test Analog"
print "* Test USB"
print "*"
print "* Type ctrl-C to exit"
print "*"
print "**********************************"
 
 
OUTDIG0 = Pin('W10','OUTPUT') 
OUTDIG1 = Pin('W9','OUTPUT')
LED1 = Pin('N17','OUTPUT')
STATUS_GSM = Pin('N16','INPUT')

LDIGIN0 = Pin('W16','INPUT')
LDIGIN1 = Pin('W15','INPUT')
LDIGIN2 = Pin('W14','INPUT')
LDIGIN3 = Pin('W13','INPUT')
LDIGIN4 = Pin('W12','INPUT')
LDIGIN5 = Pin('W11','INPUT')

while True:

	print""		
	print "**********************************"
	print "*"
	print "*  Test Output"
	print "*"
	print "*  Blinks every 2 seconds the" 
	print "*   OUTDIG0 - OUTDIG1 pins"
	print "*"
	print "**********************************"
	print""		
	sleep(2)
	print "OUTDIG0 ON"
	OUTDIG0.on()
	print "OUTDIG1 ON"
	OUTDIG1.on()
	sleep(2)
	print "OUTDIG0 OFF"
	OUTDIG0.off()
	print "OUTDIG1 OFF"
	OUTDIG1.off()
	sleep(2)
	
	print "OUTDIG0 ON"
	OUTDIG0.on()
	print "OUTDIG1 ON"
	OUTDIG1.on()
	sleep(2)
	print "OUTDIG0 OFF"
	OUTDIG0.off()
	print "OUTDIG1 OFF"
	OUTDIG1.off()
	sleep(2)
	
	sleep(3)

	print""
	print""	
	print "**********************************"
	print "*"
	print "*  Test Input"
	print "*"
	print "* If a digital input is triggered in "
	print "* low led1 flashes as the entry" 
	print "* number:"
	print "* LDIGIN0 - flashes 1x"
	print "* LDIGIN1 - flashes 2x"
	print "* LDIGIN2 - flashes 3x"
	print "* LDIGIN3 - flashes 4x"
	print "* LDIGIN4 - flashes 5x"
	print "* LDIGIN5 - flashes 6x"
	print "*"
	print "**********************************"
	print""			
	sleep(2)
	print "LDIGIN0: "
	if LDIGIN0.get_value()==0:
		LED1.on()
		sleep(0.3)
		LED1.off()
		sleep(0.3)
		print "ON"
	else:
		print "OFF"
		
	sleep(2)
	
	print "LDIGIN1: "
	if LDIGIN1.get_value()==0:
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)
		print "ON"
	else:
		print "OFF"

	sleep(2)
	
	print "LDIGIN2: "
	if LDIGIN2.get_value()==0:
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)
		print "ON"
	else:
		print "OFF"

	sleep(2)
	
	print "LDIGIN3: "		
	if LDIGIN3.get_value()==0:
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)		
		print "ON"
	else:
		print "OFF"

	sleep(2)
	
	print "LDIGIN4: "		
	if LDIGIN4.get_value()==0:
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)	
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)	
		print "ON"
	else:
		print "OFF"

	sleep(2)
	
	print "LDIGIN5: "	
	if LDIGIN5.get_value()==0:
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)	
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)
		LED1.on()
		sleep(0.3)
		LED1.off()	
		sleep(0.3)		
		print "ON"
	else:
		print "OFF"	
		
	sleep(3)

	print""
	print""	
	print "**********************************"
	print "*"
	print "*  Test Modem"
	print "*"
	print "* Does the sequence turn on"
	print "* wait 5 seconds and turn off, if"
	print "* it can not make one of these"
	print "* two operations it returns error "
	print "*"
	print "**********************************"
	print ""
	sleep(2)
	quectel_power = Pin('N15','HIGH')
	quectel_power_key = Pin('N13','LOW')

	quectel_power_key.on()
	sleep(1)
	quectel_power_key.off()

	if STATUS_GSM.get_value() == 1:
		print "MODEM ON"
	else:
		print "ERROR"
	
	sleep(5)

	quectel_power = Pin('N15','LOW')
	quectel_power_key = Pin('N13','LOW')
	
	quectel_power_key.off()
	sleep(1)
	quectel_power_key.on()
	
	if STATUS_GSM.get_value() == 0:
		print "MODEM OFF"
	else:
		print "ERROR"
		
	sleep(5)	

	print""
	print""
	print "**********************************"
	print "*"
	print "*  Test Analog"
	print "*"
	print "* Displays value read ANAIN_0"
	print "* and ANAIN_1 pins"
	print "*"
	print "**********************************"
	print ""
	sleep(2)
	print "ANAIN_0: "
	os.system("cat /sys/bus/iio/devices/iio\:device0/in_voltage3_raw")
	sleep(2)
	print "ANAIN_1: "
	os.system("cat /sys/bus/iio/devices/iio\:device0/in_voltage2_raw")
	sleep(2)

	
	print""
	print""
	print "**********************************"
	print "*"
	print "*  Test USB"
	print "*"
	print "* List available USB devices"
	print "*"
	print "**********************************"
	print""
	sleep(2)
	print "Ports: "
	os.system("lsusb")
	sleep(2)

	print""
