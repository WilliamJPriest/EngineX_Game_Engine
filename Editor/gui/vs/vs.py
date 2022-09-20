import dearpygui.dearpygui as dpg
from Editor.gui.error_windows import Error_Window
from Editor.add_obj import  *
from Editor.project import  *

class Object(Error_Window, Add_obj):
    def add_to_OnClickFile(self):
        f = open(on_clickFile, 'r').read()
        y = json.loads(f)
        pos_l, pos_r = 300, 0
        
        for k, v in y.items():
            Key = dpg.get_value(f'onclick {k}')
            changes = {'name':self.Name,'model':dpg.get_value(f'model{k}'), 'gravity':False,'pos':self.to_tuple(dpg.get_value(f'position {k}')), 'scale':self.to_tuple(dpg.get_value(f'scale {k}')), 'color':''}
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
            self.model = dpg.get_value(f'model')
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



            
    def create_node(self):
        with dpg.node_editor(callback=self.link_callback, delink_callback=self.delink_callback, tag='ne'):
            f = open(on_clickFile, 'r').read()
            y = json.loads(f)
            pos_l, pos_r = 300, 0
            
            for k, v in y.items():
                def del_():
                    y.pop(k)
                    d = json.dumps(y)
                    f = open(on_clickFile, "w")
                    f.write(d)
                    f.close()

                with dpg.node(label=f'{self.Name}-{k}'.upper(), tag = k):
                    with dpg.node_attribute(label=f"Node A4"):
                        dpg.add_input_text(label=f"Name", width=150, default_value=self.Name + '-up', tag=f'name {k}')
                        dpg.add_input_text(label=f"Model", width=150, default_value=self.Model, tag=f'model {k}')
                        dpg.add_button(label=f'Color', callback=self.color_picker)
                        dpg.add_input_text(label=f'Position', width=150, default_value=self.position, tag=f'position {k}')
                        dpg.add_input_text(label=f'replace obj', width=150, tag=f'replace {k}')
                        dpg.add_input_text(label=f'add obj', width=150, tag=f'add {k}')
                        dpg.add_input_text(label=f'Scale', width=150, default_value=self.scale, tag=f'scale {k}')
                        dpg.add_checkbox(label=f'Gravity', tag=f'gravity {k}')
                        dpg.add_viewport_drawlist()
                        # dpg.add_button(label='Change', callback=self.change)
                        dpg.add_button(label='del', callback=del_)
                with dpg.node(label="OnClick", pos=(pos_l, pos_r)):
                    with dpg.node_attribute(label="Node A1", attribute_type=dpg.mvNode_Attr_Output):
                        dpg.add_input_text(label="onClick", width=50, default_value=k, tag=f'onclick {k}')

                pos_l += 300
                pos_r + 100

    def object(self):
        dpg.create_context()
        with dpg.window(label=f"{self.Name}", width=1000, height=500):
            self.create_node()
            
                        
    def run_vs(self):
        dpg.create_context()
        self.object()
        dpg.create_viewport(title='EngineX', width=1000, height=500)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()




