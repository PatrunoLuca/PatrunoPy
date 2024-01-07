import requests as rqst
from random import randint
import logging
from os import path
from time import sleep


SLEEPTIME = 20


class NodeSample:
    def __init__(self, url: str, token=None, sensornum=0) -> None:
        self.url = url
        self.token = token
        self.headers = {}

        if token is not None:
            self.headers["token"] = self.token

        self.sensor = str(sensornum)
        self.headers["sensor_number"] = self.sensor

        self._start_log()

    def _start_log(self):
        if path.exists("tests.log") is False:
            with open("tests.log", "w"):
                pass

        logging.basicConfig(
            filename="tests.log",
            filemode="a",
            format="%(asctime)s - %(message)s",
            datefmt="%d/%m/%y %H:%M:%S",
        )

    def post(self, humidity: int, light: int, moisture: int, temperature: int) -> None:
        logging.warning(
            str(
                rqst.post(
                    self.url,
                    json={
                        "humidity": humidity,
                        "light": light,
                        "moisture": moisture,
                        "temperature": temperature,
                    },
                    headers=self.headers,
                ).json()
            )
        )


if __name__ == "__main__":
    Node = NodeSample("http://localhost:3000", token="XXX")

    for i in range(200):
        Node.post(randint(20, 50), randint(200, 1000), randint(300, 900), randint(0, 40))
        sleep(SLEEPTIME)
