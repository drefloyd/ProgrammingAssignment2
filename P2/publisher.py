import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"  # establishes broker
client = mqtt.Client("Temperature_inside")  # create client and name
client.connect(mqttBroker)  # connects client to broker

while True:
    randomNumber = uniform(20.0, 21.0)  # random decimal from 20 to 21
    client.publish("TEMPERATURE", randomNumber)  # publishes the random number on the "TEMPERATURE" topic
    print("Just published " + str(randomNumber) + " to Topic: TEMPERATURE")
    time.sleep(1)

# from youtube video: https://www.youtube.com/watch?v=kuyCd53AOtg
