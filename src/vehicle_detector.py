import cv2
from ultralytics import YOLO
import math

model = YOLO("yolov8n.pt")

vehicle_id = 0
tracked_objects = {}


def detect_vehicles(frame):

    global vehicle_id
    global tracked_objects

    results = model(frame, verbose=False, conf=0.5)

    vehicle_count = 0

    new_tracked = {}

    for result in results:

        for box in result.boxes:

            confidence = float(box.conf[0])
            cls = int(box.cls[0])

            if cls in [2, 3, 5, 7]:

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2

                current_id = None

                for obj_id, (px, py) in tracked_objects.items():

                    distance = math.hypot(cx - px, cy - py)

                    if distance < 50:
                        current_id = obj_id
                        break

                if current_id is None:
                    vehicle_id += 1
                    current_id = vehicle_id

                new_tracked[current_id] = (cx, cy)

                vehicle_count += 1

                label = f"ID {current_id} | {model.names[cls]}"

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 0, 255),
                    2
                )

                cv2.putText(
                    frame,
                    label,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 0, 255),
                    2
                )

    tracked_objects = new_tracked

    return frame, vehicle_count