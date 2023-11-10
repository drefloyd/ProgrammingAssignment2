import paho.mqtt.client as mqtt
import time

isLocked = 0


def on_message(client, userdata, message):
    global isLocked
    print("Received message: ", str(message.payload.decode("utf-8")))
    if message.payload.decode("utf-8") == password:
        if isLocked == 1:
            isLocked = 0
            print(f"correct password given, lock is now locked!")
        else:
            isLocked = 1
        print(f"correct password given, lock is now unlocked!")
    else:
        print(f"incorrect password given!")


password = "123abc"
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Lock")

client.on_message = on_message  # when a message is received call the function

client.connect(mqttBroker)

client.loop_start()
client.subscribe("MQTTLock")

time.sleep(30)
client.loop_stop()
client.disconnect()
