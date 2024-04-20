
from models.NoteModel import NoteModel
from presenter.NotePresenter import NotePresenter
from views.NoteView import NoteView
def main():
    model = NoteModel()
    view = NoteView()
    presenter = NotePresenter(model, view)

    while True:
        print("\nMenu:")
        print("1. Show all notes")
        print("2. Show notes by date")
        print("3. Add note")
        print("4. Edit note")
        print("5. Delete note")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            presenter.show_all_notes()
        elif choice == '2':
            date = input("Enter date (YYYY-MM-DD): ")
            presenter.show_note_by_date(date)
        elif choice == '3':
            title = input("Enter note title: ")
            body = input("Enter note body: ")
            presenter.add_note(title, body)
        elif choice == '4':
            index = int(input("Enter index of the note to edit: "))
            new_title = input("Enter new title: ")
            new_body = input("Enter new body: ")
            presenter.edit_note(index - 1, new_title, new_body)
        elif choice == '5':
            index = int(input("Enter index of the note to delete: "))
            presenter.delete_note(index)
        elif choice == '6':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()