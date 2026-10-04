import os
import json
import cv2
import numpy as np


def spots(data_directory: str):
    image = cv2.imread("temp/test.jpg")

    with open(os.path.join(data_directory, "config.json"), "r") as file:
        data = json.load(file)

    for row in data["spots"]:
        for spot in row:
            cv2.rectangle(
                image,
                spot[0:2],
                spot[2:4],
                (100, 255, 100),
                3,
            )

    cv2.imshow("Spots", image)
    cv2.waitKey(0)


def threshold(data_directory: str):
    with open(os.path.join(data_directory, "config.json"), "r") as file:
        data = json.load(file)

    image = cv2.imread("temp/test.jpg")
    for i, row in enumerate(data["spots"]):
        for j, spot in enumerate(row):
            cropped = image[spot[1] : spot[3], spot[0] : spot[2]]

            hsv = cv2.cvtColor(cropped, cv2.COLOR_BGR2HSV)
            h, s, v = cv2.split(hsv)

            value_threshold = data["threshold"]["value"]
            saturation_threshold = data["threshold"]["saturation"]

            value_mask = ((v > value_threshold) * 255).astype(np.uint8)
            saturation_mask = ((s > saturation_threshold) * 255).astype(np.uint8)

            cv2.imshow(f"{i}:{j}:value", value_mask)
            cv2.waitKey(0)

            cv2.imshow(f"{i}:{j}:saturation", saturation_mask)
            cv2.waitKey(0)
