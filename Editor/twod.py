from ursina import *
import dearpygui.dearpygui as dpg
from Editor import obj
from Editor.gui.main import *
import threading
from ursina.prefabs.first_person_controller import FirstPersonController


class TwoD(Button, Main):
    def __init__(self):
        super().__init__(model='', scale=0)
        Main.__init__(self, obj)

    def input(self, key):
        if key == 'm':
            run_main = threading.Thread(target=self.run_main)
            run_main.start()
        if key == 'd':
            camera.rotation_y += 5
        if key == 'a':
            camera.rotation_y -= 5
        if key == 's':
            camera.rotation_x += 5
        if key == 'w':
            camera.rotation_x -= 5
        if key == 'f':
            FirstPersonController()
        if key == 'e':
            FirstPersonController().disable()