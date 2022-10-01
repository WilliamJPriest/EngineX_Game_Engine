import os, json, requests, json
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def auth(self, username, password):
        x = requests.post('https://whispering-crag-05987.herokuapp.com/login', data={'username':username, 'password':password})
        j = json.loads(x.text)
        return j['success'] == True

    def login(self):
        f = open('hub/login.json', "r")
        y = json.loads(f.read())
        # print(self.auth(y['username'], y['password']))
        if not y['username'] or not y['password'] or not self.auth(y['username'], y['password']):
                return False

        return True
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(676, 480)
        MainWindow.setStyleSheet("color: rgb(114, 159, 207);\n"
"background-color:black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 110, 131, 31))
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 190, 141, 41))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(114, 159, 207);")
        self.pushButton.clicked.connect(lambda: self.on_click())
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 140, 471, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 20, 221, 61))
        self.label_2.setStyleSheet("font: 75 italic 30pt \"Ubuntu Condensed\";\n"
"color: rgb(114, 159, 207);\n"
"")
        self.label_2.setObjectName("label_2")


        if not self.login():
                self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_2.setGeometry(QtCore.QRect(560, 30, 88, 34))
                self.pushButton_2.clicked.connect(lambda: self.onclick_login())
                self.pushButton_2.setStyleSheet("::hover {\n"
        "color:white;\n"
        "}")
                self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.login()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EngineX"))
        self.label.setText(_translate("MainWindow", "New Project:"))
        self.pushButton.setText(_translate("MainWindow", "New Project"))
        self.label_2.setText(_translate("MainWindow", "EngineX"))
        if not self.login(): self.pushButton_2.setText(_translate("MainWindow", "Login"))


    def on_click(self):
        os.system(f"python3 NewProject {self.lineEdit.text()}")
        os.system(f'python3 {self.lineEdit.text()}.py')

    def onclick_login(self):
        os.system('python3 hub/login.py')
        quit()
        




