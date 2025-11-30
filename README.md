# File Organizer WIP  

**Automatically organize files in a folder by extension — no more messy downloads folder!**

## What It Does  
- Scans a specified directory for all files  
- Checks each file’s extension (e.g. `.jpg`, `.pdf`, `.mp3`, `.py`, etc.)  
- Moves files into subfolders named by file type (e.g. `jpg/`, `webp/`, `pdf/`, `py/`, `Others/`)  
- Skips over folders to avoid mis-sorting directories  
- Works on **Windows, macOS, and Linux**  

## Why I Built It  
I got tired of manually sorting a messy Downloads folder after long coding sessions or media downloads. This simple tool saves time, keeps things tidy, and automates a boring repetitive chore — while giving me practice in scripting and file operations with Python.  

## How to Use  

```bash
# Clone the repo  
git clone https://github.com/YourUsername/FileOrganizer.git  
cd FileOrganizer  

# Run the script with the path to the folder you want organized  
python organizer.py "/path/to/your/folder"
```

> Make sure you point to the **correct folder** — files will be moved.  

##  What Folder Structure Looks Like  
```
FileOrganizer/
├── webps/
├── png/
├── pdf/
├── py/
└── Others/
```

##  What I Learned / Challenges Solved  
- Using Python’s `os` and `shutil` libraries for file and folder management  
- Handling edge cases (files with no extension, hidden files, permissions, etc.)  
- Writing code that works across operating systems  
- Building a practical script, not just a toy project  

## Future Improvements (Roadmap)  
- Add a simple GUI for non-coders (so you don’t need the terminal)  
- Allow a config file for custom folder names / rules  
- Add logging / Undo support (in case files are moved in error)  
- Package as an installable tool (`pip install file-organizer`)  

## License & Contact  
MIT License — feel free to use and adapt.  
Created by Julia Shannon. Reach me at: juliarshan@gmail.com  

