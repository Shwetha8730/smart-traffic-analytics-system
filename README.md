# 🚦 Intelligent Traffic Monitoring and Analytics System using OpenCV, YOLOv8 and Firebase

## 📖 Overview

This project presents a Smart Traffic Analytics System developed using Python, OpenCV, YOLOv8, and Firebase. The system performs real-time lane detection, vehicle detection, vehicle tracking, traffic density classification, lane departure warning generation, and cloud-based traffic analytics. It processes road video streams, monitors traffic conditions, tracks vehicles using unique IDs, measures processing performance through FPS monitoring, and uploads traffic statistics to Firebase Realtime Database for cloud storage and analysis.

## 🎯 Problem Statement

Traditional traffic monitoring systems often require expensive infrastructure, manual observation, and limited real-time analytics. This project provides an intelligent, cost-effective traffic monitoring solution capable of detecting lane boundaries, tracking vehicles, classifying traffic density, generating lane departure warnings, and storing traffic analytics in the cloud using Computer Vision, Artificial Intelligence, and Firebase technologies.


## ✨ Features

* Real-time Lane Detection
* Region of Interest (ROI) Masking
* Canny Edge Detection
* Hough Line Transform
* Lane Area Highlighting
* YOLOv8 Vehicle Detection
* Vehicle Tracking
* Vehicle Counting
* Traffic Density Classification
* Lane Departure Warning System
* FPS Monitoring
* Firebase Realtime Database Integration
* Cloud-Based Traffic Analytics
* Video Processing and Visualization

## 🛠️ Technologies Used

* Python
* OpenCV
* NumPy
* YOLOv8 (Ultralytics)
* Firebase Realtime Database
* Firebase Admin SDK
* Computer Vision
* Firebase Realtime Database
* Firebase Admin SDK

## 📂 Project Structure

```text
smart-traffic-analytics-system/
├── assets/
│   ├── output_demo.png
│   └── firebase_dashboard.png
├── outputs/
├── src/
│   ├── lane_detector.py
│   ├── vehicle_detector.py
│   ├── cloud_logger.py
│   ├── utils.py
│   └── pipeline.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🔄 System Workflow

1. Read video frames using OpenCV.
2. Detect lane boundaries using image processing techniques.
3. Detect and classify vehicles using YOLOv8.
4. Track vehicles using unique IDs.
5. Count vehicles in real time.
6. Classify traffic density as Low, Medium, or High.
7. Generate lane departure warnings.
8. Calculate real-time FPS.
9. Upload traffic statistics to Firebase Realtime Database.
10. Display processed output video with analytics overlays.


## 📋 Output Information

The system displays:

* Lane Area Detection
* Vehicle Bounding Boxes
* Vehicle IDs (Tracking)
* Vehicle Count
* Traffic Density (Low / Medium / High)
* Lane Departure Warning
* FPS Value
* Cloud Logged Traffic Data

## ☁️ Firebase Cloud Analytics

Traffic analytics data is uploaded to Firebase Realtime Database every 5 seconds to balance real-time monitoring and processing performance.

Stored fields:

* Vehicle Count
* FPS
* Timestamp

The collected data can be used for traffic monitoring, traffic density analysis, and cloud-based analytics applications.

Example:

Vehicle Count: 4

FPS: 4.22

Timestamp: 2026-06-07 11:32:07

## 🏆 Key Achievements

✔ Real-time lane detection using OpenCV

✔ Vehicle detection using YOLOv8

✔ Vehicle tracking and counting

✔ Traffic density classification

✔ Lane departure warning system

✔ FPS monitoring for performance analysis

✔ Cloud-based traffic analytics using Firebase

✔ Automated traffic data logging with timestamps

## 🚀 Future Enhancements

* Vehicle Speed Estimation
* Distance Estimation
* DeepSORT / ByteTrack Integration
* Collision Warning System
* Curved Lane Detection
* ADAS Dashboard
* Cloud Analytics Dashboard
* Real-Time Camera Integration

## 📈 Results

The Smart Traffic Analytics System successfully:

- Detects and highlights road lanes
- Detects and tracks vehicles using YOLOv8
- Assigns unique IDs to vehicles
- Counts vehicles in real time
- Classifies traffic density as Low, Medium, or High
- Generates lane departure warnings
- Calculates processing FPS
- Uploads traffic analytics to Firebase Realtime Database
- Provides a foundation for future ADAS applications

## 📸 Screenshots

### Lane and Vehicle Detection

![Lane Detection Output](assets/output_demo.png)

### Firebase Cloud Analytics

![Firebase Dashboard](assets/firebase_dashboard.png)

## 👩‍💻 Author

**Shwethashree S**

B.Tech – Information Science and Engineering  
Presidency University, Bangalore