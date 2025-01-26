Smart Home Monitoring System Using Google Cloud Platform

Project Overview


This project demonstrates an IoT-based Smart Home Monitoring System leveraging Google Cloud Platform (GCP), MongoDB, MQTT protocol, and Arduino-based IoT devices. The system monitors temperature, humidity, motion, and smoke levels using sensors and processes the data for real-time analysis and storage.


Features:
Sensor data collection using Arduino IoT devices.
MQTT for message communication.
MongoDB for data storage and retrieval.
Secure communication using TLS/SSL.
Role-Based Access Control (RBAC) for GCP services.
Security configurations for monitoring and event logging.
Prerequisites
Hardware:

Arduino device with DHT11, IR motion sensor, and smoke sensor.
LED indicators for visual feedback.
Software:

Arduino IDE installed.
Python 3.7+ with paho-mqtt and pymongo libraries.
MongoDB installed locally or on MongoDB Atlas.
Cloud Services:

Google Cloud Platform account.
Enabled GCP services: Cloud Pub/Sub, Cloud Functions, etc.
Tools:

A text editor for configuration files (e.g., Nano, VS Code).
Git for version control.
SSH client (e.g., PuTTY) for connecting to your cloud instance.
Repository Structure

homeManagement/
homeManagement/
├── config/
│   ├── mongod.conf               # MongoDB local configuration
│   ├── mongodb-atlas.config      # MongoDB Atlas connection settings
│   ├── mosquitto.conf            # MQTT broker TLS/SSL settings
│   ├── rbac-config.json          # RBAC configuration for GCP services
├── MongoScript/
│   ├── ingest_mqtt_to_mongodb.py # Python script to ingest MQTT data to MongoDB
├── homeManagement.ino            # Arduino code for the IoT device
└── README.md                     # Documentation for the project

Getting Started
1. Clone the Repository
Set up the project by cloning the repository:

bash
Copy
Edit
git clone https://github.com/<MLAshahid>/homeManagement.git
cd homeManagement
2. Configure the Environment
Arduino Code:
Open homeManagement.ino in Arduino IDE.

Update the following constants with your configuration:

WiFi SSID and password:
cpp
Copy
Edit
const char* WIFI_SSID = "<Your-WiFi-SSID>";
const char* WIFI_PASSWORD = "<Your-WiFi-Password>";
MQTT broker details:
cpp
Copy
Edit
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
Copy
Edit
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
