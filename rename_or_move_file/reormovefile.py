from pathlib import Path

# Old file path
old_path = Path("/path/to/old_file.txt")

# New file path /can be same directory with different name or a different folder
new_path = Path("/path/to/new_file.txt")  # Rename
# new_path = Path("/new/folder/new_file.txt")  # Move

# Rename or move the file
old_path.rename(new_path)

print(f"File moved/renamed to: {new_path}")
