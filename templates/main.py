import sys
from PyQt5.QtWidgets import QApplication
import di
from pageFactory import getPage

def main():
    app = QApplication(sys.argv)
    di.init_resources()
    navCtrl = di.DI["NavController"]
    ROOT_PAGE = getPage("HomePage")
    navCtrl.setRoot(ROOT_PAGE)
    mainWin = di.DI["MainWindow"]
    mainWin.show()
    app.exec_()

if __name__ == "__main__":
    main()