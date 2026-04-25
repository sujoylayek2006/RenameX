# 📖 RenameX — Usage Examples

This file demonstrates real-world use cases for **RenameX**, covering common scenarios, edge cases, and expected outputs.

---

## 🚀 How to Run

From the **project root**, run:

```bash
python src/main.py
```

---

## 📌 Example 1 — Convert `.txt` to `.md`

**Scenario:** You have a notes folder full of `.txt` files and want to convert them to Markdown.

**Input:**
```
Enter folder path (press Enter for current directory): C:\Users\John\Documents\notes
Enter source extension (e.g. .txt): .txt
Enter target extension (e.g. .md): .md
```

**Output:**
```
Renaming '.txt' -> '.md' in: C:\Users\John\Documents\notes

  Renamed: todo.txt       ->  todo.md
  Renamed: ideas.txt      ->  ideas.md
  Renamed: summary.txt    ->  summary.md

Done! 3 file(s) renamed.
```

---

## 📌 Example 2 — Convert `.jpeg` to `.jpg`

**Scenario:** Standardizing image file extensions in a photo folder.

**Input:**
```
Enter folder path (press Enter for current directory): C:\Users\John\Pictures\vacation
Enter source extension (e.g. .txt): .jpeg
Enter target extension (e.g. .md): .jpg
```

**Output:**
```
Renaming '.jpeg' -> '.jpg' in: C:\Users\John\Pictures\vacation

  Renamed: beach.jpeg     ->  beach.jpg
  Renamed: sunset.jpeg    ->  sunset.jpg
  Renamed: family.jpeg    ->  family.jpg

Done! 3 file(s) renamed.
```

---

## 📌 Example 3 — Use Current Directory (press Enter)

**Scenario:** You are already inside the target folder in your terminal and want to rename files without typing a path.

**Input:**
```
Enter folder path (press Enter for current directory): 
Enter source extension (e.g. .txt): .log
Enter target extension (e.g. .md): .txt
```

> ✅ Pressing **Enter** defaults to the folder where `main.py` is running from.

**Output:**
```
Renaming '.log' -> '.txt' in: .

  Renamed: error.log      ->  error.txt
  Renamed: system.log     ->  system.txt

Done! 2 file(s) renamed.
```

---

## 📌 Example 4 — Extension Without Dot (Auto-fix)

**Scenario:** You forget to add the `.` before the extension — RenameX handles it automatically.

**Input:**
```
Enter folder path (press Enter for current directory): C:\Users\John\Downloads\reports
Enter source extension (e.g. .txt): csv
Enter target extension (e.g. .md): xlsx
```

> ✅ RenameX auto-adds the dot: `csv` → `.csv`, `xlsx` → `.xlsx`

**Output:**
```
Renaming '.csv' -> '.xlsx' in: C:\Users\John\Downloads\reports

  Renamed: sales.csv      ->  sales.xlsx
  Renamed: budget.csv     ->  budget.xlsx

Done! 2 file(s) renamed.
```

---

## 📌 Example 5 — No Matching Files Found

**Scenario:** The folder exists but contains no files with the given source extension.

**Input:**
```
Enter folder path (press Enter for current directory): C:\Users\John\Documents\empty_folder
Enter source extension (e.g. .txt): .py
Enter target extension (e.g. .md): .txt
```

**Output:**
```
Renaming '.py' -> '.txt' in: C:\Users\John\Documents\empty_folder

Done! 0 file(s) renamed.
```

---

## 📌 Example 6 — Invalid Folder Path (Error Handling)

**Scenario:** The folder path typed does not exist on disk.

**Input:**
```
Enter folder path (press Enter for current directory): C:\Users\John\nonexistent_folder
Enter source extension (e.g. .txt): .txt
Enter target extension (e.g. .md): .md
```

**Output:**
```
[Error] Folder not found: 'C:\Users\John\nonexistent_folder'
```

> ⚠️ RenameX safely stops and reports the error without crashing.

---

## 📌 Example 7 — Linux / macOS Path Format

**Scenario:** Running RenameX on a Unix-based system.

**Input:**
```
Enter folder path (press Enter for current directory): /home/john/documents/notes
Enter source extension (e.g. .txt): .txt
Enter target extension (e.g. .md): .md
```

**Output:**
```
Renaming '.txt' -> '.md' in: /home/john/documents/notes

  Renamed: draft.txt      ->  draft.md
  Renamed: notes.txt      ->  notes.md

Done! 2 file(s) renamed.
```

---

## 💡 Tips

| Tip | Detail |
|-----|--------|
| **Default directory** | Press `Enter` at the path prompt to use the current folder |
| **Dot optional** | You can type `txt` or `.txt` — both work |
| **Any extension** | Works with any file type: `.html`, `.py`, `.csv`, `.jpeg`, etc. |
| **Safe on errors** | File permission errors are reported but don't stop the process |
| **Cross-platform** | Works on Windows, Linux, and macOS |
