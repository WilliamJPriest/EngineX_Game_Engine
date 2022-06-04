from ursina import *
from Editor.gui.vs import *
from Editor.gui.obj_keys import *
from Editor.add_obj import *


class render_obj(Button, Object, Keys):
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
            self.Mov_Keys(key)
            self.GUI_Keys(key)


class Render(Add_obj):
    def render_all(self):
        for k, v in self.objects.items():
            render_obj(Model=v['model'], Color=color, Position=v['pos'])
    
