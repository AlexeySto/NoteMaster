import abc


class Command(abc.ABC):
    def __init__(self, console_ui) -> None:
        super().__init__()
        self.console_ui = console_ui

    def execute(self):
        raise NotImplementedError("Нельзя вызывать абстрактный метод")
