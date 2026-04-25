# 🔄 RenameX — Bulk File Extension Renamer

RenameX is a lightweight, dependency-free Python utility designed for seamless bulk extension swapping. Featuring built-in folder validation, automatic prefix handling, and detailed execution logs, it simplifies file management tasks for developers and students alike.
---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [Installation & Setup](#️-installation--setup)
- [Usage](#usage)
- [Example](#example)
- [Use Cases](#-use-cases)
- [How It Works](#️-how-it-works)
- [Project Structure](#-project-structure)
- [Important Notes](#️-important-notes)
- [Contributing](#-contributing)
- [Show Your Support](#-show-your-support)
- [License](#-license)

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

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sujoylayek2006/RenameX.git
cd RenameX
```

### 2️⃣ Run the Script

No installation or pip packages needed — just run it directly with Python:

```bash
python src/main.py
```

> **Requires:** Python 3.6 or higher. No third-party dependencies.

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

## 🗂️ Use Cases

RenameX is perfect for a wide range of practical scenarios:

| Scenario | Example |
|---|---|
| **Convert notes format** | Rename all `.txt` files to `.md` for Markdown editors |
| **Batch photo renaming** | Change `.jpeg` files to `.jpg` for consistency |
| **Web asset migration** | Rename `.html` files to `.htm` for legacy server support |
| **Data file conversion** | Switch `.csv` files to `.tsv` after a format change |
| **Script file prep** | Rename `.py` files to `.pyw` for Windows GUI scripts |
| **Log file management** | Convert `.log` files to `.txt` for easier reading |

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
│── examples/                     # Example usage walkthrough
│   │── 1.Before_the_using_RenameX.png
│   │── 2.Terminal_view_before.png
│   │── 3.Terminal_view_after.png
│   │── 4.After_the_using_RenameX.png
│   └── EXAMPLES.md               
│── README.md                     # This file
│── LICENSE                       # License file
└── requirements.txt              # Dependency info (none required)
```

---

## ⚠️ Important Notes

> [!WARNING]
> **Always backup important files before running RenameX.** Extension renaming modifies files in place and cannot be automatically undone.

- 📁 **Ensure the correct folder path is provided** — an invalid path will halt the script before any changes are made.
- 🧪 **Test on sample files first** — create a test folder with dummy files and do a dry run before applying to real data.
- 🔡 Extensions are **case-sensitive** on some systems (e.g., `.TXT` ≠ `.txt` on Linux/macOS).
- 🚫 The script only renames files in the **top-level folder** — it does not recurse into subfolders.

---

## 🤝 Contributing

Contributions are welcome and appreciated! Here's how you can help:

1. **Fork** the repository
2. **Create a new branch** for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** and commit them with a clear message:
   ```bash
   git commit -m "feat: add your feature description"
   ```
4. **Push** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request** — describe what you changed and why.

Please make sure your code follows the existing style and is well-commented.

---

## ⭐ Show Your Support

If **RenameX** saved you time or helped you learn something new, consider showing your support:

- ⭐ **Star** this repository on GitHub
- 🍴 **Fork** it and build something cool on top of it
- 🐛 **Report bugs** or suggest features via [Issues](https://github.com/sujoylayek2006/RenameX/issues)
- 📣 **Share** it with friends or classmates who might find it useful

Every bit of support motivates further development — thank you! 🙏

---

## 📄 License

This project is open-source and free to use for personal or educational purposes.
This project is licensed under the [MIT License](https://github.com/sujoylayek2006/RenameX?tab=MIT-1-ov-file#).

---

> Made with ❤️ by **SUJOY LAYEK** using Python

