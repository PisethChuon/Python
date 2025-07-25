import os

# write notes
# view notes
# delete note
# menu - simple CLI

NOTES_FILE = "notes.txt"

def write_note():
    note_title = input("Type your note title: ").strip()
    note_content = input("Type your note: ").strip()
    if note_title and note_content:
        with open(NOTES_FILE, "a") as file:
            file.write(f"Title: {note_title}\n{note_content}\n{'-'*40}\n")
        print("Note saved!\n")
    else:
        print("Title and note cannot be empty.\n")

def view_notes():
    if not os.path.exists(NOTES_FILE) or os.path.getsize(NOTES_FILE) == 0:
        print("No notes found.\n")
        return
    with open(NOTES_FILE) as file:
        print("\nYour Notes:\n")
        print(file.read())

def delete_notes():
    if os.path.exists(NOTES_FILE):
        open(NOTES_FILE, "w").close()
        print("All notes deleted.\n")
    else:
        print("No notes to delete.\n")

def menu():
    while True:
        print("1. Write a note")
        print("2. View notes")
        print("3. Delete all notes")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            write_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()

