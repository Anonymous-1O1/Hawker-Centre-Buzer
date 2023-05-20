#Sending code
from microbit import *
import radio
rad_ones=0
rad_tens=0
while True:
    rad=(rad_tens*10)+rad_ones
    display.scroll(rad)
    if button_a.was_pressed():
        if rad_tens==7:
            rad_tens=0
        else:
            rad_tens+=1
    elif button_b.was_pressed():
        if rad_ones==9:
            rad_ones=0
        else:
            rad_ones+=1
    if pin_logo.is_touched():
        break
display.scroll("set",rad)
radio.on()
radio.config(channel=rad)
radio.send("Connected")
while True:
    display.show(rad)
    if button_a.is_pressed():
        while True:
            display.show("R")
            radio.send("Ready")
            if button_b.was_pressed():
                while True:
                    display.show("D")
                    radio.send("Done")
    sleep(100)
