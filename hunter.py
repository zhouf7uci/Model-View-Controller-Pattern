# Hunter inherits from the Pulsator (1st) and Mobile_Simulton (2nd) classes:
#   updating/displaying like its Pulsator base, but also moving (either in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    dist = 200
    def __init__(self,x,y):
        Mobile_Simulton.__init__(self,x,y,20,20,0,5)
        Mobile_Simulton.randomize_angle(self)
        self._counter = 0
        
    def update(self, model):
        items = Pulsator.update(self, model)
        prey = model.find(lambda i : isinstance(i, Prey) and Pulsator.distance(self, i.get_location()) <= Hunter.dist)
        hunt = [n for n in prey]
        hunt.sort(key = lambda x : Pulsator.distance(self, x.get_location()))
        if len(hunt) != 0:
            xy1 = hunt[0].get_location()
            xy2 = Pulsator.get_location(self)
            Mobile_Simulton.set_angle(self, atan2(xy1[1] - xy2[1], xy1[0] - xy2[0]))
        Mobile_Simulton.move(self)
        Mobile_Simulton.wall_bounce(self)
        return items
