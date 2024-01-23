from model.service import Service


class Presenter:
    def __init__(self) -> None:
        self.service = Service()
    
    def add_note(self, name_note, body_note):
        self.service.add_note(name_note, body_note)
    
    def all_notes(self):
        return self.service.all_notes()
    
    def print_name_notes(self):
        return self.service.print_name_notes()

    def edit_note(self, num_note, name_note, body_note):
        return self.service.edit_note(num_note, name_note, body_note)
    
    def delete_note(self, num_note):
        return self.service.delete_note(num_note)
    
    def finish(self):
        return self.service.finish()
