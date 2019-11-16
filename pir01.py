
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  #BCM setting

GPIO.setup(18,GPIO.IN)  #PIN number 18

print "PIR Sensor Test."

try:
 while True:
  if GPIO.input(18)==1:  #Active is 1
   print "Motion detected"
   time.sleep(0.2)  # delay 0.2[s]
  else:
   print "Motion not detected"
   time.sleep(0.2)

except KeyboardInterrupt:  # CTRL+C to Exit
 GPIO.cleanup()
