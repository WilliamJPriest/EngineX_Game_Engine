import dearpygui.dearpygui as dpg
from Editor.gui.error_windows import Error_Window
from Editor.add_obj import  *
from Editor.project import  *

class Object(Error_Window, Add_obj):
    key = None
    def link_callback(self, sender, app_data):
        dpg.add_node_link(app_data[0], app_data[1], parent=sender)
        print(dpg.get_selected_nodes('ne'))
        def run():
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
            self.color = ''#to_tuple(dpg.get_value('Color'))
            self.scale = to_tuple(dpg.get_value('scale'))
            f = open(objectsFile, 'r').read()
            y = json.loads(f)
            y[self.Name]['model'] = dpg.get_value('model')
            y[self.Name]['pos'] = to_tuple(dpg.get_value('position'))
            y[self.Name]['color'] = ''
            y[self.Name]['scale'] = to_tuple(dpg.get_value('scale'))
            d = json.dumps(y)
            f = open(objectsFile, "w")
            f.write(d)
            f.close()
        except Exception as e:
            self.err_win(dpg, e)

    def create_node():
        ''
            
    def create_node_vs(self, onclick=''):
        with dpg.node_editor(callback=self.link_callback, delink_callback=self.delink_callback, tag='ne'):
            
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


    def object(self):
        dpg.create_context()
        with dpg.window(label=f"Object {self.model}", width=1000, height=500):
            self.create_node()
            
                        
    def run_vs(self):
        import os, sys, inspect
        from qtpy.QtWidgets import QApplication

        sys.path.insert(0, os.path.join( os.path.dirname(__file__), "..", ".." ))

        from nodeeditor.utils import loadStylesheet
        from nodeeditor.node_editor_window import NodeEditorWindow




        
        app = QApplication(sys.argv)

        wnd = NodeEditorWindow()
        wnd.nodeeditor.addNodes()
        module_path = os.path.dirname( inspect.getfile(wnd.__class__) )

        loadStylesheet( os.path.join( module_path, 'qss/nodestyle.qss') )

        sys.exit(app.exec_())




