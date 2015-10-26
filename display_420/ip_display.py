# loading the class
import lcddriver
from time import *
from subprocess import *
from time import sleep, strftime
from datetime import datetime

# lcd start
lcd = lcddriver.lcd()

cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"

def run_cmd(cmd):
  p = Popen(cmd, shell=True, stdout=PIPE)
  output = p.communicate()[0]
  return output
 
while 1:
  lcd.lcd_clear()
  ipaddr = run_cmd(cmd)
  lcd.lcd_display_string(datetime.now().strftime('%b %d  %H:%M:%S\n'), 1)
  lcd.lcd_display_string('IP %s' % ( ipaddr ), 2)
  sleep(2)

