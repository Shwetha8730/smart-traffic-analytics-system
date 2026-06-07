import cv2
import numpy as np

def region_of_interest(image):
    height, width = image.shape[:2]

    polygon = np.array([[
        (int(width * 0.25), height),
        (int(width * 0.75), height),
        (int(width * 0.58), int(height * 0.60)),
        (int(width * 0.42), int(height * 0.60))
    ]])

    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygon, 255)

    return cv2.bitwise_and(image, mask)

def make_line(image, line_params):
    if line_params is None:
        return None
    slope, intercept = line_params
    height = image.shape[0]
    y1 = height
    y2 = int(height * 0.60)
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])

def average_lines(image, lines):
    left, right = [], []
    height, width = image.shape[:2]
    if lines is None:
        return None, None
    for line in lines:
        x1, y1, x2, y2 = line[0]
        if x2 == x1:
            continue
        slope = (y2 - y1) / (x2 - x1)
        intercept = y1 - slope * x1
        length = np.sqrt((y2-y1)**2 + (x2-x1)**2)
        mid_x = (x1 + x2) / 2
        if slope < -0.3 and mid_x < width * 0.50:
            left.append((slope, intercept, length))
        elif slope > 0.3 and mid_x > width * 0.50:
            right.append((slope, intercept, length))
    left_line, right_line = None, None
    if left:
        total = sum(l[2] for l in left)
        s = sum(l[0]*l[2] for l in left) / total
        i = sum(l[1]*l[2] for l in left) / total
        left_line = make_line(image, (s, i))
    if right:
        total = sum(l[2] for l in right)
        s = sum(l[0]*l[2] for l in right) / total
        i = sum(l[1]*l[2] for l in right) / total
        right_line = make_line(image, (s, i))
    return left_line, right_line

def draw_lanes(frame, left_line, right_line):
    overlay = np.zeros_like(frame)
    if left_line is not None:
        x1, y1, x2, y2 = left_line
        cv2.line(overlay, (x1,y1), (x2,y2), (0,255,0), 8)
    if right_line is not None:
        x1, y1, x2, y2 = right_line
        cv2.line(overlay, (x1,y1), (x2,y2), (0,255,0), 8)
    return cv2.addWeighted(frame, 0.8, overlay, 1, 0)
