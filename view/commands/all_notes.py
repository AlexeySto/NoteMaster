from view.commands.command import Command


class All_notes(Command):
    def __init__(self, console_ui) -> None:
        super().__init__(console_ui)
        self.description = "Вывести все заметки"

    def execute(self):
        self.console_ui.all_notes()
        