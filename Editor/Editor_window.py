from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import subprocess
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from Editor.twod import TwoD
win = Ursina()

class Window:
    def Win(self):
        for x in range(10):
            for z in range(10):
                Entity(
                    model='cube', 
                    color=color.dark_gray, 
                    collider='box',
                    ignore=True,
                    position= (x, 0, z), 
                    origin_y=0.5, 
                    parent=scene,
                    texture = 'white_cube')
        FirstPersonController()

    def Win2D(self):
        for x in range(10):
            for z in range(10):
                Entity(
                    model='cube', 
                    color=color.dark_gray, 
                    collider='box',
                    ignore=True,
                    position= (x, 0, z), 
                    origin_y=0.5, 
                    parent=scene,
                    texture = 'white_cube')
        TwoD()
        

        





