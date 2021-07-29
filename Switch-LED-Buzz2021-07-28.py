#! /usr/bin/python3
# cording: utf-8

import pigpio,signal
from time import sleep

pinSW1=4
pinSW2=22
pinSW3=10
pinSW4=11

pinLED1=14
pinLED2=23
pinLED3=25
pinLED4=7

pinBuzz = 18

pinSW=[pinSW1,pinSW2,pinSW3,pinSW4]
pinLED=[pinLED1,pinLED2,pinLED3,pinLED4]

onNUM = 0

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    gpio = pigpio.pi()

    for pin in pinLED:
        gpio.set_mode(pin,pigpio.OUTPUT)
    
    for pin in pinSW:
        gpio.set_mode(pin, pigpio.INPUT)
        

    while True:
        for i in range(4):
            SW = not(bool(gpio.read(pinSW[i])))
            gpio.write(pinLED[i], SW)
            onNUM += SW

        if onNUM == 4:
            gpio.hardware_PWM(pinBuzz, 4000, 500000)
        else:
            gpio.hardware_PWM(pinBuzz, 0, 0)

        onNUM = 0
        sleep(0.05)
