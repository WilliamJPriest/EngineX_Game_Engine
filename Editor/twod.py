from matplotlib import scale
from ursina import *


class TwoD(Button):
    def __init__(self):
        super().__init__(model='', scale=0)
    
    def input(self, key):
        if key == 'd':
            camera.rotation_y += 1
        if key == 'a':
            camera.rotation_y -= 1
        if key == 's':
            camera.rotation_x += 1
        if key == 'w':
            camera.rotation_x -= 1
