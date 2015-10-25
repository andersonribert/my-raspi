from checkoutApi import CheckoutApi
from display import Display
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    # will keep running until the button is pressed
    input_state = GPIO.input(18)
    # when the button is pressed:
    if input_state == False:
        time.sleep(0.2)
        lcd = Display()
        chkAPI = CheckoutApi()

        # clear lcd and then show text asking for user's tag
        lcd.clear_lcd()
        lcd.show_msg_firstLine("Please Scan your")
        lcd.show_msg_secondLine("tag: ")
        # prompt on command line
        user_tag_id=raw_input("Please Scan your tag to Start : ")
        # clear lcd and then show text asking for device's tag
        lcd.clear_lcd()
        lcd.show_msg_firstLine("Please Scan the")
        lcd.show_msg_secondLine("device's tag: ")
        # prompt on command line
        device_tag_id=raw_input("Please, Scan the device you are checking out. : ")

        # clean up,# prompt on command line
        lcd.clear_lcd()
        chkAPI.checkout_device(device_tag_id, user_tag_id)
        lcd.__init__()
