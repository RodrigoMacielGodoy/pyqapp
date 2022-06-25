from PyQt5.QtWidgets import QWidget
from .homeUI import Ui_HomePage

class HomePage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)