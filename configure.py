import os
import json
import cv2


def spots(data_directory: str, parking_spots: list[int]):
    spots = []
    image = cv2.imread("temp/test.jpg")
    for spot_count in parking_spots:
        row = []
        for _ in range(spot_count):
            roi = list(
                cv2.selectROI("Selector", image, showCrosshair=False, fromCenter=False)
            )

            spot = [roi[0], roi[1], roi[0] + roi[2], roi[1] + roi[3]]
            row.append(spot)

            cv2.rectangle(
                image,
                spot[0:2],
                spot[2:4],
                (100, 255, 100),
                3,
            )
        spots.append(row)

    os.makedirs(data_directory, exist_ok=True)

    try:
        with open(os.path.join(data_directory, "config.json"), "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data["spots"] = spots

    with open(os.path.join(data_directory, "config.json"), "w") as file:
        json.dump(data, file, indent=2)


def threshold(data_directory: str, thresholds: list[float]):
    try:
        with open(os.path.join(data_directory, "config.json"), "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data["threshold"] = {"value": thresholds[0], "saturation": thresholds[1]}

    with open(os.path.join(data_directory, "config.json"), "w") as file:
        json.dump(data, file, indent=2)
