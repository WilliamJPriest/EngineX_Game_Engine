from ursina import *
from Editor.gui.vs import *
from Editor.gui.obj_keys import *
from Editor.add_obj import *
from .project import *


class render_obj(Button, Object, Keys):
    def __init__(self,  Gravity:bool=False, Scale=(1, 1, 1), Origin: float=0.6,Texture: str='', Position:tuple = (5, 2, 5), Name='',Model: str = 'cube', Color='red', **kwargs):
        self.Name = Name
        self.Model = Model
        self.Gravity = Gravity
        super().__init__(
            parent=scene,
            scale=Scale,
            position=Position,
            model=Model,
            origin = Origin,
            texture=Texture,
            color = Color
            )


    def update(self):
        if self.Gravity:
            self.origin_y += 0.1

    def input(self, key):
        if self.hovered:
            b = Text(scale=1, text=f'{self.get_position()} {self.scale}')
            b.fade_out()
            self.key = key
            if not Play:
                self.Mov_Keys(key)
                self.GUI_Keys(key)

            
class Render(Add_obj):
    def render_all(self, **kwargs):
        for k, v in self.objects().items():
            render_obj(Name=k, Model=v['model'], Color=v['color'], Position=v['pos'], Scale=v['scale'], Origin=v['origin'])
    
