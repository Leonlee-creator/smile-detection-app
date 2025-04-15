# 😄 Smile Detection App

This is a Python app that uses your **computer’s webcam** to detect **faces and smiles** in real-time.

---

## 💡 How It Works

- The code uses **OpenCV** to access your webcam and process the video feed live.
- It uses two **pre-trained Haar Cascade classifiers**:
  - `haarcascade_frontalface_default.xml` — for face detection
  - `haarcascade_smile.xml` — for smile detection
- When a face is detected, a **blue rectangle** is drawn.
- When a smile is detected inside the face, a **green rectangle** is drawn.

🟢 You can press `q` anytime to close the camera window.

---

## 🛠️ Technologies Used

- Python
- OpenCV
- Haar Cascade Classifiers (from OpenCV GitHub)

---

## 🚀 How to Run It

1. Make sure you have Python and OpenCV installed:

```bash
pip install opencv-python
