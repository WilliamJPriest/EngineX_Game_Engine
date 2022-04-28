from Editor import obj, Editor_window



e = Editor_window.Window()
e.Win2D()

obj.add_2dobj(Model='model/scene.gltf')
Editor_window.win.run()

