#버튼으로 사진 찍기
import Pi_Camera
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)
camera=picamera.Picamera()
camera.resolution=(1920,1080)

try:
    while True:
        button_state=GPIO.input(12)
        if button_state==False:
            print('Button Pressed.')
            time.sleep(2)
            camera.capture('example.jpg')
            break
    time.sleep(2)
except KeyboardInterrupt:
    pass
finally:
    camera.close()
    GPIO.cleanup()