import RPi.GPIO as GPIO
import time

def switchPressed(channel):
    print('channel %s pressed!' %channel)
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(12,GPIO.RISING,callback=switchPressed)

try:
    while 1:
        print(".")
        time.sleep(0.1)
finally:
    GPIO.cleanup()