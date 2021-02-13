"""
An Aplication to view Krypto Graph´s.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

import matplotlib


class KryptoGraph(toga.App):

    def startup(self):
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return KryptoGraph()
