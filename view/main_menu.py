from view.commands.add_note import Add_note
from view.commands.all_notes import All_notes
from view.commands.edit_note import Edit_note
from view.commands.delete_note import Delete_note
from view.commands.finish import Finish


class Main_menu:
    def __init__(self, console_ui) -> None:
        self.command_list = []
        self.console_ui = console_ui
        self.command_list.append(Add_note(console_ui))
        self.command_list.append(All_notes(console_ui))
        self.command_list.append(Edit_note(console_ui))
        self.command_list.append(Delete_note(console_ui))
        self.command_list.append(Finish(console_ui))

    def print_menu(self):
        i = 1
        for x in self.command_list:
            print(f"{i}. {x.description}")
            i +=1
        print()

    def execute(self, choice):
        self.command_list[choice - 1].execute()
