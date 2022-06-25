from PyQt5.QtWidgets import QWidget

from . import pageDict

def getPage(pageName : str) -> QWidget:
    if pageName in pageDict.pages:
        return pageDict.pages[pageName]()
    raise IndexError(
        f"Page {pageName} not found!\nPossible pages are :\n{list(pageDict.pages.values())}")