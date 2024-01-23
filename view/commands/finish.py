from view.commands.command import Command


class Finish(Command):
    def __init__(self, console_ui) -> None:
        super().__init__(console_ui)
        self.description = "Завершить работу"

    def execute(self):
        self.console_ui.finish()
