# 🚗 Vision-Based Vehicle Occupancy Detection

A smart parking system that uses computer vision to detect whether parking spaces are occupied or vacant. The system uses a camera connected to a Raspberry Pi and processes the captured images to determine parking-space occupancy.

## 📌 Project Overview

The aim of this project is to develop a vision-based parking system that can monitor parking spaces in real time without requiring a separate physical sensor for every parking slot.

The system captures the parking area using a camera, processes the image, analyzes individual parking spaces, and determines whether each space is occupied or vacant.

## 🎯 Objectives

- Detect vehicle occupancy in designated parking spaces.
- Process camera images using computer vision techniques.
- Display the parking status through the connected output system.
- Build a low-cost smart parking prototype using Raspberry Pi.
- Reduce dependence on individual sensors for each parking space.

## ⚙️ How It Works

The basic workflow of the system is:

Camera
↓
Image Acquisition
↓
Image Preprocessing
↓
Parking-Slot Analysis
↓
Occupancy Detection
↓
Output Display

The system processes the captured parking-area image and analyzes the predefined parking-space regions to determine whether vehicles are present.

## 🛠️ Technologies Used

### Software

- Python
- OpenCV
- NumPy
- JSON

### Hardware

- Raspberry Pi
- Camera
- LCD display
- GPIO components
- Connecting wires
- Breadboard

## 📁 Project Structure

```text
Vision-Based-Vehicle-Occupancy-Detection/
│
├── main.py
├── detect.py
├── configure.py
├── show.py
├── config.json
├── image.jpeg
├── requirements.txt
└── README.md
