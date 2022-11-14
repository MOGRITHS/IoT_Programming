from tkinter import *
import time

root=Tk()

REDLED=False
R_i=0
GREENLED=False
G_i=0
BLUELED=False
B_i=0
led_pwm=IntVar()
LED=0



def turnonRedled():
    global R_i
    if(R_i%2==0):
        print("Red Led On")
        REDLED=True
        R_i+=1
    else:
        print("Red Led Off")
        REDLED=False
        R_i+=1
    
def turnonGreenled():
    global G_i
    if(G_i%2==0):
        print("Green Led On")
        GREENLED=True
        G_i+=1
    else:
        print("Green Led Off")
        GREENLED=False
        G_i+=1
        
def turnonBlueled():
    global B_i
    if(B_i%2==0):
        print("Blue Led On")
        BLUELED=True
        B_i+=1
    else:
        print("Blue Led Off")
        BLUELED=False
        B_i+=1

def switchPwm(self):
    global LED
    LED=str(pwm_slide.get())
    text="pwm state: "+LED
    pwm_label.config(text=text)

def blinkLed():
    print("Red led on")
    time.sleep(0.2)
    print("Red led off")
    print("Green led on")
    time.sleep(0.2)
    print("Green led off")
    print("Blue led on")
    time.sleep(0.2)
    print("Blue led off")
    
redled_btn=Button(root,text="Red Led On",command=turnonRedled)
greenled_btn=Button(root,text="Green Led On",command=turnonGreenled)
blueled_btn=Button(root,text="Green Led On",command=turnonBlueled)
pwm_label=Label(root,text="pwm state: ")
pwm_slide=Scale(root,command=switchPwm,showvalue=False,from_=0,to=255,variable=led_pwm,orient="horizontal")
blink_btn=Button(root,text="Blink",command=blinkLed)

redled_btn.grid(row=1,column=1)
greenled_btn.grid(row=1,column=2)
blueled_btn.grid(row=1,column=3)
pwm_label.grid(row=2,column=2)
pwm_slide.grid(row=3,column=2)
blink_btn.grid(row=4,column=1)

root.mainloop()