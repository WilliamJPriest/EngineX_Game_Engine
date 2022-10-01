from PyQt5 import QtCore, QtGui, QtWidgets
from hub import *
import sys



if __name__ == '__main__': 
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


