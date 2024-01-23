from model.note import Note
from model.file_handler import File_handler
import datetime


class Notes_List:
    def __init__(self) -> None:
        self.notes_list = File_handler.load_notes()

    def add_note(self, name_note, body_note):
        self.notes_list.append(Note(name_note, body_note))

    def print_name_notes(self):
        res = ""
        i = 1
        for x in self.notes_list:
            res += f"{i}. {x.name_note}\n"
            i += 1
        return res

    def all_notes(self):
        res = ""
        i = 1
        for x in self.notes_list:
            res += f"{i}. {x.data_time}\n Заголовок: {x.name_note}\n Текст:\n{x.body_note}\n"
            i += 1
        return res

    def checked_num_note(self, num_note):
        if (num_note <= len(self.notes_list)):
            return True
        else:
            raise ValueError("Заметки с таким индексом нет.")
            return False

    def edit_note(self, num_note, name_note, body_note):
        try:
            if (self.checked_num_note(num_note)):
                self.notes_list[num_note -
                                1].data_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                self.notes_list[num_note - 1].name_note = name_note
                self.notes_list[num_note - 1].body_note = body_note
                return f"Заметка {num_note} изменена."
        except ValueError as msg:
            return msg

    def delete_note(self, num_note):
        try:
            if (self.checked_num_note(num_note)):
                self.notes_list.pop(num_note - 1)
                return f"Заметка {num_note} удалена."
        except ValueError as msg:
            return msg
        
    def finish(self):
        try:
            File_handler.save_notes(self.notes_list)
            return True
        except IOError:
            return False
