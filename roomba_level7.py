# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

speed(7)

# THIS PARAMETER CAN CHANGE!!!
# Make sure your code works for n_alcoves = 0, 1, 2, 3, and 4
# (You are allowed to use this parameter in your code)
n_alcoves = 3

# Draw the Level 7 version of the room
window = room.draw_room(level = 7, n_alcoves = n_alcoves)

level_7_height = 1220
level_5_height = 560
scale_factor = level_7_height / level_5_height

###
# Start your code here
forward(560)
backward(40)


right(90)
forward(120)
right(90)
forward(320)


right(90)
forward(40)
right(90)
forward(280)


left(90)
forward(40)
left(90)
forward(280)
right(90)
forward(40)
right(90)
forward(280)
left(90)
forward(40)
left(90)
forward(280)
right(90)
forward(40)
right(90)
forward(280)
left(90)
forward(40)
left(90)
forward(280)


backward(40)
right(90)
forward(40)
right(90)
forward(40)
left(90)
right(90)
forward(200)
right(90)
forward(40)
left(90)
forward(40)
right(90)
forward(240)
right(90)
forward(40)
left(90)
forward(40)
right(90)
forward(240)
backward(120)
left(90)
forward(40)
backward(560)
forward(40)
right(90)
backward(40)
forward(80)
left(90)
forward(80)
left(90)
forward(80)
left(90)
forward(40)
right(90)
forward(40)
backward(160)
forward(80)
right(90)
forward(640)
backward(40)
right(90)
forward(40)
backward(80)
right(90)
forward(40)
right(90)
forward(40)
backward(160)
forward(40)
left(90)
forward(40)
right(90)
forward(80)
backward(40)
left(90)
forward(240)
left(90)
forward(240)
left(90)
forward(40)
backward(80)
right(90)
forward(80)
left(90)
forward(80)
left(90)
forward(80)
backward(40)
right(90)
forward(40)
backward(160)
 
# End your code here
###
 
window.exitonclick()