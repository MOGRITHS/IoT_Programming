import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
red_led=GPIO.PWM(16,500)
red_led.start(0)

try:
    while True:
        for i in range (101):
            if i==100:
                i=0
            red_led.ChangeDutyCycle(i)
            time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    red_led.stop()
    GPIO.cleanup()
