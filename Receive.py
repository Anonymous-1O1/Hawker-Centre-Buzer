#receiveing end
from microbit import *
import random
import radio
import music

rad=random.randint(0,79)
radio.on()
radio.config(channel=rad)
while True:
    display.scroll(rad)
    mes=radio.receive()
    if mes!=None:
        break
display.scroll("Set")
boolean=True
while boolean:
    display.scroll(rad)
    if radio.receive()!=None:
        if radio.receive()=="Ready":
            while boolean:
                display.show("R")
                music.play(['c1:1'])
                if radio.receive()=="Done":
                    display.show("D")
                    boolean=False
