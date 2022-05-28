import dearpygui.dearpygui as dpg
from Editor.gui.vs import *
from Editor.gui.error_window import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Main:
    def __init__(self, obj):
        self.obj = obj

        
    objects = {}

    def Create_obj(self):
        def create():
            self.objects[dpg.get_value('name')] = {'model':dpg.get_value('model'), 'color':dpg.get_value('color'),'pos':tuple(int(i) for i in dpg.get_value('pos'))} 
            self.obj.add_obj(Model=dpg.get_value('model'), 
            Position=tuple(int(i) for i in dpg.get_value('pos')), 
            Color=dpg.get_value('color'))
            
        with dpg.window(label="Create object", height=500, width=500, pos=(100,0)):
            dpg.add_text("")
            dpg.add_input_text(label="Name", default_value="New Object", tag='name')
            dpg.add_input_text(label="Model", default_value="cube", tag='model')
            dpg.add_input_text(label="Position", default_value="525", tag='pos')
            dpg.add_input_text(label="Color", tag='color')
            dpg.add_text("")
            dpg.add_button(label="Create", callback=create)

    def Objects(self):
        with dpg.window(label="Objects", height=500, width=200, pos=(100,0)):
            for k, v in self.objects.items():
                dpg.add_text(k)
                model = v['model']
                color = v['color']
                pos = v['pos']
                with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Left, modal=True, tag="modal_id"):
                    dpg.add_text(f'model: {model} \ncolor: {color}\npos: {pos}')
                    dpg.add_text("")
    def Run(self):
        try:
            self.position = self.cam.position
            self.rotation = self.cam.rotation
            self.scale = self.cam.scale
        except Exception as e:
            Error_Window_Tk().err_win_tk(e)
        

    def add_camera(self):
        self.cam = self.obj.add_obj(Model='camera/model/scene.gltf', 
            Position=(5, 2, 5))

    def btns(self):
        dpg.add_button(label='run', callback=self.Run, width=200, height=55)
        dpg.add_button(label='new object', callback=self.Create_obj, width=200, height=55)
        dpg.add_button(label='camera', callback=self.add_camera, width=200, height=55)
        dpg.add_button(label='objects', callback=self.Objects, width=200, height=55)
        

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