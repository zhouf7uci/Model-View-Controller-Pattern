# Black_Hole inherits from only Simulton, updating by finding+removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,20,20)
        
    def update(self, model):
        items = model.find(lambda i : isinstance(i, Prey) and self.contains(i.get_location()))
        temp = set(x for x in items)
        for k in temp:
            model.remove(k)
        return items
    
    def display(self, canvas):
        xy = Simulton.get_location(self)
        wh = Simulton.get_dimension(self)
        canvas.create_oval(xy[0] - wh[0]/2, xy[1] - wh[1]/2, xy[0] + wh[0]/2, xy[1] + wh[1]/2, fill='Black')
    
    def contains(self,xy):
        return Simulton.distance(self, xy) < Black_Hole.radius
