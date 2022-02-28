import network
from m5stack import lcd

wifi = network.WLAN(network.STA_IF)  # set the WiFi to station mode
wifi.active(True)                    # turn it on

lcd.clear()

while True:
    access_points = wifi.scan()
    if 0 < len(access_points):
        lcd.text(0, 10, "Closest AP")
        lcd.text(0, 30, access_points[0][0])       # that's the name
        lcd.text(0, 70, "Strength")
        lcd.text(0, 90, str(access_points[0][3]))  # -23[dbM] is closer than -50[dbM]
