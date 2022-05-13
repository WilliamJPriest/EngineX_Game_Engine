from subprocess import check_output
from New import *
import os
import sys

def Newproject_gui():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    demo = LoadingGif()
    demo.mainUI(window)
    window.show()
    sys.exit(sys.argv[1] in check_output(['ls']).decode())
    

def Newproject(project):
    os.system(f'bash  NewProject/NewProject.sh {project}')

Newproject(sys.argv[1])
