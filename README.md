# 📏 Object Measurement Tool (using A4 Paper as Reference)

A simple Python + OpenCV + Flask-based web app that measures real-world objects placed on an A4 sheet. Just upload a photo, and the tool detects the object and returns its width, height, and area in millimeters.

---

## ⚙️ How It Works

1. You place an object on an A4 sheet (210mm x 297mm).
2. Upload the image to the app.
3. The app:
   - Detects the A4 as a reference.
   - Warps the perspective to a top-down view.
   - Extracts the object and measures its bounding box.
4. Displays the results + annotated image.

---

## 🧰 Tech Stack & Libraries

- **Python**
- **OpenCV** – image processing & computer vision
- **NumPy** – matrix math
- **Flask** – web framework
- **Werkzeug** – secure file handling


