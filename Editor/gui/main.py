import dearpygui.dearpygui as dpg
from Editor.gui.vs import *
from Editor.gui.error_windows import *
from ursina.prefabs.first_person_controller import FirstPersonController
from Editor.obj import *

class Main(Render):
    def __init__(self, obj):
        self.obj = obj

    def Create_obj(self):
        def create():
            self.add(Model=dpg.get_value('model'),  Scale=tuple(int(i) for i in dpg.get_value('scale')),Name=dpg.get_value('name'),Position=tuple(int(i) for i in dpg.get_value('pos')), Color=dpg.get_value('color'))
            self.render_all()

        with dpg.window(label="Create object", height=500, width=500, pos=(100,0)):
            dpg.add_text("")
            dpg.add_input_text(label="Name", default_value="New Object", tag='name')
            dpg.add_input_text(label="Model", default_value="cube", tag='model')
            dpg.add_input_text(label="Position", default_value="525", tag='pos')
            dpg.add_input_text(label="Scale", default_value="111", tag='scale')
            dpg.add_input_text(label="Color", tag='color')
            dpg.add_text("")
            dpg.add_button(label="Create", callback=create)

    def Objects(self):
        with dpg.window(label="Objects", height=500, width=200, pos=(100,0)):
            for k, v in self.objects().items():
                dpg.add_text(k)
                model = v['model']
                color = v['color']
                pos = v['pos']
                with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Left, modal=True, tag="modal_id"):
                    dpg.add_text(f'model: {model} \ncolor: {color}\npos: {pos}')
                    dpg.add_text("")
    def Run(self):
        try:
            self.cam.parent = camera.ui
        except Exception as e:
            Error_Window_Tk().err_win_tk(e)

    def add_camera(self):
        self.cam = self.add(Model='camera/model/scene.gltf',  Name='Cam 1',Position=(5, 2, 5), Color='white')
        self.render_all()

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