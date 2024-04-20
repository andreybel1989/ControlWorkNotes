
import json
import os
from datetime import datetime

from .Note import Note


class NoteModel:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.notes = []

        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for note_data in data:
                    # id = note_data.get('id')
                    title = note_data.get('title')
                    body = note_data.get('body')

                    # date = datetime.strptime(note_data.get('date'), '%Y-%m-%d %H:%M:%S')
                    self.notes.append(Note(title, body))

    def save_notes(self):
        serialized_notes = []
        for note in self.notes:
            serialized_note = {
                'id': note.id,
                'title': note.title,
                'body': note.body,
                'date': note.date.strftime('%Y-%m-%d %H:%M:%S')
            }
            serialized_notes.append(serialized_note)

        with open(self.filename, 'w') as file:
            json.dump(serialized_notes, file)

    def add_note(self, title, body):
        self.notes.append(Note(title, body))
        self.save_notes()

    def edit_note(self, index, title, body):
        if 0 <= index < len(self.notes):

            id = self.notes[index].id

            date = self.notes[index].date
            self.notes[index] = Note(title, body)
            self.save_notes()


    def delete_note(self, id):
        note_id = int(id)
        for index, note in enumerate(self.notes):
            print(note.id)
            if note.id == note_id:
                del self.notes[index]
                self.save_notes()
                print("Заметка удалена успешно")
                return
        print("Заметка с указанным id не существует.")

    def get_notes(self):
        return self.notes

    def get_note_by_date(self, date):
        selected_notes = [note for note in self.notes if note.date.date() == date]
        return selected_notes
