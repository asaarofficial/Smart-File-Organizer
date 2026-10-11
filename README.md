# Smart File Organizer 📂

A Python automation script that instantly cleans up messy directories by sorting files into categorized sub-folders based on their extensions. 

## Features
- **Automated Sorting:** Detects file types (like `.pdf`, `.jpeg`, `.csv`) and generates corresponding folders on the fly.
- **macOS Optimized:** Safely ignores hidden system files (like `.DS_Store`) to prevent clutter.
- **Self-Preserving:** The script excludes itself from the sorting process so it stays exactly where you left it.
- **Zero Dependencies:** Built entirely with Python's standard `os` and `shutil` libraries. No extra downloads required.

## How to Use
1. Drop `organizer.py` into the messy folder you want to clean up.
2. Open your terminal and navigate to that folder.
3. Run the following command:
   ```bash
   python3 organizer.py
   ```
