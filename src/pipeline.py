import cv2
import sys
import os
import time

sys.path.insert(0, os.path.dirname(__file__))

from cloud_logger import upload_data
from lane_detector import detect_lanes
from vehicle_detector import detect_vehicles

def process_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    prev_time = time.time()
    last_upload = time.time()

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        frame = detect_lanes(frame)
        frame, vehicle_count = detect_vehicles(frame)

        curr_time = time.time()
        fps_value = 1 / (curr_time - prev_time)
        prev_time = curr_time

        if curr_time - last_upload >= 1:
            upload_data(vehicle_count, fps_value)
            last_upload = curr_time

        cv2.putText(frame, f"Vehicles: {vehicle_count}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.putText(frame, f"FPS: {int(fps_value)}", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        out.write(frame)

        cv2.imshow("Lane + Vehicle Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"Output saved to {output_path}")


if __name__ == "__main__":
    os.makedirs("outputs", exist_ok=True)

    process_video("assets/test_video.mp4", "outputs/demo_output.mp4")