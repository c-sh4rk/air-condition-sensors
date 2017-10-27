

def readSensor(sensorId):
    file = open("/sys/bus/w1/devices/{:s}/w1_slave".format(sensorId))
    data = file.read()
    file.close()
    return float(data.split("\n")[1].split(" ")[9][2:]) / 1000
