Originally gotten from: https://arduinogeek.wordpress.com/2014/04/23/raspberry-pi-with-i2c-2004-lcd/

1 - Enable and setup the I²C in Raspbian

Add the modules to the startup : :

`sudo nano /etc/modules`

Add those 2 lines:

`i2c-bcm2708` 
`i2c-dev`

We reboot :

`sudo reboot`

2 - We now install the required components :

`sudo apt-get install python-smbus i2c-tools`

We remove the I²C modules from the blacklist :

`sudo nano /etc/modprobe.d/raspi-blacklist.conf`

the line

`blacklist i2c-bcm2708` - becomes - `#blacklist i2c-bcm2708`

Our Raspberry should be ready to use I²C devices after a new reboot.

`sudo reboot`
