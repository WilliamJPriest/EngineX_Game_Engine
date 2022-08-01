from cProfile import label
import dearpygui.dearpygui as dpg
from Editor.gui.error_windows import Error_Window
from Editor.add_obj import  *
from Editor.project import  *

class Object(Error_Window, Add_obj):
    def add_to_OnClickFile(self):
        Key = dpg.get_value('onclick')
        changes = {'name':self.Name,'model':dpg.get_value('model'), 'pos':self.to_tuple(dpg.get_value('position')), 'scale':self.to_tuple(dpg.get_value('scale')),'color':''}
        f = open(on_clickFile, 'r').read()
        on_click = json.loads(f)
        on_click[Key] = changes
        y = json.dumps(on_click)
        f = open(on_clickFile, "w")
        f.write(y)
        f.close()
        
    key = None


    def link_callback(self, sender, app_data):
        dpg.add_node_link(app_data[0], app_data[1], parent=sender)
        print(dpg.get_value('ne'))
        self.add_to_OnClickFile()

    def delink_callback(self, sender, app_data):
        dpg.delete_item(app_data)

    def color_picker(self):
        with dpg.window(label="Color"):
            dpg.add_color_picker(tag='Color')


    def to_tuple(self, pos):
            lst = []
            for i in pos:
                try:
                    lst.append(int(i))
                except:
                    pass
            return tuple(lst)
    
    def change(self):
        try:
            self.model = dpg.get_value('model')
            self.position = self.to_tuple(dpg.get_value('position'))
            self.color = ''#self.to_tuple(dpg.get_value('Color'))
            self.scale = self.to_tuple(dpg.get_value('scale'))
            self.Gravity = dpg.get_value('gravity')
            f = open(objectsFile, 'r').read()
            y = json.loads(f)
            y[self.Name]['model'] = dpg.get_value('model')
            y[self.Name]['pos'] = self.to_tuple(dpg.get_value('position'))
            y[self.Name]['color'] = ''
            y[self.Name]['scale'] = self.to_tuple(dpg.get_value('scale'))
            if self.Gravity:
                y[self.Name]['gravity'] = True
            d = json.dumps(y)
            f = open(objectsFile, "w")
            f.write(d)
            f.close()
        except Exception as e:
            self.err_win(dpg, e)

            
    def create_node(self, onclick='up'):
        with dpg.node_editor(callback=self.link_callback, delink_callback=self.delink_callback, tag='ne'):            
            with dpg.node(label=str(self.Model).upper()):
                with dpg.node_attribute(label="Node A4"):
                    dpg.add_input_text(label="Model", width=150, default_value=self.Model, tag='model')
                    dpg.add_button(label='Color', callback=self.color_picker)
                    dpg.add_input_text(label='Position', width=150, default_value=self.position, tag='position')
                    dpg.add_input_text(label='Scale', width=150, default_value=self.scale, tag='scale')
                    dpg.add_checkbox(label='Gravity', tag='gravity')
                    dpg.add_viewport_drawlist()
                    dpg.add_button(label='Change', callback=self.change)
            with dpg.node(label="OnClick", pos=(300, 0)):
                with dpg.node_attribute(label="Node A1", attribute_type=dpg.mvNode_Attr_Output):
                    dpg.add_input_text(label="onClick", width=50, default_value=onclick, tag='onclick')

    def object(self):
        dpg.create_context()
        with dpg.window(label=f"{self.Name}", width=1000, height=500):
            dpg.add_button(label='create On Click', parent='ne')
            self.create_node()
            
                        
    def run_vs(self):
        dpg.create_context()
        self.object()
        dpg.create_viewport(title='EngineX', width=1000, height=500)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()




