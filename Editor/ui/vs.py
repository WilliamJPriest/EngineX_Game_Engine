import dearpygui.dearpygui as dpg


class Object:
    def object(self):
        dpg.create_context()

        def link_callback(sender, app_data):
            dpg.add_node_link(app_data[0], app_data[1], parent=sender)
            print(dpg.get_value('test'))

        def delink_callback(sender, app_data):
            dpg.delete_item(app_data)

        with dpg.window(label="Object", width=800, height=500):
            dpg.add_button(label='create')
            
            with dpg.node_editor(callback=link_callback, delink_callback=delink_callback):
                with dpg.node(label=self.model, pos=(1, 100)):
                    with dpg.node_attribute(label="Animation"):
                        dpg.add_input_text(tag='animation')
                        