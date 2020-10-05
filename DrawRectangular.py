# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:42:20 2020

@author: 15025
"""

import turtle
# draw a rectangular
# problem: why everytime we second time run this program, it will arouse an error:
# Traceback (most recent call last):
#   File "C:\documents\pythonProgram\python100Day\pictureDraw.py", line 5, in <module>
#     turtle.pensize(4)    


class Picture:
    def drawRectangular(self):
        # set the width of pen
        turtle.pensize(4)
        # set the color of pen
        turtle.pencolor('red')
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        # start draw
        # start event-loop, then we could close graphics through click close button of tkinter
        # turtle.done() is same as turtle.mainloop()
        turtle.mainloop()        
        

if __name__ == "__main__":
    main = Picture()
    main.drawRectangular()
