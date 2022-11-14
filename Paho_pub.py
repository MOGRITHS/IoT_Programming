import paho.mqtt.client as mqtt

mqtt=mqtt.Client("MOGRITHS")

mqtt.connect("localhost",1883)

mqtt.publish("MOGRITHS","hello")
mqtt.publish("MOGRIHTS","world")
mqtt.loop(2)