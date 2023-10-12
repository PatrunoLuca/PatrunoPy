// Libary to run the server
const express = require("express");
const app = express();

// File system library
const fs = require("fs");

// Format time date
const strftime = require("strftime");

// Define a database using a json file
const json_db = require("node-json-db");
const statuses = JSON.parse(fs.readFileSync("./private/statuses.json"));
const db = new json_db.JsonDB(
    new json_db.Config("./private/sensor_db.json", true, true, "//")
);

// Password to check if device is authorized
const token = "XXX";

// Define logger
const winston = require("winston");

const logger = winston.createLogger({
    level: "info",
    exitOnError: false,
    format: winston.format.combine(
        winston.format.timestamp({
            format: "YYYY/MM/DD HH:mm:ss",
        }),
        winston.format.simple()
    ),
    transports: [
        new winston.transports.Console(),
        new winston.transports.File({
            filename: "logger.log",
        }),
    ],
});

// If a post request is sent at any page
app.post("/", express.json(), (req, res) => {
    // Define status code
    let status_code = false;

    // Status is 415 if requiests is not a json
    if (!req.is("json") && status_code == false) {
        status_code = 415;
    }

    // Status is 401 if the token is not correct or not present in the request
    if (
        (!"token" in req.headers || req.get("token") != token) &&
        status_code == false
    ) {
        status_code = 401;
    }

    // WIP: CHECK THE SENSOR NUMBER
    // WIP: CHECK IF HUMIDITY, MOISTURE AND TEMPERATURE

    if (status_code === false) {
        // Set the path on the database to "sensor: {"date" : { "time" ; data } }"
        const db_path = `//sensor_${req.get("sensor_number")}//${strftime(
            "%y/%m/%d"
        )}//${strftime("%H:%M:%S.%L")}`;

        // Extract Humidity, Moisture and Temperature from the request
        const db_data = {
            humidity: req.body.humidity,
            moisture: req.body.moisture,
            temperature: req.body.temperature,
        };

        try {
            // Push to database
            db.push(db_path, db_data);
            status_code = 200;
        } catch (error) {
            // If some error happens on the server side add it to log and set the status_code to 400
            logger.error(error, { ip: req.socket.remoteAddress });
            status_code = 400;
        }
    }

    logger.http(statuses[status_code]["message"], {
        status_code: status_code,
        ip: req.socket.remoteAddress,
    });

    // Return response
    res.status(status_code).json(statuses[status_code]);
    res.end();
});

app.get("*", (req, res) => {
    status_message(req.socket.remoteAddress, statuses[400]);
    const message =
        "<h1>Error " +
        statuses[400]["status_code"] +
        ": " +
        statuses[400]["status"] +
        "</h1><h3>" +
        statuses[400]["description"] +
        "</h3>";
    res.status(400).send(message);
    res.end();
});

app.listen(3000, () => {
    console.log("Application started and Listening on port 3000");
});
