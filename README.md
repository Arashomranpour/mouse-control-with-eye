<div align="center">

# 👁️ Eye-Controlled Mouse

**Move the cursor with your eyes and click by blinking - using a webcam, MediaPipe Face Mesh and PyAutoGUI.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0097A7?logo=google&logoColor=white)

</div>

---

## ✨ How it works

- 📷 Reads webcam frames and runs **MediaPipe Face Mesh** with refined (iris) landmarks.
- 👀 The iris landmarks are mapped to screen coordinates, and `pyautogui` moves the cursor accordingly.
- 😉 When the distance between the upper and lower eyelid landmarks of one eye drops below a threshold (a blink / wink), a **mouse click** is triggered.
- Press **Q** to quit.

## 🚀 Getting Started

```bash
git clone https://github.com/Arashomranpour/mouse-control-with-eye.git
cd mouse-control-with-eye
pip install opencv-python mediapipe pyautogui
python mouse.py
```

> 💡 Sit in good light and keep your face centered. The blink threshold and cursor scaling in `mouse.py` can be tuned for your camera.

## 📁 Project Structure

```
.
└── mouse.py     # Face-mesh tracking, cursor movement, blink-to-click
```

## 🛠️ Tech Stack

`OpenCV` · `MediaPipe` · `PyAutoGUI`
