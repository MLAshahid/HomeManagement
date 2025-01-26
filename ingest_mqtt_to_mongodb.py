import pymongo
import paho.mqtt.client as mqtt
from datetime import datetime, timezone

# MongoDB configuration
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["smarthome"]
collection = db["iot"]

# MQTT configuration
mqtt_broker_address = "34.122.46.212"  # Your MQTT broker address
mqtt_topic = "iot"

# Define the callback function for connection
def on_connect(client, userdata, flags, reason_code, properties=None):
    if reason_code == 0:
        print(f"Successfully connected to MQTT broker at {mqtt_broker_address}")
        client.subscribe(mqtt_topic)
    else:
        print(f"Failed to connect, reason code: {reason_code}")

# Define the callback function for ingesting data into MongoDB
def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    print(f"Received message: {payload}")
    
    # Add timestamp to the message
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
    # Insert data into MongoDB
    document = {"timestamp": timestamp, "data": payload}
    collection.insert_one(document)
    print("Data ingested into MongoDB")

# Create MQTT client instance
client = mqtt.Client(protocol=mqtt.MQTTv311)  # Use the latest protocol version
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(mqtt_broker_address, 1883, 60)

# Start the MQTT loop
try:
    print("Listening for MQTT messages...")
    client.loop_forever()
except KeyboardInterrupt:
    print("Script terminated by user.")
