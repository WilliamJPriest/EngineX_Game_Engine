import dearpygui.dearpygui as dpg

class Main_WIN:
    def Create_obj(self):
        with dpg.window(label="Create object", height=300, width=300, pos=(100,0)):
            dpg.add_text("")
            dpg.add_input_text(label="Model", default_value="cube", tag='model')
            dpg.add_button(label="Create", callback=self.val)

    def run(self):
        dpg.create_context()
        with dpg.window(label="EngineX", height=600, width=600):
            dpg.add_slider_float(label="Ground", default_value=1, max_value=100)
            dpg.add_text("")
            dpg.add_button(label='new object', callback=self.Create_obj)

        dpg.create_viewport(title='Custom Title', width=600, height=600)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

Main_WIN().run()


