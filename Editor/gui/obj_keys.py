import threading

class Keys:
    def GUI_Keys(self, key):
        if key == '1':
            run_vs = threading.Thread(target=self.run_vs)
            run_vs.start()

        if key == '2':
            pass
    def Mov_Keys(self, key):
        if key == 'g':
            self.origin_x += 1
        if key == 'h':
            self.origin_x -= 1
        if key == 'b':
            self.origin_y += 1
        if key == 'delete':
            self.disable()
        if key == 'y':
            self.origin_y -= 1
        if key == 'j':
            self.origin_z -= 1
        if key == 'k':
            self.origin_z += 1
        if key == 'o':
            self.rotation_x -= 1
        if key == 'm':
            self.rotation_x += 1
        if key == 'p':
            self.rotation_y -= 1
        if key == 'l':
            self.rotation_y += 1
        if key == 'c':
            self.scale_x -= 0.1
        if key == 'v':
            self.scale_x += 0.1
        if key == 'z':
            self.scale_y -= 0.1
        if key == 'x':
            self.scale_y += 0.1
