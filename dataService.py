import database

def addSensorData(sensorId, type, value):
    query = "INSERT INTO sensor_data (sensorId, type, value) VALUES(%s, %s, %s)"
    data = (sensorId, type, value)
    database.cursor.execute(query, data)
    database.connection.commit()
