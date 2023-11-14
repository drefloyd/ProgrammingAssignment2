# publishes messages to the MQTT broker


import paho.mqtt.client as mqtt

IP_ADDRESS = "10.0.0.74"
mqttBroker = IP_ADDRESS  # establishes broker
client = mqtt.Client("MQTTLock")  # create client and name

LWT_TOPIC = "LockStatus"
LWT_MESSAGE = "Lock broken!"
client.will_set(LWT_TOPIC, LWT_MESSAGE, qos=1, retain=False)

client.connect(mqttBroker)  # connects to broker

passwordEntered = "N/A"

while True:
    passwordEntered = input("Enter a password to Lock/Unlock: ")
    client.publish("MQTTLock", passwordEntered)
    print(f"Just published '{passwordEntered}' to Topic: MQTTLock")
