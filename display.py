# -*- coding: utf-8 -*-
import time
from RPLCD.gpio import CharLCD
from RPi import GPIO

lcd = CharLCD(pin_rs=14, pin_rw=8, pin_e=15, pins_data=[18, 23, 24, 25],
              numbering_mode=GPIO.BCM)

def writeSensorValue(sensorId, temperature, humidity):
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string(sensorId)
    lcd.cursor_pos = (1, 0)
    lcd.write_string("T={:0.1f} H={:0.1f} %".format(temperature, humidity))

#lcd.clear()
