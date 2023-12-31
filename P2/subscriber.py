# Receives (subscribes to) messages from the broker

import paho.mqtt.client as mqtt
import time

IP_ADDRESS = "10.0.0.74"  # original was "10.0.0.74"
port = 1883


def on_message(client, userdata, message):
    global isLocked, tempPass, tempActivated
    if str(message.payload.decode("utf-8")) == "Lock broken!":
        print("The lock has broken!")

    # if the entered password is the permanent
    elif message.payload.decode("utf-8") == permPass:
        print("Received Message ", str(message.payload.decode("utf-8")))
        if isLocked == 1:
            isLocked = 0
            tempActivated = False
            print("Correct password given. The lock is now unlocked, temporary password is disabled!")
        else:
            isLocked = 1
            tempActivated = True
            print("Correct password given. The lock is now locked, temporary password is activated!")

    # if the temporary password has been entered, and it's already been activated
    elif message.payload.decode("utf-8") == tempPass and tempActivated is True:
        print("Received Message ", str(message.payload.decode("utf-8")))
        if isLocked == 1:
            isLocked = 0
            tempActivated = False
            print("Temporary password used to unlock the lock. Temporary password is now disabled!")
        else:
            isLocked = 1
            print("Correct temporary password given. The lock is now locked!")    # temporary password is still active

    # if the temp password is entered, but it has not been activated yet.
    elif message.payload.decode("utf-8") == tempPass and tempActivated is False:
        print("Received Message ", str(message.payload.decode("utf-8")))
        print("The temporary password has not been activated yet. Enter the permanent password first!")

    else:
        print("Received Message ", str(message.payload.decode("utf-8")))
        print("Incorrect password entry!")


def on_connect(client, userdata, flags, rc):
    print("Connect: " + str(rc))  # rc, result code should be 0 on successful connection
    client.subscribe("MQTTLock")
    client.subscribe("LockStatus")


isLocked = 1  # lock starts as locked
tempActivated = False  # from the start only the permanent password can be used

# neither password will ever change
permPass = "123abc"
tempPass = "temp"

mqttBroker = IP_ADDRESS
client = mqtt.Client("Lock")

client.on_connect = on_connect  # set for on_connect callback
client.on_message = on_message  # when a message is received call the function

client.connect(mqttBroker, port=port)

client.loop_start()

time.sleep(500)  # time to wait before stopping the loop
client.loop_stop()
client.disconnect()
