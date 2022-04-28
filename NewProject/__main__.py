from NewProject.NewProject import *
import os

def Newproject_gui():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    demo = LoadingGif()
    demo.mainUI(window)
    window.show()
    sys.exit(app.exec_())

def Newproject():
    os.system('Newproject/Newproject.sh')
