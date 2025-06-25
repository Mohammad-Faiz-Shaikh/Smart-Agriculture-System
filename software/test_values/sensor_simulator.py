import paho.mqtt.client as mqtt
import json
import time
import random

broker = "smart-cluster-9oaghg.a01.euc1.aws.hivemq.cloud"
port = 8883
username = "mqttuser1"
password = "Badshah1"
topic = "smart/agriculture/data"

client = mqtt.Client()
client.username_pw_set(username, password)
client.tls_set()

client.connect(broker, port, 60)
client.loop_start()

try:
    while True:
        temperature = random.randint(20, 35)  # Simulated temperature
        humidity = random.randint(40, 80)     # Simulated humidity

        payload = {
            "d": {
                "temperature": temperature,
                "humidity": humidity
            }
        }

        print(f"Sending: {payload}")
        client.publish(topic, json.dumps(payload))
        time.sleep(5)

except KeyboardInterrupt:
    print("Simulation stopped.")
    client.loop_stop()
    client.disconnect()
