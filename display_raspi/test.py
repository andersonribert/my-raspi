# loading the class
import lcddriver
from time import *

### THIS SECTION IS FOR BASIC DISPLAY TEST ########

# lcd start
lcd = lcddriver.lcd()

# this command clears the display (captain obvious)
lcd.lcd_clear()

# basic lcd screen test
# now we can display some characters (text, line)
lcd.lcd_display_string("   Hello world !", 1)
lcd.lcd_display_string("      I am", 2)
