from .project import *
from datetime import date

today = date.today()

f = open('history.txt', 'r').read()
history = f + '\n' + projectFile + ' ' + str(today)
f = open('history.txt', "w")
f.write(history)
f.close()