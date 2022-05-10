from PyQt5 import QtCore, QtGui, QtWidgets
from Hub import *
import os
import sys

app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(open('hub/style.css', 'r').read())
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())