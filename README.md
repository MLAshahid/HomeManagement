# Smart Home Monitoring System Using Google Cloud Platform

This repository contains the code and configuration files for the **Smart Home Monitoring System** project. The system leverages IoT devices, MQTT, MongoDB, and Google Cloud Platform to monitor and manage a smart home environment.

---

## Project Overview

This project uses:
- **IoT Sensors**: For real-time temperature, humidity, smoke, and motion detection.
- **MQTT**: For communication between sensors and backend services.
- **MongoDB**: For storing sensor data.
- **Google Cloud Platform**: To process and manage IoT data.

---

## Features

- Real-time data collection and monitoring.
- Secure communication using TLS/SSL.
- Role-Based Access Control (RBAC) for managing access to resources.
- Scalable architecture using MongoDB Atlas and Google Cloud.

---

## Directory Structure


homeManagement/
├── config/
│   ├── mongod.conf             # MongoDB local config file
│   ├── mongodb-atlas.config    # MongoDB Atlas config file
│   ├── mosquitto.conf          # Mosquitto MQTT broker TLS/SSL config
│   ├── rbac-config.json        # IAM roles and permissions config
├── MongoScript/
│   ├── ingest_mqtt_to_mongodb.py  # Python script to ingest MQTT data into MongoDB
├── homeManagement.ino          # Arduino IoT sensor code
└── README.md                   # Project documentation


Prerequisites
Hardware:
IoT sensors (DHT11, smoke, IR motion sensors, etc.).
ESP32 microcontroller.
Software:
Arduino IDE.
Python 3.x.
MongoDB installed locally or use MongoDB Atlas.
Mosquitto MQTT broker.
Google Cloud Services:
Enable Cloud Pub/Sub, Cloud Functions, and IAM roles.
Setup and Installation
1. Clone Repository
bash

git clone https://github.com/<your-username>/homeManagement.git
cd homeManagement
2. Configure the System
Update the configuration files in the config/ directory with your details:
WiFi SSID and Password
MQTT Broker Address
MongoDB Connection Strings
3. Run IoT Device Code
Open homeManagement.ino in Arduino IDE.
Update the WiFi and MQTT configurations in the code.
Upload the code to your ESP32.
4. Set Up Python Script for Data Ingestion
Install dependencies:
bash

pip install pymongo paho-mqtt
Run the Python script:
bash

python3 MongoScript/ingest_mqtt_to_mongodb.py
Security Features
Secure Communication:

Configured MQTT with TLS/SSL encryption. See config/mosquitto.conf.
Data Protection:

MongoDB Atlas uses IP whitelisting and encryption for secure data handling.
Role-Based Access Control:

IAM roles are set up for Google Cloud services. See config/rbac-config.json.
Example Configuration Files
MongoDB Atlas Configuration (mongodb-atlas.config)
json
{
  "cluster": "Cluster0",
  "database": "smarthome",
  "username": "<your-username>",
  "password": "<your-password>",
  "whitelist_ips": ["<your-ip>"]
}
Mosquitto Configuration (mosquitto.conf)
plaintext
Copy
Edit
listener 8883
cafile /etc/mosquitto/ca_certificates/ca.crt
certfile /etc/mosquitto/certs/server.crt
keyfile /etc/mosquitto/certs/server.key
Screenshots
Add relevant screenshots for:

Google Cloud setup.
Arduino IDE with uploaded code.
Python script running.
MongoDB data in the database.
References
Mosquitto MQTT Documentation
MongoDB Atlas Documentation
Google Cloud Platform IAM Documentation



Getting Started
1. Clone the Repository
Set up the project by cloning the repository:

bash

git clone https://github.com/<MLAshahid>/homeManagement.git
cd homeManagement
2. Configure the Environment
Arduino Code:
Open homeManagement.ino in Arduino IDE.

Update the following constants with your configuration:

WiFi SSID and password:

const char* WIFI_SSID = "<Your-WiFi-SSID>";
const char* WIFI_PASSWORD = "<Your-WiFi-Password>";
MQTT broker details:


const char* MQTT_SERVER = "<Your-MQTT-Broker-IP>";
const char* MQTT_TOPIC = "iot";
Connect your Arduino device and upload the code.

MongoDB Configuration:
For Local MongoDB: Use config/mongod.conf for local setup.
For MongoDB Atlas:
Create a cluster in MongoDB Atlas.
Update config/mongodb-atlas.config with your Atlas connection string.
MQTT Broker Configuration:
Configure Mosquitto with config/mosquitto.conf for TLS/SSL.
RBAC for GCP:
Use config/rbac-config.json to define role-based access permissions in GCP.
3. Running the System
Step 1: Start MQTT Broker
If using Mosquitto locally, start it with:

bash

mosquitto -c config/mosquitto.conf
Step 2: Run the Python Backend
Run the ingest_mqtt_to_mongodb.py script to handle incoming MQTT messages and store them in MongoDB:

bash

python3 MongoScript/ingest_mqtt_to_mongodb.py
Step 3: Monitor Arduino
Use the Arduino Serial Monitor to observe sensor data being published to the MQTT broker.

Step 4: Access MongoDB
Query your MongoDB database to verify the ingested data:

bash

mongo
> use smarthome
> db.iot.find().pretty()
Security Measures
Secure MQTT Communication: Configured mosquitto.conf for TLS/SSL encryption.

MongoDB Security:

IP whitelisting for Atlas.
Encrypted communication using MongoDB Atlas.
RBAC:

Defined IAM roles in rbac-config.json for secure GCP access.
Monitoring:

Logs simulated in config/security.log.
How to Set Up the GitHub Repository
Create a Repository:

Log in to your GitHub account and create a new repository named homeManagement.
Push Files to GitHub: Run the following commands:

bash

git init
git add .
git commit -m "Initial commit for Smart Home Monitoring System"
git branch -M main
git remote add origin https://github.com/<your-username>/homeManagement.git
git push -u origin main
Screenshots
Configuration Examples:
MongoDB Connection: Screenshot of mongodb-atlas.config.
MQTT TLS/SSL: Screenshot of mosquitto.conf.
References
MongoDB Atlas Documentation: https://www.mongodb.com/docs/atlas/
Google Cloud Pub/Sub: https://cloud.google.com/pubsub/docs
Mosquitto MQTT Documentation: https://mosquitto.org/documentation/
