class Color_Picker:
    def color_picker(self, dpg):
        with dpg.window(label="Color"):
            dpg.add_color_picker(tag='Color')
            print(dpg.get_value('Color'))