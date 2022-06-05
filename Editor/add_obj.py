import  json
from Editor.gui.error_window import *


objects = {}

class Add_obj:

    def objects(self) -> dict:
        try:
            f = open('objects.txt', 'r').read()
            y = json.loads(f)
            return y
        except Exception as e:
            Error_Window_Tk().err_win_tk(e)
            self.add(Model='cube', Position=(5, 2, 5), Name='Cube')
            self.objects()

    def add(self, Model, Position:tuple, Color='', Name='', **kwargs):
        objects[Name] = {
        'model':Model, 
        'color':Color,
        'pos':tuple(int(i) for i in Position)
        }
        
        y = json.dumps(objects)
        f = open("objects.txt", "w")
        f.write(y)
        f.close()

    def test(self):
        self.add(Model='cube', Position=(5, 2, 5), Name='test')
        self.add(Model='cube 1', Position=(5, 2, 5), Name='test 1')
        for k, v in self.objects().items():
            print(v['model'])



    

