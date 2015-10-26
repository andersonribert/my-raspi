1 - Enable and setup the I²C in Raspbian
=
Add the modules to the startup : :

`sudo nano /etc/modules`

Add those 2 lines:

`i2c-bcm2708` 
`i2c-dev`

We reboot :

`sudo reboot`

2 - We now install the required components :
=
`sudo apt-get install python-smbus i2c-tools`

We remove the I²C modules from the blacklist :

`sudo nano /etc/modprobe.d/raspi-blacklist.conf`

the line

`blacklist i2c-bcm2708` - becomes - `#blacklist i2c-bcm2708`

Our Raspberry should be ready to use I²C devices after a new reboot.

`sudo reboot`

3 - Testing the I²C
=
We are going to use the i2cdetect command to list every I²C devices. This command is not the same on a Rev 1 or Rev 2 Pi (I²C bus address is different), so it’s important to choose the right one :

- `sudo i2cdetect -y 0` (for Rev 1)
- `sudo i2cdetect -y 1` (for Rev 2)

On this screenshot, you can see my Pi has 3 I²C devices :
– display with address #27
– unused AT24C32 eeprom chip with address #50
– DS1307 RTC with address #68. It is noted « UU » because it’s in use.
Your display may have another address. I’ve seen #24 and #28 but it can be something else. It should be indicated in the display’s datasheet. We need this address to setup the driver a little later in lcddriver.py file, where you’ll have to set the I²C address. It defaults to #27 :

`# LCD Address`

`ADDRESS = 0x27`

Originally gotten from: https://arduinogeek.wordpress.com/2014/04/23/raspberry-pi-with-i2c-2004-lcd/

And https://github.com/CaptainStouf/raspberry_lcd4x20_I2C
