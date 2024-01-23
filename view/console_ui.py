from view.main_menu import Main_menu
from view.view import View
from presenter.presenter import Presenter


class Console_ui(View):

    ERROR_MSG = "Введено не корректное значение!\n"

    def __init__(self, val):
        super().__init__()
        self.work = val
        self.menu = Main_menu(self)
        self.presenter = Presenter()

    def check_number(self, choice):
        if(len(self.menu.command_list) >= choice):
            return True
        else:
            return False

    def start(self):
        print("Здравствуйте\n")
        while self.work:
            self.menu.print_menu()
            try:
                choice = int(input("Введите номер команды: "))
                print()
                if (self.check_number(choice)):
                    self.menu.execute(choice)
                else:
                    print(Console_ui.ERROR_MSG)
            except ValueError:
                print(Console_ui.ERROR_MSG)

    def add_note(self):
        name_note = input("Введите имя заметки:\n")
        body_note = input("Введите текст заметки:\n")
        self.presenter.add_note(name_note, body_note)
        print("Заметка добавлена\n")

    def all_notes(self):
        print(self.presenter.all_notes())

    def edit_note(self):
        print(self.presenter.print_name_notes())
        try:
            num_note = int(input("Введите номер заметки которую хотите изменить: "))
            print()
            name_note = input("Введите новое имя:\n")
            print()
            body_note = input("Введите новый текст:\n")
            print()
            print(self.presenter.edit_note(num_note, name_note, body_note))
        except ValueError:
            print(Console_ui.ERROR_MSG)

    def delete_note(self):
        print(self.presenter.print_name_notes())
        try:
            num_note = int(input("Введите номер заметки которую хотите удалить: "))
            print()
            print(self.presenter.delete_note(num_note))
        except ValueError:
            print(Console_ui.ERROR_MSG)

    def finish(self):
        if (self.presenter.finish()):
            print("Заметки успешно сохранены.\nДосвидания. \n")
        else:
            print("Увы, заметки не удалось сохранить.\nДосвидания. \n")
        self.work = False
