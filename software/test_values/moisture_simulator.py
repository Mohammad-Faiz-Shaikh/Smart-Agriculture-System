import paho.mqtt.client as mqtt
import json
import time
import random

broker = "smart-cluster-9oaghg.a01.euc1.aws.hivemq.cloud"
port = 8883
username = "mqttuser1"
password = "Badshah1"
topic = "smart/agriculture/status"  # topic for moisture updates

client = mqtt.Client()
client.username_pw_set(username, password)
client.tls_set()

client.connect(broker, port, 60)
client.loop_start()

try:
    while True:
        # Random moisture level between 40% and 85%
        moisture = random.randint(40, 85)

        payload = {
            "moisture": moisture
        }

        print(f"Sending moisture: {payload}")
        client.publish(topic, json.dumps(payload))
        time.sleep(5)

except KeyboardInterrupt:
    print("Stopped.")
    client.loop_stop()
    client.disconnect()
