from Editor import obj, Editor_window



e = Editor_window.Window()
e.Win()

obj.add_obj(Model='model/scene.gltf')
Editor_window.win.run()
