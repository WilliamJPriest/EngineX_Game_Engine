from turtle import pos
import dearpygui.dearpygui as dpg
from pygame import Color


class Main:
    def __init__(self, obj):
        self.obj = obj

    def Create_obj(self):

        def create():
            self.obj.add_obj(Model=dpg.get_value('model'), 
            Position=tuple(int(i) for i in dpg.get_value('pos')), 
            Color=dpg.get_value('color'))
            
        with dpg.window(label="Create object", height=500, width=500, pos=(100,0)):
            dpg.add_text("")
            dpg.add_input_text(label="Name", default_value="A10", tag='name')
            dpg.add_input_text(label="Model", default_value="freeModels/model/scene.gltf", tag='model')
            dpg.add_input_text(label="Position", default_value="525", tag='pos')
            dpg.add_input_text(label="Color", tag='color')
            dpg.add_text("")
            dpg.add_button(label="Create", callback=create)

    def objects(self):
        ''
        

    def btns(self):
        dpg.add_button(label='new object', callback=self.Create_obj, width=200, height=55)
        dpg.add_button(label='objects', callback=self.objects, width=200, height=55)

    def run_main(self):
        dpg.create_context()
        with dpg.window(label="EngineX", height=600, width=600):
            dpg.add_text("")
            self.btns()
        dpg.create_viewport(title='EngineX', width=800, height=800)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
