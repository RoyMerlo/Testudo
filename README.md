![20250504_0436_Testudo_ Metadata Cleaner_simple_compose_01jtcjbq4gfmba9qj3cfng7h1g](https://github.com/user-attachments/assets/a95c2b4c-1f22-4d18-80fc-3247aad0db6e)
![pis](https://github.com/user-attachments/assets/7bd00cd3-aa95-4ea6-bfa2-f9e7e9cf333f)

# ⚡ TESTUDO - Metadata Cleaner

**TESTUDO** is a professional and modern GUI-based metadata cleaner for any file type (images, videos, documents, etc.).  
It uses `exiftool` under the hood to **securely remove all metadata** from a file and offers a clean sharing feature after sanitization.

![screenshot](https://your-screenshot-url.com/preview.png) <!-- Replace with your screenshot URL -->

---

## 🔐 Features

- 🔎 View original file metadata before deletion
- 🧼 One-click metadata removal using `exiftool`
- 📤 Optional secure sharing after cleaning
- 💻 Cross-platform GUI (built with Python & Tkinter)
- 💡 Modern and sci-fi-inspired interface
- 🪪 Supports any file format (video, image, Office, PDF, RAW, etc.)
- 🛡️ No internet required — 100% local processing

---

## 📦 Installation

### Requirements

- Python 3.7+
- `exiftool` installed and available in system path  
  **On Linux (Debian/Ubuntu):**
  ```bash
  sudo apt install libimage-exiftool-perl
pip install -r requirements.txt
🚀 Run the App
bash
Copy
Edit
python testudo.py
The app will launch a graphical interface.

📷 Screenshot

🛠️ How It Works
Select any file using the file dialog.

View its current metadata.

Confirm to delete it.

The metadata is permanently removed using:

bash
Copy
Edit
exiftool -all= yourfile.ext
Optionally, share the cleaned file to another folder.

🔐 Why Use TESTUDO?
Most files you send online (PDFs, photos, videos) contain hidden metadata, such as:

Your device info

GPS coordinates

Creation software

Time and date stamps

TESTUDO protects your privacy and removes these traces in one click.

🧪 Compatibility
✅ Linux (tested on Ubuntu)

✅ Windows (with exiftool installed)

✅ macOS (via Homebrew install of exiftool)

📁 Portable / AppImage (Linux)
To create a standalone .AppImage version:

bash
Copy
Edit
chmod +x testudo.py
./build-appimage.sh
We will include the build-appimage.sh script soon.

👨‍💻 Author
Developed by Roy Merlo
© 2025 – All rights reserved


  
