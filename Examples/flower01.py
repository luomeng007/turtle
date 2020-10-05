# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:47:16 2020

@author: 15025

draw flower
"""

import turtle 


class Picture:
    def drawRectangular(self):
        obj = turtle.Turtle()
        
        obj.penup()
        obj.setpos(-3,37)
        obj.pendown()
        
        for i in range(200):
            obj.speed(0)
            obj.color("purple")
            obj.forward(i + 10)
            obj.right(65)
            obj.color("blue")
            obj.forward(i + 10)
            obj.right(65)
        
        turtle.done()
        
        
if __name__ == "__main__":
    main = Picture()
    main.drawRectangular()