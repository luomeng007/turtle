# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:20:33 2020

@author: 15025

the turtle in pycharm is more fluent than in Anaconda Spyder
"""

import turtle

# 1.the default direction of turtle is right
# turtle moves towards right 20 units
# turtle.forward(20)    # same as turtle.fd()
# turtle.backward(20)     # same as turtle.bk() or turtle.back


# 2.turtle.goto(x, y): go to a specific coordinate on the screen
# on our screen, x direction towards right and y direction towards up
# turtle.goto(0, 100)
# turtle.goto(0, -100)
# turtle.goto(100, 0)
# turtle.goto(-100, 0)


# 3.turtle.seth() change the turtle direction
# we could compare this with cartesian coordinate
# angle:
#   0 - east - right direction
#   90 - north - up direction
#   180 - west - left direction
#   270 - south - down direction
# turtle.seth(0)
# turtle.seth(90)
# turtle.seth(180)
# turtle.seth(270)


# 4. turtle.rotate(): parameter: angle, rotate turtle along a direction
# turtle rotate clockwise for 20 degree
# turtle.right(20)     # same as turtle.rt()
# turtle rotate anticlockwise for 20 degree
# turtle.left(20)     # same as turtle.lt


# 5.turtle.setposition(): move turtle to a absolute position
# but we need to know the original position is (0, 0), the default direction will not change---right
# turtle.setposition(200, 200)  # same as turtle.set(200, 200)


# 6.turtle.home(): move turtle to (0, 0)


# 7.turtle.circle(): draw a circle, anticlockwise, the center is up the origin, at (0, 100)
# turtle.circle(100, 270)
# turtle.goto(0, 100)


# 8.turtle.exitonclick(): realise click to quit gui window


# debug, mainloop is needed for debug turtle.
turtle.mainloop()
