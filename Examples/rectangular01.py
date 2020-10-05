# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:47:16 2020

@author: 15025
"""

import turtle 


class Picture:
    def drawRectangular(self):
        obj = turtle.Turtle()
        
        # Loop 4 times. Everything I want to repeat is 
        # *indented* by four spaces.
        for i in range(4):
            obj.forward(50)
            obj.right(90)
            
        # This isn't indented, so we aren't repeating it.
        turtle.done()
        
        
if __name__ == "__main__":
    main = Picture()
    main.drawRectangular()
