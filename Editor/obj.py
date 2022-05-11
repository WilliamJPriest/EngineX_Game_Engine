from ursina import *
from Editor.ui.input import *
from Editor.ui.vs import *
import threading

class add_obj(Button, Object):
    def __init__(self, Origin: float=0.6, Texture: str='', Position:tuple = (5, 2, 5), Model: str = 'cube', Color='red', **kwargs):
        super().__init__(
            parent=scene,
            position=Position,
            model=Model,
            origin = Origin,
            texture=Texture,
            color = Color
            )

    def input(self, key):
        if self.hovered:
            b = Text(scale=1, text=f'{self.get_position()} {self.scale}')
            b.fade_out()
            self.key = key
            if key == 'g':
                self.origin_x += 1
            if key == 'h':
                self.origin_x -= 1
            if key == 'b':
                self.origin_y += 1
            if key == 'delete':
                self.disable()
            if key == 'e':
                run_vs = threading.Thread(target=self.run_vs)
                run_vs.start()
            if key == 'y':
                self.origin_y -= 1
            if key == 'j':
                self.origin_z -= 1
            if key == 'k':
                self.origin_z += 1
            if key == 'o':
                self.rotation_x -= 1
            if key == 'm':
                self.rotation_x += 1
            if key == 'p':
                self.rotation_y -= 1
            if key == 'l':
                self.rotation_y += 1
            if key == 'c':
                self.scale_x -= 0.1
            if key == 'v':
                self.scale_x += 0.1
            if key == 'z':
                self.scale_y -= 0.1
            if key == 'x':
                self.scale_y += 0.1
            if key == ']':
                pos = input(':')
                self.position = tuple([int(i) for i in pos])



            

class add_2dobj(add_obj):
    def input(self, key):
        if self.hovered:
            b = Text(scale=2, text=f'{self.get_position()}')
            b.fade_out()
            print(self.get_position())
            if key == 'g':
                self.origin_x += 1
            if key == 'h':
                self.origin_x -= 1
            if key == 'b':
                self.origin_y += 1
            if key == 'y':
                self.origin_y -= 1
            if key == 'k':
                self.origin_z += 1
            if key == 'o':
                self.rotation_x -= 1
            if key == 'm':
                self.rotation_x += 1
            if key == 'p':
                self.rotation_y -= 1
            if key == 'l':
                self.rotation_y += 1
            if key == 'c':
                self.scale_x -= 0.1
            if key == 'v':
                self.scale_x += 0.1
            if key == 'z':
                self.scale_y -= 0.1
            if key == 'x':
                self.scale_y += 0.1