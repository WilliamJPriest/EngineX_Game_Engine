import dearpygui.dearpygui as dpg
from Editor.gui.error_window import Error_Window

class Object(Error_Window):
    key = None
    def link_callback(self, sender, app_data):
        dpg.add_node_link(app_data[0], app_data[1], parent=sender)

        if dpg.get_value('onclick'):
            while self.key != 'q':
                if self.key == dpg.get_value('onclick'):
                    self.change()

    def delink_callback(self, sender, app_data):
        dpg.delete_item(app_data)

    def color_picker(self):
        with dpg.window(label="Color"):
            dpg.add_color_picker(tag='Color')
    
    def change(self):
        def to_tuple(pos):
            lst = []
            for i in pos:
                try:
                    lst.append(int(i))
                except:
                    pass
            return tuple(lst)

        try:
            self.model = dpg.get_value('model')
            self.position = to_tuple(dpg.get_value('position'))
            self.color = tuple(dpg.get_value('Color'))
            self.scale = to_tuple(dpg.get_value('scale'))
        except Exception as e:
            self.err_win(dpg, e)
            
    def create_node(self, onclick=''):
        with dpg.node_editor(callback=self.link_callback, delink_callback=self.delink_callback):
            with dpg.node(label=self.model):
                with dpg.node_attribute(label="Node A4"):
                    dpg.add_input_text(label="Model", width=150, default_value=self.model, tag='model')
                    dpg.add_button(label='Color', callback=self.color_picker)
                    dpg.add_input_text(label='Position', width=150, default_value=self.position, tag='position')
                    dpg.add_input_text(label='Scale', width=150, default_value=self.scale, tag='scale')
                    dpg.add_button(label='Change', callback=self.change)
            with dpg.node(label="OnClick", pos=(300, 0)):
                with dpg.node_attribute(label="Node A1", attribute_type=dpg.mvNode_Attr_Output):
                    dpg.add_input_text(label="onClick", width=50, default_value=onclick, tag='onclick')

            #with dpg.node(label="OnCollision", pos=(400, 0)):
            #    with dpg.node_attribute(label="Node A1", attribute_type=dpg.mvNode_Attr_Output):
            #        ''


    def object(self):
        dpg.create_context()
        with dpg.window(label=f"Object {self.model}", width=1000, height=500):
            self.create_node()
            
                        
    def run_vs(self):
        dpg.create_context()
        self.object()
        dpg.create_viewport(title='EngineX', width=1000, height=500)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()