import dearpygui.dearpygui as dpg


class Object:
    key = None

    def object(self):
        dpg.create_context()

        def link_callback(sender, app_data):
            def to_tuple(pos):
                lst = []
                for i in pos:
                    try:
                        lst.append(int(i))
                    except:
                        pass
                return tuple(lst)
            dpg.add_node_link(app_data[0], app_data[1], parent=sender)
            while True:
                if self.key == dpg.get_value('onclick'):
                    self.model = dpg.get_value('model')
                    self.position = to_tuple(dpg.get_value('position'))
                    self.color = dpg.get_value('color')
                    self.scale = to_tuple(dpg.get_value('scale'))
                    break

        def delink_callback(sender, app_data):
            dpg.delete_item(app_data)

        with dpg.window(label="Object", width=1000, height=500):
            dpg.add_button(label='create')
            
            with dpg.node_editor(callback=link_callback, delink_callback=delink_callback):
                with dpg.node(label=self.model):
                    with dpg.node_attribute(label="Node A4"):
                        dpg.add_input_text(label="Model", width=150, default_value=self.model, tag='model')
                        dpg.add_input_text(label='Color', width=150, default_value=self.color, tag='color')
                        dpg.add_input_text(label='Position', width=150, default_value=self.position, tag='position')
                        dpg.add_input_text(label='Scale', width=150, default_value=self.scale, tag='scale')


                with dpg.node(label="On Click", pos=(300, 0)):
                    with dpg.node_attribute(label="Node A1", attribute_type=dpg.mvNode_Attr_Output):
                        dpg.add_input_text(label="onClick", width=50, tag='onclick')
                        
    def run_vs(self):
        dpg.create_context()
        self.object()
        dpg.create_viewport(title='EngineX', width=1000, height=500)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()