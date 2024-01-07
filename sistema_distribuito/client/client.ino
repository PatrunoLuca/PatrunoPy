// Library for humidity and temperature sensor
#include <DHT.h>

// Library to use WIFI
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

// DHT
#define DHTPIN D4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// Light and Moisture
#define LIGHTPIN A0
#define MOISTUREPIN A1

// Network SSID
#define SSID "XXX"
#define PASSWORD "XXX"

// Server Data
#define SERVER "XXX"        // Url to the server
#define TOKEN "XXX"         // Password to send to the server
#define SENSOR_NUMBER "1" // It's important to put a different number on every device to handle the data on the server

// Delay between every iteration of the cycle
#define CYCLEDELAY 5000

void setup() {
    Serial.begin(9600);
    dht.begin();

    // Two Blank Lines
    Serial.println("");
    Serial.println("");

    // Connect WiFi
    WiFi.begin(SSID, PASSWORD);

    // Wait for device to get connected to the WIFI
    while (WiFi.status() != WL_CONNECTED) {
      Serial.print(".");
      delay(500);
    }

    // Device has connected succesfully to WIFI
    Serial.println();
    Serial.print("Connected! IP address: ");
    Serial.println(WiFi.localIP());
}

void loop()
{
    if ((WiFi.status() == WL_CONNECTED))
    {

        // Read sensors data
        int h = dht.readHumidity();
        int l = analogRead(LIGHTPIN);
        int m = analogRead(MOISTUREPIN);
        int t = dht.readTemperature();

        WiFiClient client;
        HTTPClient http;

        // Connect to the server
        Serial.println("[HTTP] begin...");
        http.begin(client, SERVER);

        // Set headers of the requests
        http.addHeader("Content-Type", "application/json");
        http.addHeader("token", TOKEN);
        http.addHeader("sensor_number", SENSOR_NUMBER);

        // Format data to json
        String post_data = "{\"humidity\" : " + String(h) + ", \"light\" : " + String(l) +", \"moisture\" : " + String(m) + ", \"temperature\" : " + String(t) + "}";

        Serial.println(post_data);
        int httpCode = http.POST(post_data);

        // If http is a positive number it means the request was a success
        if (httpCode > 0)
        {

            // Show informations received after the succesful requests
            Serial.printf("\t[HTTP] POST... code: %d\n", httpCode);
            if (httpCode == HTTP_CODE_OK)
            {
                const String &payload = http.getString();
                Serial.print("\treceived payload: << ");
                Serial.print(payload);
                Serial.println(" >>");
            }
        }
        else
        {
            // Print error if the request wasn't succesful
            Serial.printf("\t[HTTP] POST... failed, error: %s\n", http.errorToString(httpCode).c_str());
        }

        http.end();
    }

    delay(CYCLEDELAY);
}