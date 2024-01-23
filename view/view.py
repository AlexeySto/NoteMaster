import abc


class View(abc.ABC):
    def __init__(self) -> None:
        super().__init__()

    def start(self):
        raise NotImplementedError("Нельзя вызывать абстрактный метод")
