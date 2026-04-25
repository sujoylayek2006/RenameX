# 🔄 RenameX — Bulk File Extension Renamer

RenameX is a lightweight, dependency-free Python utility designed for seamless bulk extension swapping. Featuring built-in folder validation, automatic prefix handling, and detailed execution logs, it simplifies file management tasks for developers and students alike.
---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example](#example)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [License](#license)

---

## About

**RenameX** is a simple but handy Python CLI tool that lets you bulk-rename files in any folder by swapping their file extension. Instead of manually renaming files one by one, just run the script, enter your folder path and the two extensions, and the tool handles the rest.

---

## ✨ Features

- 🎨 Displays a styled **ASCII banner** on startup with tool info
- 📁 Supports any folder path (or defaults to the current directory)
- 🔁 Renames all matching files in a single run
- ✅ Auto-adds the `.` prefix to extensions if you forget it
- 🛡️ Validates the folder path before doing anything
- 📊 Shows a clear summary of renamed files and a final count
- ⚠️ Gracefully reports any files that couldn't be renamed

---

## Requirements

- Python **3.6+**
- No external libraries required — uses only the built-in `os` module

---

## 🚀 Usage

1. **Clone or download** this repository.

2. **Run the script** from your terminal:

   ```bash
   python src/main.py
   ```

3. **The banner will appear, then follow the prompts:**

   ```
   ================================================================
       ____                                 _  __
      / __ \___  ____  ____ _____ ___  ____| |/ /
     / /_/ / _ \/ __ \/ __ `/ __ `__ \/ _ \   /
    / _, _/  __/ / / / /_/ / / / / / /  __/   |
   /_/ |_|\___/_/ /_/\__,_/_/ /_/ /_/\___/_/|_|

   ================================================================
   [*] Tool        : RenameX - File Extension Changer
   [*] Version     : 1.0
   [*] Developer   : SUJOY LAYEK
   [*] Description : Fast and secure bulk file extension modifier.
   ================================================================

   Enter folder path (press Enter for current directory):
   Enter source extension (e.g. .txt):
   Enter target extension (e.g. .md):
   ```

> **Tip:** You can press **Enter** at the folder path prompt to use the directory where the script is located.

---

## 💡 Example

**Scenario:** You have a folder `C:\Users\John\Documents\notes` full of `.txt` files and want to convert them all to `.md`.

```
Enter folder path (press Enter for current directory): C:\Users\John\Documents\notes
Enter source extension (e.g. .txt): .txt
Enter target extension (e.g. .md): .md

Renaming '.txt' -> '.md' in: C:\Users\John\Documents\notes

  Renamed: todo.txt  ->  todo.md
  Renamed: ideas.txt  ->  ideas.md
  Renamed: summary.txt  ->  summary.md

Done! 3 file(s) renamed.
```

---

## ⚙️ How It Works

1. The script starts and **displays the RenameX ASCII banner** with tool metadata.
2. The user enters a **folder path**, a **source extension**, and a **target extension**.
3. The script validates that the folder exists.
4. It iterates through all files in the folder and finds every file whose name ends with the source extension.
5. Each matching file is renamed by replacing the old extension with the new one using `os.rename()`.
6. Errors (e.g., permission issues) are caught and reported without stopping the rest of the process.
7. A final count of successfully renamed files is displayed.

---

## 📂 Project Structure

```

RenameX/
│── src/
│   └── main.py                   # Main RenameX script
│── examples/
│   └── EXAMPLES.md               # Example usage walkthrough
│── README.md                     # This file
│── LICENSE                       # License file
└── requirements.txt              # Dependency info (none required)
```

---

## 📄 License

This project is open-source and free to use for personal or educational purposes.
This project is licensed under the [MIT License](https://github.com/sujoylayek2006/RenameX?tab=MIT-1-ov-file#).

---

> Made with ❤️ by **SUJOY LAYEK** using Python

