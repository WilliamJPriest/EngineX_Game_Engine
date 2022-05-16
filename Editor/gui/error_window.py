class Error_Window:
    def err_win(self, dpg, err):
        with dpg.window(label="Error"):
            dpg.add_text('')
            dpg.add_text(err)
            with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Left, modal=True, tag="modal_id"):
                dpg.add_button(label="Close", callback=lambda: dpg.configure_item("modal_id", show=False))
