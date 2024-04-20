class NoteView:
    def show_notes(self, notes):
        if notes:
            for i, note in enumerate(notes):
                print(f"{i + 1}.id = {note.id} date: {note.date.strftime('%Y-%m-%d %H:%M:%S')}\n {note.title} \n{note.body}\n")
        else:
            print("No notes found.")

    def show_note(self, note):
        if note:
            print(f"[{note.id}] {note.title} - {note.date.strftime('%Y-%m-%d %H:%M:%S')}\n{note.body}")
        else:
            print("Note not found.")

    def get_user_input(self, prompt):
        return input(prompt)
