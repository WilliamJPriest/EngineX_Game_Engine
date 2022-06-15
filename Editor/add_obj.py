import  json
from Editor.gui.error_windows import *
from Editor.project import *

objects = {}

class Add_obj:

    def objects(self) -> dict:
        try:
            f = open(objectsFile, 'r').read()
            y = json.loads(f)
            return y
        except Exception as e:
            Error_Window_Tk().err_win_tk(e)
            self.add(Model='cube', Position=(5, 2, 5), Name='Cube')
            self.objects()

    def add(self, Model, Position:tuple, Color='', Name='', Origin='', Scale:tuple=(1, 1, 1), **kwargs):
        objects[Name] = {
        'model':Model, 
        'color':Color,
        'scale':Scale,
        "origin":Origin,
        'pos':tuple(int(i) for i in Position)
        }
        y = json.dumps(objects)
        f = open(objectsFile, "w")
        f.write(y)
        f.close()


    

