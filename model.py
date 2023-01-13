import controller
import model   # Pass a reference to this module when calling each update in update_all

#Use the reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
all_simul = set()
k = ""

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, all_simul, k
    running = False
    cycle_count = 0
    all_simul = set()
    k = ""


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global running, cycle_count
    running = False
    cycle_count += 1
    temp = set(k for k in all_simul)
    for i in temp:
        i.update(model)


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global k
    k = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if k == "Ball":
        add(Ball(x,y))
    elif k == "Floater":
        add(Floater(x,y))
    elif k == "Black_Hole":
        add(Black_Hole(x,y))
    elif k == "Pulsator":
        add(Pulsator(x,y))
    elif k == "Hunter":
        add(Hunter(x,y))
    elif k == "Special":
        add(Special(x,y))
    elif k == "Remove":
        temp = set(k for k in all_simul)
        for i in temp:
            if i.contains((x,y)):
                remove(i)


#add simulton s to the simulation
def add(s):
    global all_simul
    all_simul.add(s)

# remove simulton s from the simulation    
def remove(s):
    global all_simul
    all_simul.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    true_simul = set()
    for i in all_simul:
        if p(i):
            true_simul.add(i)
    return true_simul


#call update for every simulton (passing each model) in the simulation
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        temp = set(k for k in all_simul)
        for i in temp:
            i.update(model)

#To animate: first delete every simulton from the canvas; then call display on
#  each simulton being simulated to add it back to the canvas, possibly in a
#  new location; also, update the progress label defined in the controller
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for i in all_simul:
        i.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(cycle_count)+" cycles/"+str(len(all_simul))+" simultons")
