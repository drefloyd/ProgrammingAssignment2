import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    global isLocked, tempPass, tempActivated
    print("Received message: ", str(message.payload.decode("utf-8")))

    # if the entered password is the permanent
    if message.payload.decode("utf-8") == permPass:
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
        if isLocked == 1:
            isLocked = 0
            tempActivated = False
            print("Temporary password used to unlock the lock. Temporary password is now disabled!")
        else:
            isLocked = 1
            print("Correct temporary password given. The lock is now locked!")    # temporary password is still active

    # if the temp password is entered, but it has not been activated yet. Not sure if we should include this or not
    elif message.payload.decode("utf-8") == tempPass and tempActivated is False:
        print("The temporary password has not been activated yet. Enter the permanent password first!")

    else:
        print("Incorrect password entry!")


isLocked = 1  # lock starts as locked
tempActivated = True  # from the start either the permanent or temporary passwords can be given

# neither password will ever change (given the instructions)
permPass = "123abc"
tempPass = "temp"

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Lock")

client.on_message = on_message  # when a message is received call the function

client.connect(mqttBroker)

client.loop_start()
client.subscribe("MQTTLock")

time.sleep(50)  # time to wait before stopping the loop
client.loop_stop()
client.disconnect()
