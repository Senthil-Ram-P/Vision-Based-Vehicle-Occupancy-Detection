import os
import json
import cv2
import numpy as np
import subprocess
import time 


import board
from digitalio import DigitalInOut
from adafruit_character_lcd.character_lcd import Character_LCD_Mono
import RPi.GPIO as GPIO



# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

lcd_rs = DigitalInOut(board.D26)
lcd_en = DigitalInOut(board.D19)
lcd_d4 = DigitalInOut(board.D13)
lcd_d5 = DigitalInOut(board.D6)
lcd_d6 = DigitalInOut(board.D5)
lcd_d7 = DigitalInOut(board.D11)

lcd = Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows
)


pwm_pin = 18
GPIO.setup(pwm_pin, GPIO.OUT)

pwm = GPIO.PWM(pwm_pin, 100)
pwm.start(0)



def detect(data_directory: str):
    while True:
        with open(os.path.join(data_directory, "config.json"), "r") as file:
            data = json.load(file)

        cmd = [
            "rpicam-jpeg",
            "-o", "data/image.jpeg"
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print("Error running camera command:")
            print(result.stderr)
        else:
            print("Image captured successfully")

        image = cv2.imread("data/image.jpeg")
        status = []
        count = 0
        total = 0
        for row in data["spots"]:
            row_status = []
            for spot in row:
                cropped = image[spot[1] : spot[1] + spot[3], spot[0] : spot[0] + spot[2]]
                is_occupied = check_spot_is_occupied(cropped, data["threshold"])
                row_status.append(is_occupied)
                total+=1
                if is_occupied:
                    count+=1
            status.append(row_status)

        lcd.message = ""
        for spot in status[0]:
            lcd.message += "X" if spot else "O"

        lcd.message += f"   Used: {count}/{total}\n "

        for spot in status[1]:
            lcd.message += "X" if spot else "O"

        lcd.message += f"   Open: {'Yes' if count != total else 'No '}"

        if count != total:
            pwm.ChangeDutyCycle(5)
        else:
            pwm.ChangeDutyCycle(24)
        time.sleep(1)


def check_spot_is_occupied(image, threshold):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    value_threshold = threshold["value"]
    saturation_threshold = threshold["saturation"]

    value_count = np.count_nonzero(v > value_threshold)
    saturation_count = np.count_nonzero(s > saturation_threshold)

    value_percent = value_count / v.size
    saturation_percent = saturation_count / h.size

    print(f"Value: {value_percent}\nSaturation: {saturation_percent}")

    return value_percent > 0.4 or (value_percent > 0.1 and saturation_percent > 0.3)
