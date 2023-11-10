import paho.mqtt.client as mqtt


mqttBroker = "mqtt.eclipseprojects.io"  # establishes broker
client = mqtt.Client("MQTTLock")  # create client and name

client.connect(mqttBroker)  # connects to broker

passwordEntered = "N/A"

while True:
    passwordEntered = input("Enter a password to Lock/Unlock: ")
    client.publish("MQTTLock", passwordEntered)
    print(f"Just published '{passwordEntered}' to Topic: MQTTLock")
