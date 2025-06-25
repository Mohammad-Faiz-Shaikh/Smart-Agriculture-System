import time
import sys
import ibmiotf.device

organization = "your_org_id"
deviceType = "iotdevice1"
deviceId = "qwerty123"
authMethod = "token"
authToken = "your_auth_token"

def myCommandCallback(cmd):
    command = cmd.data['command']
    print("Command received:", command)
    if command == "ON":
        print("Motor ON")
    elif command == "OFF":
        print("Motor OFF")
    elif command == "runfor30minutes":
        print("Motor will run for 30 minutes...")
        for i in range(30, 0, -1):
            print(f"{i} minutes left")
            time.sleep(1)
        print("Motor OFF after 30 minutes")

try:
    deviceOptions = {
        "org": organization,
        "type": deviceType,
        "id": deviceId,
        "auth-method": authMethod,
        "auth-token": authToken
    }
    client = ibmiotf.device.Client(deviceOptions)
    client.connect()
    client.commandCallback = myCommandCallback
    while True:
        time.sleep(1)

except Exception as e:
    print("Error:", e)
    sys.exit()