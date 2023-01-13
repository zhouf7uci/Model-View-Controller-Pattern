#subclass of Floater, except it avoids Hunters (so does the exact opposite of what a hunter does)

from hunter import Hunter
from floater import Floater
import math

class Special(Floater):
    dist = 50
    def __init__(self,x,y):
        Floater.__init__(self,x,y)
        Floater.randomize_angle(self)
        
    def update(self, model):
        predator = model.find(lambda i : isinstance(i, Hunter) and Hunter.distance(self, i.get_location()) <= Special.dist)
        hunt = [n for n in predator]
        hunt.sort(key = lambda x : Hunter.distance(self, x.get_location()))
        if len(hunt) != 0:
            xy1 = hunt[0].get_location()
            xy2 = self.get_location()
            self.set_angle(-math.atan2(xy1[1] - xy2[1], xy1[0] - xy2[0]))
            self.wall_bounce()
            self.move()
        else:
            Floater.update(self, model)
                    
    def display(self,canvas):
        xy = Floater.get_location(self)
        canvas.create_oval(xy[0] - Floater.radius, xy[1] - Floater.radius, xy[0] + Floater.radius, xy[1] + Floater.radius, fill='Orange')