# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    radius = 5
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,0,5)
        Prey.randomize_angle(self)
        
    def update(self, model):
        if random() < .30:
            while True:
                i = random()
                if i >= .5:
                    s = random()
                    if s < .5:
                        Prey.set_angle(self, Prey.get_angle(self) - i)
                    else:
                        Prey.set_angle(self, Prey.get_angle(self) + i)
                break
            while True:
                i = random()
                if i >= .5:
                    s = random()
                    if s < .5:
                        Prey.set_speed(self, Prey.get_speed(self) - i)
                    else:
                        Prey.set_speed(self, Prey.get_speed(self) + i)
                break   
            if Prey.get_speed(self) < 3:
                Prey.set_speed(self, 3)
            elif Prey.get_speed(self) > 7:
                Prey.set_speed(self, 7)
        Prey.move(self)
        Prey.wall_bounce(self)
    
    def display(self,canvas):
        xy = Prey.get_location(self)
        canvas.create_oval(xy[0] - Floater.radius, xy[1] - Floater.radius, xy[0] + Floater.radius, xy[1] + Floater.radius, fill='Red')
