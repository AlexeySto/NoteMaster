from view.commands.command import Command


class Add_note(Command):
    def __init__(self, console_ui) -> None:
        super().__init__(console_ui)
        self.description = "Создать заметку"

    def execute(self):
        self.console_ui.add_note()
        