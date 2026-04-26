# 🔄 RenameX — Bulk File Extension Renamer

RenameX is a lightweight, dependency-free Python CLI tool that lets you bulk-rename files in any folder by swapping their file extension — fast, simple, and safe.

---

## 📋 Table of Contents

- [About](#-about)
- [Preview](#️-preview)
- [Features](#✨-features)
- [Installation & Setup](#️-installation--setup)
- [How To Use](#-how-to-use)
- [How It Works](#️-how-it-works)
- [Use Cases](#️-use-cases)
- [Project Structure](#-project-structure)
- [Important Notes](#️-important-notes)
- [Contributing](#-contributing)
- [Show Your Support](#-show-your-support)
- [License](#-license)

---

## 📌 About

**RenameX** is a simple but powerful Python CLI tool that lets you bulk-rename files in any folder by swapping their file extension. Instead of manually renaming files one by one, just run the script, enter your folder path and the two extensions — and the tool handles the rest instantly.

---

## 🖥️ Preview

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
```

---

## ✨ Features

| Feature | Details |
|---|---|
| 🎨 ASCII banner | Styled terminal banner displayed on startup |
| 📁 Any folder supported | Use any path, or press Enter to use the current directory |
| 🔍 Dry-run preview | Shows you exactly what will be renamed **before** touching any files |
| ✅ Confirmation prompt | You must type `y` to confirm — nothing renames by accident |
| 🔁 Bulk renaming | Renames all matching files in a single confirmed run |
| ✅ Auto dot correction | Type `txt` — it auto-corrects to `.txt` and tells you |
| 🛡️ Input validation | Re-asks for input if an extension is left blank |
| 🛡️ Folder validation | Validates the path before scanning or changing anything |
| 🚫 Duplicate guard | Skips files where the renamed target already exists |
| 🔁 Same-extension guard | Detects if source and target are identical — exits early |
| 📊 Rename summary | Shows `[OK]` / `[Skip]` / `[Error]` for each file + final count |
| ⚠️ Safe error handling | Catches permission errors without stopping the rest of the process |
| ⌨️ Ctrl+C support | Press Ctrl+C at any time to exit cleanly — no scary traceback |
| ✅ No dependencies | Uses only Python's built-in `os` module |

---

## ⚙️ Installation & Setup

### Requirements

- Python **3.6** or higher
- No external libraries required — uses only the built-in `os` module

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/sujoylayek2006/RenameX.git
cd RenameX
```

**2. Run the script**
```bash
python src/main.py
```

> No `pip install` needed — this tool uses only Python's built-in libraries!

---

## 🧭 How To Use

### Step 1 — Clone or download this repository

```bash
git clone https://github.com/sujoylayek2006/RenameX.git
cd RenameX
```

### Step 2 — Run the script

```bash
python src/main.py
```

### Step 3 — Enter the folder path

```
Step 1 of 3 — Folder
  Enter the full path to the folder you want to work in.
  Press Enter to use the CURRENT directory.

  Folder path: C:\Users\Sujoy\Documents\notes
```

> Press **Enter** to use the current directory — the full resolved path is printed so you always know where you are.

### Step 4 — Enter the source extension

```
Step 2 of 3 — Source Extension
  This is the extension your files currently have.

Enter source extension (e.g. .txt): txt
  [+] Auto-corrected to: '.txt'
```

> If you forget the dot, it is auto-added and shown to you — `txt` becomes `.txt`.

### Step 5 — Enter the target extension

```
Step 3 of 3 — Target Extension
  This is the extension you want to rename your files TO.

Enter target extension (e.g. .txt): md
  [+] Auto-corrected to: '.md'
```

### Step 6 — Review the preview and confirm

```
  Scanning 'C:\Users\Sujoy\Documents\notes' for '.txt' files...

  Preview — 3 file(s) will be renamed:

    todo.txt    ->  todo.md
    ideas.txt   ->  ideas.md
    summary.txt ->  summary.md

  Proceed with renaming? (y/n): y
```

> You see every rename **before** it happens. Type `y` to proceed or `n` to cancel safely.

### Step 7 — Watch the results!

```
  [OK]    todo.txt    ->  todo.md
  [OK]    ideas.txt   ->  ideas.md
  [OK]    summary.txt ->  summary.md

  Done!  3 renamed
```

---

## ⚙️ How It Works

1. The script starts and **displays the RenameX ASCII banner** with tool metadata.
2. The user is guided through **3 numbered steps**: folder path → source extension → target extension.
3. At each step, **input is validated** — empty extensions are rejected, missing dots are auto-added.
4. If source and target extensions are the same, the script **exits early** with a clear message.
5. The script **validates that the folder exists** — if not, it stops safely with a helpful hint.
6. It **scans the folder** and builds a list of all files matching the source extension.
7. A **dry-run preview** shows every planned rename before any file is touched.
8. The user **confirms with `y`** — typing anything else cancels cleanly with no changes made.
9. Each file is renamed using `os.rename()`. If a target filename already exists, that file is **skipped**.
10. Errors (e.g. permission issues) are **caught and reported** per-file without stopping the rest.
11. A **final summary** shows counts of renamed, skipped, and failed files.

---

## 🗂️ Use Cases

| Scenario | Example |
|---|---|
| 📝 **Convert notes format** | Rename all `.txt` files to `.md` for Markdown editors |
| 🖼️ **Batch photo renaming** | Change `.jpeg` files to `.jpg` for consistency |
| 🌐 **Web asset migration** | Rename `.html` files to `.htm` for legacy server support |
| 📊 **Data file conversion** | Switch `.csv` files to `.tsv` after a format change |
| 🐍 **Script file prep** | Rename `.py` files to `.pyw` for Windows GUI scripts |
| 🗂️ **Log file management** | Convert `.log` files to `.txt` for easier reading |

---

## 📂 Project Structure

```
RenameX/
├── src/
│   └── main.py               # Main RenameX script
├── examples/                 # Example usage walkthrough
│   ├── 1.Before_RenameX.png
│   ├── 2.Terminal_before.png
│   ├── 3.Terminal_after.png
│   ├── 4.After_RenameX.png
│   └── EXAMPLES.md
├── .gitignore                # Git repository settings
├── README.md                 # This file
├── LICENSE                   # License file
└── requirements.txt          # Dependency info (none required)
```

---

## ⚠️ Important Notes

> [!WARNING]
> **Always backup important files before running RenameX.** Extension renaming modifies files in place and cannot be automatically undone.

- 🔍 **Preview before you commit** — RenameX always shows a dry-run preview and asks for confirmation before touching any files.
- 📁 **Ensure the correct folder path is provided** — an invalid path halts the script before any changes are made.
- 🧪 **Test on sample files first** — create a test folder with dummy files and verify the preview looks right before applying to real data.
- 🔡 Extensions are **case-sensitive** on some systems (e.g., `.TXT` ≠ `.txt` on Linux/macOS).
- 🚫 The script only renames files in the **top-level folder** — it does not recurse into subfolders.
- ⌨️ **Press Ctrl+C at any time** to exit safely — no files will be changed.

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
