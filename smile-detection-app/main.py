import cv2
import os
import time

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load Haar Cascade classifiers with absolute paths
face_cascade = cv2.CascadeClassifier(os.path.join(current_dir, 'haarcascade_frontalface_default.xml'))
smile_cascade = cv2.CascadeClassifier(os.path.join(current_dir, 'haarcascade_smile.xml'))

# Verify that the cascade files were loaded correctly
if face_cascade.empty():
    print("Error: Could not load face cascade classifier")
    exit()
if smile_cascade.empty():
    print("Error: Could not load smile cascade classifier")
    exit()

print("Starting webcam...")
# Try different camera indices
for i in range(3):  # Try first 3 camera indices
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Successfully opened camera {i}")
        break
    cap.release()

if not cap.isOpened():
    print("Error: Could not open any camera")
    exit()

# Set camera properties for better performance
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame. Retrying...")
        time.sleep(0.1)  # Wait a bit before retrying
        continue

    # Convert to grayscale (for detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Region of interest for smile detection
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Adjust smile detection parameters
        smiles = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.7,
            minNeighbors=15,
            minSize=(25, 25)
        )

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)

    # Show the frame
    cv2.imshow('Smile Detector 😄', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
