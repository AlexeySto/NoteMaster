from model.note_list import Notes_List


class Service:
    def __init__(self) -> None:
        self.notes_list = Notes_List()

    def add_note(self, name_note, body_note):
        self.notes_list.add_note(name_note, body_note)

    def all_notes(self):
        return self.notes_list.all_notes()

    def print_name_notes(self):
        return self.notes_list.print_name_notes()

    def edit_note(self, num_note, name_note, body_note):
        return self.notes_list.edit_note(num_note, name_note, body_note)

    def delete_note(self, num_note):
        return self.notes_list.delete_note(num_note)
    
    def finish(self):
        return self.notes_list.finish()
