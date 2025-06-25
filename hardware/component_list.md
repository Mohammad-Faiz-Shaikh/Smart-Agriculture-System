# 🧰 Component List

These are the hardware components used in the Smart Agriculture System project:

| Component               | Quantity | Description |
|-------------------------|----------|-------------|
| **Arduino UNO**         | 1        | Microcontroller board for controlling all components |
| **Soil Moisture Sensor**| 1        | Detects the moisture level in the soil |
| **DHT11 / DHT22 Sensor**| 1        | Measures temperature and humidity |
| **Water Float Sensor**  | 1        | Detects water level in the tank or soil |
| **Wi-Fi Module (ESP8266)** | 1     | Sends sensor data to HiveMQ via internet |
| **LCD Display (16x2)**  | 1        | Displays real-time sensor readings |
| **Relay Module**        | 1        | Used to switch the water pump on/off |
| **Motor / Water Pump**  | 1        | Used for irrigation |
| **Power Supply (5V/12V)**| 1       | Powers the Arduino and motor system |
| **Jumper Wires**        | As needed| Used for electrical connections |
| **Breadboard / PCB**    | 1        | For prototyping the circuit |
| **HiveMQ Broker (Cloud)**| 1       | Cloud MQTT broker for real-time data transmission |

---

**Note**: The Wi-Fi module connects the Arduino to HiveMQ cloud for transmitting sensor data and receiving irrigation commands.
