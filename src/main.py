"""
Tool Name    : RenameX
Description  : Renames files from one extension to another in a user-specified folder.
Developed by : SUJOY LAYEK
Date         : 25-04-2026
"""

import os


# ── Banner ───────────────────────────────────────────────────────────────────

def print_banner():
    """Prints the tool's banner and essential information to the terminal."""
    banner = """
================================================================
    ____                                 _  __
   / __ \\___  ____  ____ _____ ___  ____| |/ /
  / /_/ / _ \\/ __ \\/ __ `/ __ `__ \\/ _ \\   / 
 / _, _/  __/ / / / /_/ / / / / / /  __/   | 
/_/ |_|\\___/_/ /_/\\__,_/_/ /_/ /_/\\___/_/|_| 

================================================================
[*] Tool        : RenameX - File Extension Changer
[*] Version     : 1.0
[*] Developer   : SUJOY LAYEK
[*] Description : Fast and secure bulk file extension modifier.
================================================================
    """
    print(banner)


# ── Helper: Extension Input ───────────────────────────────────────────────────

def ask_extension(prompt_label):
    """
    Asks the user to enter a file extension and keeps asking until
    a non-empty value is provided. Automatically adds the leading dot
    if the user forgets it, and shows them what was accepted.

    Args:
        prompt_label (str): A human-readable label like 'source' or 'target'.

    Returns:
        str: A valid file extension starting with a dot (e.g. '.txt').
    """
    while True:
        value = input(f"Enter {prompt_label} extension (e.g. .txt): ").strip()

        # Reject empty input — extension is required
        if not value:
            print(f"  [!] {prompt_label.capitalize()} extension cannot be empty. Please try again.\n")
            continue

        # Auto-add the dot if the user forgot it (e.g. 'txt' -> '.txt')
        if not value.startswith("."):
            value = "." + value
            print(f"  [+] Auto-corrected to: '{value}'")

        return value


# ── Core Logic: Preview & Rename ─────────────────────────────────────────────

def get_rename_pairs(folder_path, from_ext, to_ext):
    """
    Scans the folder and returns a list of (old_path, new_path, filename, new_name)
    tuples for every file that matches from_ext.

    Args:
        folder_path (str): The directory to scan.
        from_ext    (str): The extension to look for (e.g. '.txt').
        to_ext      (str): The extension to rename to  (e.g. '.md').

    Returns:
        list[tuple]: Each tuple is (old_path, new_path, old_name, new_name).
    """
    pairs = []
    for filename in os.listdir(folder_path):
        # Match files that end with the source extension (case-insensitive)
        if filename.lower().endswith(from_ext.lower()):
            # Replace only the trailing extension, not occurrences inside the name
            base = filename[: len(filename) - len(from_ext)]
            new_name = base + to_ext
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            pairs.append((old_path, new_path, filename, new_name))
    return pairs


def rename_files(folder_path, from_ext, to_ext):
    """
    Main rename workflow:
      1. Validates the folder.
      2. Scans for matching files.
      3. Shows a preview (dry-run).
      4. Asks for confirmation.
      5. Performs the renames and prints a final summary.

    Args:
        folder_path (str): The directory to work in.
        from_ext    (str): The extension to change from.
        to_ext      (str): The extension to change to.
    """

    # ── Step 1: Validate folder ───────────────────────────────────────────────
    if not os.path.isdir(folder_path):
        print(f"\n  [Error] Folder not found: '{folder_path}'")
        print("  Make sure the path exists and you have permission to access it.\n")
        return

    # ── Step 2: Scan for matching files ──────────────────────────────────────
    pairs = get_rename_pairs(folder_path, from_ext, to_ext)

    if not pairs:
        print(f"\n  [Info] No '{from_ext}' files found in: {folder_path}")
        print("  Nothing was changed.\n")
        return

    # ── Step 3: Preview (dry-run) ─────────────────────────────────────────────
    print(f"\n  Preview — {len(pairs)} file(s) will be renamed:\n")
    for _, _, old_name, new_name in pairs:
        print(f"    {old_name}  ->  {new_name}")

    # ── Step 4: Ask for confirmation ──────────────────────────────────────────
    print()
    confirm = input("  Proceed with renaming? (y/n): ").strip().lower()
    if confirm != "y":
        print("\n  [Cancelled] No files were changed.\n")
        return

    # ── Step 5: Rename files ──────────────────────────────────────────────────
    print()
    success_count = 0
    error_count   = 0

    for old_path, new_path, old_name, new_name in pairs:

        # Guard: skip if a file with the new name already exists
        if os.path.exists(new_path):
            print(f"  [Skip]  '{new_name}' already exists — skipping '{old_name}'")
            error_count += 1
            continue

        try:
            os.rename(old_path, new_path)
            print(f"  [OK]    {old_name}  ->  {new_name}")
            success_count += 1

        except PermissionError:
            print(f"  [Error] No permission to rename '{old_name}'. Is it open in another program?")
            error_count += 1

        except Exception as e:
            print(f"  [Error] Could not rename '{old_name}': {e}")
            error_count += 1

    # ── Summary ───────────────────────────────────────────────────────────────
    print(f"\n  Done!  {success_count} renamed", end="")
    if error_count:
        print(f",  {error_count} skipped/failed", end="")
    print()


# ── Entry Point ───────────────────────────────────────────────────────────────

def main():
    """Runs the interactive RenameX session."""

    # Show the banner at startup
    print_banner()

    try:

        # ── Get folder path ───────────────────────────────────────────────────
        print("Step 1 of 3 — Folder")
        print("  Enter the full path to the folder you want to work in.")
        print("  Press Enter to use the CURRENT directory.\n")

        folder = input("  Folder path: ").strip()
        if folder == "":
            folder = os.getcwd()   # Use actual current directory, not '.'
            print(f"  [+] Using current directory: {folder}")

        # ── Get source extension ──────────────────────────────────────────────
        print("\nStep 2 of 3 — Source Extension")
        print("  This is the extension your files currently have.\n")
        from_extension = ask_extension("source")

        # ── Get target extension ──────────────────────────────────────────────
        print("\nStep 3 of 3 — Target Extension")
        print("  This is the extension you want to rename your files TO.\n")
        to_extension = ask_extension("target")

        # Guard: renaming to the same extension is pointless
        if from_extension.lower() == to_extension.lower():
            print(f"\n  [Info] Source and target extensions are the same ('{from_extension}').")
            print("  Nothing to do — exiting.\n")
            return

        # ── Run ───────────────────────────────────────────────────────────────
        print(f"\n  Scanning '{folder}' for '{from_extension}' files...")
        rename_files(folder, from_extension, to_extension)

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully — don't dump a scary traceback
        print("\n\n  [Interrupted] No files were changed. Goodbye!\n")


if __name__ == "__main__":
    main()
