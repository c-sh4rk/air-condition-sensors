import time
import dht
import dallas


while 1:
    dht.readShowAndSave("dht11-2", "DHT11", 2)
    dht.readShowAndSave("dht22-3", "DHT22", 3)
    dallas.readShowAndSaveAll()
    time.sleep(5)
