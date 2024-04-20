from datetime import datetime



class Note:
    id_counter = 0

    def __init__(self, title, body):
        Note.id_counter += 1
        self.id = Note.id_counter
        self.title = title
        self.body = body
        self.date = datetime.now()