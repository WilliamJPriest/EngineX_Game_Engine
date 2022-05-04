from ursina import *
import dearpygui.dearpygui as dpg
from Editor import obj



class TwoD(Button):
    obj = []
    def __init__(self):
        super().__init__(model='', scale=0)

    def Create_obj(self):
        def test():
            obj.add_obj(Model=dpg.get_value('model'))
        with dpg.window(label="Create object", height=300, width=300, pos=(100,0)):
            dpg.add_text("")
            dpg.add_input_text(label="Name", default_value="A10", tag='name')
            dpg.add_input_text(label="Model", default_value="freeModels/model/scene.gltf", tag='model')
            dpg.add_button(label="Create", callback=test)

    def btns(self):
        dpg.add_button(label='new object', callback=self.Create_obj, width=200, height=55)

    def input(self, key):
        if key == 'm':
            dpg.create_context()
            with dpg.window(label="EngineX", height=600, width=600):
                dpg.add_text("")
                self.btns()
            dpg.create_viewport(title='EngineX', width=600, height=600)
            dpg.setup_dearpygui()
            dpg.show_viewport()
            dpg.start_dearpygui()
            dpg.destroy_context()
        if key == 'd':
            camera.rotation_y += 1
        if key == 'a':
            camera.rotation_y -= 1
        if key == 's':
            camera.rotation_x += 1
        if key == 'w':
            camera.rotation_x -= 1
