
from datetime import datetime

class NotePresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_all_notes(self):
        notes = self.model.get_notes()
        self.view.show_notes(notes)

    def show_note_by_date(self, date):
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        selected_notes = self.model.get_note_by_date(date_obj.date())
        self.view.show_notes(selected_notes)

    def show_note_by_index(self, index):
        notes = self.model.get_notes()
        if 0 <= index < len(notes):
            self.view.show_note(notes[index])
        else:
            self.view.show_note(None)

    def add_note(self, title, body):

        self.model.add_note(title, body)

    def edit_note(self, id, new_title, new_body):

        self.model.edit_note(id, new_title, new_body)

    def delete_note(self, id):
        self.model.delete_note(id)


