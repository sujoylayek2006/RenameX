# RenameX — Example Walkthrough 📖

This document shows **real examples** of using RenameX — from common renaming tasks to edge cases, with tips along the way.

---

## 📋 Table of Contents

- [How to Run](#-how-to-run)
- [Scenario 1 — Convert `.txt` to `.md`](#-scenario-1--convert-txt-to-md)
- [Scenario 2 — Standardize Image Extensions](#️-scenario-2--standardize-image-extensions)
- [Scenario 3 — Use Current Directory](#-scenario-3--use-current-directory)
- [Scenario 4 — Extension Without Dot (Auto-fix)](#-scenario-4--extension-without-dot-auto-fix)
- [Scenario 5 — No Matching Files Found](#-scenario-5--no-matching-files-found)
- [Scenario 6 — Invalid Folder Path](#️-scenario-6--invalid-folder-path)
- [Scenario 7 — Same Extension Entered Twice](#-scenario-7--same-extension-entered-twice)
- [Scenario 8 — Cancel Before Renaming](#-scenario-8--cancel-before-renaming)
- [Common Mistakes & Fixes](#️-common-mistakes--fixes)
- [Tips](#-tips)

---

## 🚀 How to Run

From the **project root**, run:

```bash
python src/main.py
```

---

## 📝 Scenario 1 — Convert `.txt` to `.md`

**Goal:** You have a notes folder full of `.txt` files and want to convert them all to Markdown.

### Step 1 of 3 — Enter folder path

```
Step 1 of 3 — Folder
  Enter the full path to the folder you want to work in.
  Press Enter to use the CURRENT directory.

  Folder path: C:\Users\Sujoy\Documents\notes
```

### Step 2 of 3 — Enter source extension

```
Step 2 of 3 — Source Extension
  This is the extension your files currently have.

Enter source extension (e.g. .txt): .txt
```

### Step 3 of 3 — Enter target extension

```
Step 3 of 3 — Target Extension
  This is the extension you want to rename your files TO.

Enter target extension (e.g. .txt): .md
```

### Preview & Confirm

```
  Scanning 'C:\Users\Sujoy\Documents\notes' for '.txt' files...

  Preview — 3 file(s) will be renamed:

    todo.txt    ->  todo.md
    ideas.txt   ->  ideas.md
    summary.txt ->  summary.md

  Proceed with renaming? (y/n): y
```

### Watch the results!

```
  [OK]    todo.txt    ->  todo.md
  [OK]    ideas.txt   ->  ideas.md
  [OK]    summary.txt ->  summary.md

  Done!  3 renamed
```

### ✅ Result

```
notes/
├── todo.md
├── ideas.md
└── summary.md
```

---

## 🖼️ Scenario 2 — Standardize Image Extensions

**Goal:** You have a vacation photo folder where all images are `.jpeg` and you want them to be `.jpg` for consistency.

### Step 1 of 3 — Enter folder path

```
Step 1 of 3 — Folder
  Enter the full path to the folder you want to work in.
  Press Enter to use the CURRENT directory.

  Folder path: C:\Users\Sujoy\Pictures\vacation
```

### Step 2 & 3 of 3 — Enter extensions

```
Step 2 of 3 — Source Extension
  This is the extension your files currently have.

Enter source extension (e.g. .txt): .jpeg

Step 3 of 3 — Target Extension
  This is the extension you want to rename your files TO.

Enter target extension (e.g. .txt): .jpg
```

### Preview & Confirm

```
  Scanning 'C:\Users\Sujoy\Pictures\vacation' for '.jpeg' files...

  Preview — 3 file(s) will be renamed:

    beach.jpeg  ->  beach.jpg
    sunset.jpeg ->  sunset.jpg
    family.jpeg ->  family.jpg

  Proceed with renaming? (y/n): y
```

### Watch the results!

```
  [OK]    beach.jpeg  ->  beach.jpg
  [OK]    sunset.jpeg ->  sunset.jpg
  [OK]    family.jpeg ->  family.jpg

  Done!  3 renamed
```

### ✅ Result

```
vacation/
├── beach.jpg
├── sunset.jpg
└── family.jpg
```

---

## 📂 Scenario 3 — Use Current Directory

**Goal:** You are already inside the target folder in your terminal and want to rename files without typing a full path.

### Step 1 of 3 — Press Enter to skip path

```
Step 1 of 3 — Folder
  Enter the full path to the folder you want to work in.
  Press Enter to use the CURRENT directory.

  Folder path:
  [+] Using current directory: C:\Users\Sujoy\projects\logs
```

> **Tip:** Pressing **Enter** resolves and prints the **actual full path** of the current directory — no guessing needed.

### Step 2 & 3 of 3 — Enter extensions

```
Step 2 of 3 — Source Extension
  This is the extension your files currently have.

Enter source extension (e.g. .txt): .log

Step 3 of 3 — Target Extension
  This is the extension you want to rename your files TO.

Enter target extension (e.g. .txt): .txt
```

### Preview & Confirm

```
  Scanning 'C:\Users\Sujoy\projects\logs' for '.log' files...

  Preview — 2 file(s) will be renamed:

    error.log  ->  error.txt
    system.log ->  system.txt

  Proceed with renaming? (y/n): y
```

### Watch the results!

```
  [OK]    error.log  ->  error.txt
  [OK]    system.log ->  system.txt

  Done!  2 renamed
```

---

## 🔧 Scenario 4 — Extension Without Dot (Auto-fix)

**Goal:** You forget to add the `.` before the extension — RenameX handles it automatically.

### Step 2 & 3 of 3 — Enter extensions without dot

```
Step 2 of 3 — Source Extension
  This is the extension your files currently have.

Enter source extension (e.g. .txt): csv
  [+] Auto-corrected to: '.csv'

Step 3 of 3 — Target Extension
  This is the extension you want to rename your files TO.

Enter target extension (e.g. .txt): xlsx
  [+] Auto-corrected to: '.xlsx'
```

> **RenameX auto-adds the dot and tells you:** `csv` → `.csv`, `xlsx` → `.xlsx`

### Preview & Confirm

```
  Preview — 2 file(s) will be renamed:

    sales.csv  ->  sales.xlsx
    budget.csv ->  budget.xlsx

  Proceed with renaming? (y/n): y
```

### Watch the results!

```
  [OK]    sales.csv  ->  sales.xlsx
  [OK]    budget.csv ->  budget.xlsx

  Done!  2 renamed
```

---

## 🔍 Scenario 5 — No Matching Files Found

**Goal:** Understand what happens when no files match the given source extension.

```
  Scanning 'C:\Users\Sujoy\Documents\empty_folder' for '.py' files...

  [Info] No '.py' files found in: C:\Users\Sujoy\Documents\empty_folder
  Nothing was changed.
```

> RenameX clearly tells you **nothing was changed** — no confusion about whether files were moved.

---

## ⚠️ Scenario 6 — Invalid Folder Path

**Goal:** Understand what happens when an incorrect or non-existent folder is entered.

```
  Scanning 'C:\Users\Sujoy\nonexistent_folder' for '.txt' files...

  [Error] Folder not found: 'C:\Users\Sujoy\nonexistent_folder'
  Make sure the path exists and you have permission to access it.
```

> RenameX safely stops and gives you a **helpful hint** — without crashing or touching any files.

---

## 🔁 Scenario 7 — Same Extension Entered Twice

**Goal:** Understand what happens if you accidentally type the same extension for both source and target.

```
Step 2 of 3 — Source Extension
Enter source extension (e.g. .txt): .txt

Step 3 of 3 — Target Extension
Enter target extension (e.g. .txt): .txt

  [Info] Source and target extensions are the same ('.txt').
  Nothing to do — exiting.
```

> RenameX catches this **before scanning any files** — saving time and avoiding pointless work.

---

## 🚫 Scenario 8 — Cancel Before Renaming

**Goal:** You see the preview and decide you don't want to proceed.

```
  Preview — 2 file(s) will be renamed:

    draft.txt ->  draft.md
    notes.txt ->  notes.md

  Proceed with renaming? (y/n): n

  [Cancelled] No files were changed.
```

> Typing anything other than `y` safely aborts — **zero files are touched**.

---

## ⚠️ Common Mistakes & Fixes

| Mistake | What Happens | Fix |
|---|---|---|
| Typing a path that doesn't exist | `[Error] Folder not found` + hint shown | Double-check the folder path for typos |
| Using the wrong source extension | `[Info] No '...' files found` | Make sure the extension matches the actual files |
| Forgetting the dot (e.g. `txt`) | `[+] Auto-corrected to: '.txt'` ✅ | Nothing to fix — RenameX handles it |
| Entering the same extension twice | `[Info] Source and target are the same` | Enter two *different* extensions |
| Running on the wrong folder | Wrong files get renamed | Check the preview carefully, then confirm |
| Extensions are case-sensitive on Linux | `.TXT` ≠ `.txt` | Use the exact case that matches your files |
| A target filename already exists | `[Skip]` shown, original untouched | Rename or remove the conflicting file first |

---

## 💡 Tips

- **No dot needed** — type `txt` or `.txt`, both work the same.
- **Press Enter** at the path prompt to use the current directory — the full path is printed for you.
- **Review the preview** before confirming — you see every rename before anything happens.
- **Type `n` to cancel** at the confirmation prompt if the preview looks wrong.
- **Always backup** important files before running — renaming cannot be undone automatically.
- **Test first** — try on a folder with dummy files before applying to real data.
- **Cross-platform** — works on Windows, Linux, and macOS with no changes.
- **Only top-level** — RenameX renames files in the chosen folder only, not subfolders.

---

> Made with ❤️ by **SUJOY LAYEK**
