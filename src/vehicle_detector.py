import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_vehicles(frame):
    results = model(frame, verbose=False)

    vehicle_count = 0

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])

            if cls in [2, 3, 5, 7]:  # car, motorcycle, bus, truck
                vehicle_count += 1

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                label = model.names[cls]

                cv2.rectangle(frame, (x1, y1), (x2, y2),
                              (0, 0, 255), 2)

                cv2.putText(frame,
                            label,
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5,
                            (0, 0, 255),
                            2)

    return frame, vehicle_count