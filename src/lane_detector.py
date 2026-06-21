import cv2
import numpy as np
from utils import region_of_interest, average_lines

def detect_lanes(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blur, 50, 150)
    masked_edges = region_of_interest(edges)

    lines = cv2.HoughLinesP(masked_edges, 1, np.pi/180, 15,
                            minLineLength=20,
                            maxLineGap=250)

    left_line, right_line = average_lines(frame, lines)

    overlay = np.zeros_like(frame)

    if left_line is not None:
        x1, y1, x2, y2 = left_line
        cv2.line(overlay, (x1, y1), (x2, y2), (0, 255, 0), 8)

    if right_line is not None:
        x1, y1, x2, y2 = right_line
        cv2.line(overlay, (x1, y1), (x2, y2), (0, 255, 0), 8)

    if left_line is not None and right_line is not None:
        lane_area = np.array([
            [left_line[0], left_line[1]],
            [left_line[2], left_line[3]],
            [right_line[2], right_line[3]],
            [right_line[0], right_line[1]]
        ], dtype=np.int32)

        cv2.fillPoly(overlay, [lane_area], (0, 255, 0))

    result = cv2.addWeighted(frame, 0.7, overlay, 0.5, 0)

    return result, left_line, right_line