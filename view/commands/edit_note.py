from view.commands.command import Command


class Edit_note(Command):
    def __init__(self, console_ui) -> None:
        super().__init__(console_ui)
        self.description = "Редактировать заметку"

    def execute(self):
        self.console_ui.edit_note()
        