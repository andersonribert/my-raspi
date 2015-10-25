#!/usr/bin/env python
import serial
# configure the serial connection
ser = serial.Serial(port='/dev/ttyAMA0',baudrate=9600)

class Display:
    def __init__(self):
        ser.write('\xFE\x01') # Clears lcd
        ser.write("Lab is open")

    def clear_lcd(self):
        ser.write('\xFE\x01') # Clears lcd

    def show_msg_firstLine(self,msg):
        ser.write('\xFE\x80') # SETS THE CURSOR ON THE FIRST LINE, FIRST
        ser.write(str(msg))
    
    def show_msg_secondLine(self, msg):
        ser.write('\xFE\xC0') #SETS THE CURSOR ON THE SECOND LINE,
        ser.write(str(msg))


