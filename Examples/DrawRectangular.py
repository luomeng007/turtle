# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:42:20 2020

@author: 15025
"""

import turtle  


class Picture:
    def drawRectangular(self):
        # create turtle object
        obj = turtle.Turtle()
        # set the width of pen
        obj.pensize(4)
        # set the color of pen
        obj.pencolor('red')
        
        obj.forward(100)
        obj.right(90)     # Rotate clockwise by 90 degrees
        
        obj.forward(100)
        obj.right(90)
        
        obj.forward(100)
        obj.right(90)
        
        obj.forward(100)
        obj.right(90)
        
        # start draw
        # start event-loop, then we could close graphics through click close button of tkinter
        # turtle.done() is same as turtle.mainloop()
        turtle.done()        
        

if __name__ == "__main__":
    main = Picture()
    main.drawRectangular()
