import di
from .mainWindow import MainWindow

class NavController():
    def __init__(self) -> None:
        self.window : MainWindow = di.DI["MainWindow"]

    def push(self, page):
        self.window.ui.PageContent.addWidget(page)
        page.show()
        self.window.ui.PageContent.setCurrentWidget(page)

    def setRoot(self, page):
        self.__clear_stack()
        self.window.ui.PageContent.addWidget(page)
        page.show()

    def popToRoot(self):
        count = self.window.ui.PageContent.count()
        if count == 1:
            return
        for i in range(1, count):
            widget = self.window.ui.PageContent.widget(i)
            self.window.ui.PageContent.removeWidget(widget)

    def pop(self):
        currentIndex = self.window.ui.PageContent.currentIndex()
        self.window.ui.PageContent.setCurrentIndex(currentIndex-1)
        widget = self.window.ui.PageContent.widget(currentIndex)
        self.window.ui.PageContent.removeWidget(widget)

    def __clear_stack(self):
        count = self.window.ui.PageContent.count()
        for i in range(count):
            widget = self.window.ui.PageContent.widget(i)
            self.window.ui.PageContent.removeWidget(widget)
