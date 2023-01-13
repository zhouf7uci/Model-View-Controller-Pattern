# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey


class Ball(Prey): 
    radius = 5
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,0,5)
        Prey.randomize_angle(self)
        
    def update(self, model):
        Prey.move(self)
        Prey.wall_bounce(self)
    
    def display(self,canvas):
        xy = Prey.get_location(self)
        canvas.create_oval(xy[0] - Ball.radius, xy[1] - Ball.radius, xy[0] + Ball.radius, xy[1] + Ball.radius, fill='Blue')
