import RPi.GPIO as GPIO
import time

LED=16
BUZZER=25
PIR=24
BTN=12
last_time=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(BUZZER,GPIO.IN)
GPIO.setup(BUZZER,GPIO.OUT)
GPIO.setup(PIR,GPIO.IN)


def buzz():
    pitch=1000                  #주파수
    duration=0.1                #울리는 시간
    period=1.0/pitch            #진동을 만들어 내기 위한 간격
    delay=period/2              #간격의 절반을 delay
    cycles=int(duration*pitch)
    
    for i in range(cycles):
        GPIO.output(BUZZER,True)
        time.sleep(delay)
        GPIO.output(BUZZER,False)
        time.sleep(delay)
        
try:
    while 1:
        if GPIO.input(PIR)==True:
            control=1
        if control==1:
            while True:
                buzz()
                GPIO.output(LED,True)
                if GPIO.input(BTN)==False:
                    GPIO.output(LED,False)
                    control=0
                    break
                time.sleep(0.3)
        time.sleep(0.3)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
                
