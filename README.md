# 😄 Smile Detection App

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.11-green)](https://opencv.org/)
![Status](https://img.shields.io/badge/Project-Live-brightgreen)

This is a **real-time smile detection app** built with Python and OpenCV. It uses your **webcam** to detect **faces and smiles** using pre-trained machine learning models.

---

## 💡 How It Works

- Uses your **webcam** to capture live video
- Detects **faces** using `haarcascade_frontalface_default.xml`
- Detects **smiles** using `haarcascade_smile.xml`
- Draws:
  - 🟦 Blue rectangle around faces
  - 🟩 Green rectangle around smiles

---

## 🛠️ Technologies Used

- 🐍 Python 3.10+
- 🧠 OpenCV 4.11
- 📦 Haar Cascade Classifiers (from OpenCV GitHub)

---

## 🚀 How to Run It

1. Install the required library:

```bash
pip install opencv-python
