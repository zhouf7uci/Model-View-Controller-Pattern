# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    counter = 30
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self._counter = 0
        
    def update(self, model):
        items = Black_Hole.update(self, model)
        if len(items) == 0:
            self._counter += 1
            if self._counter == Pulsator.counter:   
                Black_Hole.change_dimension(self, -1, -1)
                self._counter = 0
        else:
            Black_Hole.change_dimension(self, len(items), len(items))
            self._counter = 0
            
        xy = Black_Hole.get_dimension(self)
        if xy[0] == 0 and xy[1] == 0:
            model.remove(self)
        
        return items
