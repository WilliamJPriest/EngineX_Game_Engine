from Editor import obj, Editor_window

e = Editor_window.Window()
obj.add_obj('cube', pos=(5,2,5))
e.Win2D()
Editor_window.win.run()
