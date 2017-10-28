import Adafruit_DHT
import dataService
import display

def readSensor(name, gpio):
    if name == "DHT11":
        sensorName = Adafruit_DHT.DHT11
    elif name == "DHT22":
        sensorName = Adafruit_DHT.DHT22
    else:
        sensorName = Adafruit_DHT.DHT22

    humidity, temperature = Adafruit_DHT.read_retry(sensorName, gpio)

    return {
        "humidity": humidity,
        "temperature": temperature
    }


def printValues(sensorId, humidity, temperature):
    print("{:s}: Temperature={:0.1f} degree  Humidity={:0.1f} %".format(sensorId, temperature, humidity))

def readShowAndSave(sensorId, name, gpio, showOnDisplay):
    data = readSensor(name, gpio)

    printValues(sensorId, data["humidity"], data["temperature"])
    dataService.addSensorData(sensorId, "humidity", data["humidity"])
    dataService.addSensorData(sensorId, "temperature", data["temperature"])
    if showOnDisplay == 1:
        display.writeSensorValue(sensorId, data["temperature"], data["humidity"])
