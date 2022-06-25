from navigation import MainWindow
from navigation import NavController
from .Container import DependencyContainer as DI

def init_resources():
    DI.Singleton(MainWindow, "MainWindow")
    DI.Singleton(NavController, "NavController")