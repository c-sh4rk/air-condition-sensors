import dataService

def readSensor(sensorId):
    file = open("/sys/bus/w1/devices/{:s}/w1_slave".format(sensorId))
    data = file.read()
    file.close()
    return float(data.split("\n")[1].split(" ")[9][2:]) / 1000

def printValues(sensorId, temperature):
    print("{:s}: Temperature={:0.1f} degree ".format(sensorId, temperature))

def readShowAndSave(sensorId):
    data = readSensor(sensorId)
    printValues(sensorId, data)
    dataService.addSensorData(sensorId, "temperature", data)

def readShowAndSaveAll():
    for sensorId in getListOfSensors():
        readShowAndSave(sensorId)

def getListOfSensors():
    file = open("/sys/bus/w1/devices/w1_bus_master1/w1_master_slaves")
    listOfSensors = file.read()
    file.close()
    list = listOfSensors.split("\n")
    strippedList = map(lambda e: e.strip(), list)
    return filter(lambda e: e, strippedList)
