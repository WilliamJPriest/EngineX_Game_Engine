import threading
import json

class Keys:
    def GUI_Keys(self, key):
        if key == '1':
            run_vs = threading.Thread(target=self.run_vs)
            run_vs.start()
        
    def Mov_Keys(self, key):
        if key == 'g':
            self.origin_x += 1
        if key == 'h':
            self.origin_x -= 1
        if key == 'b':
            self.origin_y += 1
        if key == 'delete':
            
            f = open('objects.txt', 'r').read()
            objects = json.loads(f)
            objects.pop(self.Name)
            d = json.dumps(objects)
            f = open("objects.txt", "w")
            f.write(d)
            f.close()
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

        def to_tuple(pos):
            lst = []
            for i in pos:
                try:
                    lst.append(float(i))
                except:
                    pass
            return tuple(lst)

        try:
            f = open('objects.txt', 'r').read()
            objects = json.loads(f)
            object = objects[self.Name]
            object['pos'] = to_tuple(self.position)
            object['scale']= to_tuple(self.scale)
            object['origin'] = to_tuple(self.origin)
            d = json.dumps(objects)
            f = open("objects.txt", "w")
            f.write(d)
            f.close()
        except:
            pass
