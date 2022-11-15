import RPi.GPIO as GPIO
import time

def button_pressed(channel):
    print('channel %s pressed'%channel)

GPIO.add_event_detect(12,GPIO.RISING,callback=button_pressed)

try:
    while 1:
        print(".")
        time.sleep(0.1)
finally:
    GPIO.cleanup()