from view.commands.command import Command


class Delete_note(Command):
    def __init__(self, console_ui) -> None:
        super().__init__(console_ui)
        self.description = "Удалить заметку"

    def execute(self):
        self.console_ui.delete_note()
        