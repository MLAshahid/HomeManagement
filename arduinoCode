#include <PubSubClient.h>
#include <WiFi.h>
#include "DHT.h"

#define DHTTYPE DHT11
const int IR_SENSOR_PIN = 4;       // IR sensor pin
const int SMOKE_SENSOR_PIN = 15;   // Smoke sensor pin
const int DHT11_PIN = 42;          // DHT11 sensor pin
const int GREEN_LED_PIN = 9;       // Green LED for motion
const int RED_LED_PIN = 6;         // Red LED for high temperature
const int YELLOW_LED_PIN = 10;      // Yellow LED for high smoke

const char* WIFI_SSID = "40EdenHouse";
const char* WIFI_PASSWORD = "11801180";
const char* MQTT_SERVER = "34.122.46.212";
const char* MQTT_TOPIC = "iot";
const int MQTT_PORT = 1883;

char buffer[128] = ""; // Text buffer
DHT dht(DHT11_PIN, DHTTYPE);
WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(WIFI_SSID);

    WiFi.mode(WIFI_STA);
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.print(".");
    }

    Serial.println("\nWiFi connected");
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());
}

void setup() {
    Serial.begin(115200);
    dht.begin();                      // Initialize DHT sensor
    pinMode(IR_SENSOR_PIN, INPUT);    // Initialize IR sensor
    pinMode(SMOKE_SENSOR_PIN, INPUT); // Initialize smoke sensor
    pinMode(GREEN_LED_PIN, OUTPUT);   // Initialize green LED
    pinMode(RED_LED_PIN, OUTPUT);     // Initialize red LED
    pinMode(YELLOW_LED_PIN, OUTPUT);  // Initialize yellow LED
    setup_wifi();                     // Connect to WiFi
    client.setServer(MQTT_SERVER, MQTT_PORT); // Initialize MQTT server
}

void loop() {
    if (!client.connected()) {
        reconnect();
    }
    client.loop();

    // Read temperature and control red LED
    float temperature = dht.readTemperature();
    if (!isnan(temperature)) {
        sprintf(buffer, "Temperature: %.2f degree Celsius", temperature);
        client.publish(MQTT_TOPIC, buffer);
        Serial.println(buffer);

        if (temperature > 30.0) {
            digitalWrite(RED_LED_PIN, HIGH);
        } else {
            digitalWrite(RED_LED_PIN, LOW);
        }
    }

    // Read IR sensor state and control green LED
    int irState = digitalRead(IR_SENSOR_PIN);
    char irBuffer[64];
    if (irState == HIGH) {
        sprintf(irBuffer, "IR Sensor: Motion detected!");
        digitalWrite(GREEN_LED_PIN, !HIGH);
    } else {
        sprintf(irBuffer, "IR Sensor: No motion detected.");
        digitalWrite(GREEN_LED_PIN, !LOW);
    }
    client.publish(MQTT_TOPIC, irBuffer);
    Serial.println(irBuffer);

    // Read smoke level and control yellow LED
    int smokeLevel = analogRead(SMOKE_SENSOR_PIN);
    
    char smokeBuffer[64];
    sprintf(smokeBuffer, "Smoke Level: %d", smokeLevel);
    client.publish(MQTT_TOPIC, smokeBuffer);
    Serial.println(smokeBuffer);

    if (smokeLevel > 2000) { // Threshold for high smoke level
        digitalWrite(YELLOW_LED_PIN, HIGH);
        client.publish(MQTT_TOPIC, "Smoke Alert: High smoke level detected!");
        Serial.println("Smoke Alert: High smoke level detected!");
    } else {
        digitalWrite(YELLOW_LED_PIN, !LOW);
    }

    delay(1000); // Shortened delay for testing
}

void reconnect() {
    while (!client.connected()) {
        Serial.println("Attempting MQTT connection...");
        if (client.connect("ESP32Client")) {
            Serial.println("Connected to MQTT server");
        } else {
            Serial.print("Failed, rc=");
            Serial.println(client.state());
            delay(1000); // Shortened delay for testing
        }
    }
}
