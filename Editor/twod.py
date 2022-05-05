from ursina import *
import dearpygui.dearpygui as dpg
from Editor import obj
from Editor.ui.main import *



class TwoD(Button, Main):
    def __init__(self):
        super().__init__(model='', scale=0)
        Main.__init__(self, obj)

    def input(self, key):
        if key == 'm':
            self.run_main()
        if key == 'd':
            camera.rotation_y += 1
        if key == 'a':
            camera.rotation_y -= 1
        if key == 's':
            camera.rotation_x += 1
        if key == 'w':
            camera.rotation_x -= 1
