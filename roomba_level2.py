# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 2 version of the room
window = room.draw_room(level = 2)

###
# Start your code here
forward(560)
left (90)
forward(760)
left(90)
forward(560)
left(90)
forward(720)
left(90)
forward(520)
for _ in range (9):
    left(90)
    forward(40)
    left(90)
    forward(480)
    right(90)
    forward(40)
    right(90)
    forward(480)


 
 
# End your code here
###
 
window.exitonclick()