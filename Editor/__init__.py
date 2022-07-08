from .project import *
from datetime import date
from Editor.gui.error_windows import Error_Window_Tk

today = date.today()

def history(filename):
    f = open(filename, 'r').read()
    history = f + '\n' + projectFile + ' ' + str(today)
    f = open(filename, "w")
    f.write(history)
    f.close()

try:
    history(historyFile)
except Exception as e:
    Error_Window_Tk().err_win_tk(e)
    exit()


    