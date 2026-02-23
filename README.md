# Personal-Search-Engine
DAY - 39/100 Project - python X Personal Search Engine

# 🔎 Personal Search Engine (Multi-Browser Smart Dashboard)

A desktop search dashboard built using **Python + Tkinter** that allows you to search across multiple platforms and choose which browser to open results in.

---

## 🚀 Features

- 🔍 Google Search
- 🎥 YouTube Search
- 💻 GitHub Repository Search
- 🌐 Bing Search
- 📘 Wikipedia Search
- 📘 Facebook Search
- 📸 Instagram Profile Opener
- 🧹 Clear Input Button
- 🌍 Browser Selector (Default / Edge / Chrome)
- 🖼️ Custom Icon-Based Buttons
- 🧠 Centralized Browser Control Logic

---

## 🧩 How It Works

1. Enter your search query.
2. Select a browser from the dropdown.
3. Click the platform icon.
4. The selected browser opens the result.

All URLs are generated dynamically and routed through a centralized `open_browser()` function.

---

## 📁 Project Structure

Your project must follow this structure:

    Personal-Search-Engine/
    │
    ├── 39_PERSONAL_SEARCH_ENGINE.py
    └── icons/
        ├── GOOGLE.png
        ├── YOUTUBE.png
        ├── FACEBOOK.png
        ├── INSTAGRAM.png
        ├── BING.png
        ├── GITHUB.png
        └── WIKIPEDIA.png

---

## ⚠️ Fixing FileNotFoundError

If you see:

    FileNotFoundError: No such file or directory

It means your image paths are incorrect.

### ❌ Wrong Way (Hardcoded Absolute Path)

    Dir_Base_Path = r"E:\Documents_Files\RobinData\PYTHON\RawDataofpng"

This only works on your computer.

---

### ✅ Correct Way (Portable & GitHub Safe)

Use a relative path:

    Dir_Base_Path = os.path.join(os.path.dirname(__file__), "icons")

Why this works:

- Automatically detects project folder
- Works after cloning from GitHub
- No hardcoded system paths
- Portable across machines

---

## 🖥️ Browser Support

The app supports:

- Default System Browser
- Microsoft Edge
- Google Chrome

Typical executable paths (Windows):

Edge:
    C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe

Chrome:
    C:\Program Files\Google\Chrome\Application\chrome.exe

Make sure these paths exist on your system.

---

## ▶️ How To Run

1. Install Python (3.10+ recommended).
2. Clone or download this repository.
3. Ensure the `icons` folder exists with all images.
4. Run:

    python 39_PERSONAL_SEARCH_ENGINE.py

---

## 🛠 Requirements

- Python 3.x
- Tkinter (included with Python)
- Windows OS (for browser executable control)

---

## 🏆 Project Overview

This project demonstrates:

- Tkinter GUI layout management
- Image-based button controls
- Dynamic URL construction
- Centralized browser handling
- Multi-browser execution logic
- Debugging real-world errors (AttributeError, FileNotFoundError)
- Clean GitHub-ready project structuring

---

## 👨‍💻 Author

Eobin Gupta

Built as part of a 100 Days of Code journey.

First fully structured multi-platform desktop application developed primarily through guided hints and hands-on debugging.

---

⭐ If you find this project useful, feel free to fork or star the repository.
