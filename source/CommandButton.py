from PyQt5.QtWidgets import QPushButton


class CommandButton(QPushButton):
    def __init__(self, text, command):
        super().__init__(text)
        self.command = command

    def get_command(self):
        return self.command
