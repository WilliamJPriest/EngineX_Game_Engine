from ursina import *
from Editor import obj
from Editor.gui.main import *
import threading
from Editor.gui.error_windows import *
from ursina.prefabs.first_person_controller import FirstPersonController

class TwoD(Button, Main, Error_Window, obj.Render):
    def __init__(self):
        self.render_all()
        super().__init__(model='', scale=0)
        Main.__init__(self, obj)

    key = None
    
    def input(self, key):
        self.key = key

        if not Play:
            if key == 'm':
                
                run_main = threading.Thread(target=self.run_main)
                run_main.start()
                
            if key == 'd':
                camera.rotation_y += 5
                
            if key == 'a':
                camera.rotation_y -= 5
                
            if key == 's':
                camera.rotation_x += 5
                
            if key == 'w':
                camera.rotation_x -= 5
                
            if key == 'r':
                self.running = True

            if key == 'q':
                self.running = False

            if key == 'l':
                self.render_all()

            if key == '3':
                FirstPersonController()

            if key == '2':
                FirstPersonController().disable()
        else:
            self.OnClick(key)
