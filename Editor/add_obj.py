class Add_obj:

    objects = {}

    def add(self, Model, Position:tuple, Color, Name, **kwargs):
        self.objects[Name] = {
        'model':Model, 
        'color':Color,
        'pos':tuple(int(i) for i in Position)
        }