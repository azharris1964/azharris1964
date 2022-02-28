from machine import ADC, Pin         # import analog pin
from m5stack import lcd              # import to draw to the lcd
import time                          # import to sleep
import random


# 47 is the number of the pin
# Pin.IN means that we want to use the pin as an input
#button = Pin(37, Pin.IN)
#prevButtonValue = 1               # store the previous state of the button
ballX = 40
ballY = 180
ballR = 30

analogPin = ADC(Pin(36))             # we set up pin G36 as analog input
analogPin.atten(ADC.ATTN_11DB)

# the following code shows
while True:

    knob = analogPin.read()

    lcd.clear()

    lcd.fillScreen(0x00FFFF)

    lcd.text(14, 60, "Good        Morning!")

    ballY = ballY - (knob/2000)  #moves the sun's position based on knob

    if ballY > 200 or ballY < -200:         # if the ball is out of bounds:
        ballY = 80

    lcd.fillCircle(ballX, round(ballY), ballR, 0xF1C232)  #draws the sun


    time.sleep_ms(33)
