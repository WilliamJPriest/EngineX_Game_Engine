import dearpygui.dearpygui as dpg

class Input:
    def __init__(self, window_label, button_label, input_tag,input_label, callback, width=600, height=200,**kwargs):
        self.window_label = window_label
        self.button_label = button_label
        self.input_label = input_label
        self.width = width
        self.input_tag = input_tag
        self.height = height
        self.callback = callback

    def get_text(self):
        return dpg.get_value(self.input_tag)

    def run_input(self):
        dpg.create_context()

        with dpg.window(label=self.window_label):
            dpg.add_button(label=self.button_label, callback=self.callback)
            dpg.add_input_text(label=self.input_label, tag=self.input_tag)

        dpg.create_viewport(title=self.window_label, width=self.width, height=self.height)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()