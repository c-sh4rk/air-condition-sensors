#!/usr/bin/python

import time
import dht
import dallas

while 1:
    dht.readShowAndSave("dht22-2", "DHT22", 2, 1)
    dht.readShowAndSave("dht22-3", "DHT22", 3, 0)
    dht.readShowAndSave("dht11-17", "DHT11", 17, 0)
    dallas.readShowAndSaveAll()
    time.sleep(30)
