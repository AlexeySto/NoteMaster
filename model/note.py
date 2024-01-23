import datetime


class Note:
    def __init__(self, name_note, body_note) -> None:
        self.data_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.name_note = name_note
        self.body_note = body_note
        