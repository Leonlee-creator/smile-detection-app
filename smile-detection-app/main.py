import cv2
import os
import time
from datetime import datetime

# Load classifiers
current_dir = os.path.dirname(os.path.abspath(__file__))
face_cascade = cv2.CascadeClassifier(os.path.join(current_dir, 'haarcascade_frontalface_default.xml'))
smile_cascade = cv2.CascadeClassifier(os.path.join(current_dir, 'haarcascade_smile.xml'))

if face_cascade.empty() or smile_cascade.empty():
    print("Error loading classifiers")
    exit()

# Webcam setup
print("Starting webcam...")
for i in range(3):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera {i} opened.")
        break
    cap.release()

if not cap.isOpened():
    print("No camera found.")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

smile_count = 0
last_smile_time = ""

# Helper function to draw text with background
def draw_text_with_bg(img, text, pos, text_color=(255,255,255), bg_color=(0,0,0)):
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 0.6
    thickness = 2
    (text_w, text_h), _ = cv2.getTextSize(text, font, scale, thickness)
    x, y = pos
    cv2.rectangle(img, (x, y - text_h - 8), (x + text_w + 10, y + 5), bg_color, -1)
    cv2.putText(img, text, (x + 5, y - 5), font, scale, text_color, thickness)

# Loop
while True:
    ret, frame = cap.read()
    if not ret:
        time.sleep(0.1)
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        center = (x + w//2, y + h//2)
        radius = w // 2
        cv2.circle(frame, center, radius, (255, 0, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 15, minSize=(25, 25))

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)

            confidence = min(int((sw / w) * 100), 100)
            label = f"{confidence}% Smile"
            draw_text_with_bg(roi_color, label, (sx, sy))

            smile_count += 1
            last_smile_time = datetime.now().strftime('%H:%M:%S')
            break  # Only one smile per face

    # Display smile stats
    draw_text_with_bg(frame, f"Smiles: {smile_count}", (10, 30), (0, 255, 255), (50, 50, 50))
    if last_smile_time:
        draw_text_with_bg(frame, f"Last smile: {last_smile_time}", (10, 60), (0, 255, 255), (50, 50, 50))

    # Add your name
    draw_text_with_bg(frame, "Leon Taderera 😎", (430, 470), (200, 200, 255), (30, 30, 30))

    cv2.imshow('😄 Smile Detector - Press Q to Quit', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
