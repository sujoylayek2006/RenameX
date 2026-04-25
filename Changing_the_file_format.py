"""
Tool Name: RenameX
Description: Renames files from one extension to another in a user-specified folder.
"""

import os


def print_banner():
    """Prints the tool's banner and essential information to the terminal."""
    banner = """
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
    """
    print(banner)


def rename_files(folder_path, from_ext, to_ext):
    """Rename all files with from_ext to to_ext inside folder_path."""

    # Check if the provided folder path actually exists
    if not os.path.isdir(folder_path):
        print(f"[Error] Folder not found: '{folder_path}'")
        return

    count = 0  # Track how many files were renamed

    # Iterate through every file in the specified folder
    for filename in os.listdir(folder_path):

        # Check if the current file ends with the source extension
        if filename.endswith(from_ext):

            # Build the new filename by swapping the extension
            new_name = filename.replace(from_ext, to_ext)

            # Build full paths for the old and new file
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_name)

            try:
                # Rename the file
                os.rename(old_file, new_file)

                # Confirm the rename to the user
                print(f"  Renamed: {filename}  ->  {new_name}")
                count += 1  # Increment the success counter

            except Exception as e:
                # Report any error that occurs during renaming
                print(f"  [Error] Could not rename '{filename}': {e}")

    # Print a final summary of how many files were renamed
    print(f"\nDone! {count} file(s) renamed.")


# ── User Input Section ──────────────────────────────────────────────────────

# Display the banner when the script starts
print_banner()

# Ask the user for the folder path (press Enter to use current directory)
folder = input("Enter folder path (press Enter for current directory): ").strip()
if folder == "":
    folder = "."  # Default to current directory if nothing is entered

# Ask for the source extension (e.g. .txt)
from_extension = input("Enter source extension (e.g. .txt): ").strip()
if not from_extension.startswith("."):
    from_extension = "." + from_extension  # Auto-add dot if missing

# Ask for the target extension (e.g. .md)
to_extension = input("Enter target extension (e.g. .md): ").strip()
if not to_extension.startswith("."):
    to_extension = "." + to_extension  # Auto-add dot if missing

# Display a summary of what will happen before executing
print(f"\nRenaming '{from_extension}' -> '{to_extension}' in: {folder}\n")

# Call the rename function with the user-provided values
rename_files(folder, from_extension, to_extension)
