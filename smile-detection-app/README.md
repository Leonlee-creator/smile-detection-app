# 😄 Smile Detection App

This is a Python app that uses your **computer’s webcam** to detect **faces and smiles** in real-time.

---

## 💡 How It Works

- Uses **OpenCV** to access your webcam and process the video.
- Two pre-trained Haar Cascade classifiers:
  - `haarcascade_frontalface_default.xml` — face detection
  - `haarcascade_smile.xml` — smile detection
- **Blue rectangle** = face detected
- **Green rectangle** = smile detected
- Press `q` to quit

---

## 🛠️ Technologies Used

- Python
- OpenCV
- Haar Cascade Classifiers (OpenCV GitHub)

---

## 🚀 How to Run It

```bash
pip install opencv-python
python main.py

