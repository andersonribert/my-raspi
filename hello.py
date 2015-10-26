import serial,time

# Set screen width in characters
SCREEN_WIDTH = 16

# Initialize serial connection
ser = serial.Serial(port='/dev/ttyAMA0', baudrate=9600)

# Set display to with cursor blink (25 for blinking cursor)
ser.write(chr(24))

# Set backlight to true
ser.write(chr(17))
