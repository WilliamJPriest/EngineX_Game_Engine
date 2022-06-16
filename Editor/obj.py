from ursina import *
from Editor.gui.vs import *
from Editor.gui.obj_keys import *
from Editor.add_obj import *


class render_obj(Button, Object, Keys):
    def __init__(self, running, Scale=(1, 1, 1), Origin: float=0.6,Texture: str='', Position:tuple = (5, 2, 5), Name='',Model: str = 'cube', Color='red', **kwargs):
        self.Name = Name
        self.running = running
        self.Model = Model
        super().__init__(
            parent=scene,
            scale=Scale,
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
            if self.running == False:
                self.Mov_Keys(key)
                self.GUI_Keys(key)


class render_obj_play(render_obj):
    def input(self, key):
        if self.hovered:
            b = Text(scale=1, text=f'{self.get_position()} {self.scale}')
            b.fade_out()
            self.key = key
            


class Render(Add_obj):
    def render_all(self, running=False, **kwargs):
        for k, v in self.objects().items():
            render_obj(Name=k, running=running, Model=v['model'], Color=v['color'], Position=v['pos'], Scale=v['scale'], Origin=v['origin'])
    
