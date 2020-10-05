# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:47:16 2020

@author: 15025

draw a alphabet K
"""

import turtle 


class Picture:
    def drawRectangular(self):
        obj = turtle.Turtle()
        
        obj.forward(27)
        obj.left(90)
        obj.forward(120)
        obj.right(140)
        obj.forward(158)
        obj.left(90)
        obj.forward(25)
        obj.left(90)
        obj.forward(150)
        obj.right(75)
        obj.forward(160)
        obj.left(90)
        obj.forward(25)
        obj.left(90)
        obj.forward(163)
        obj.right(145)
        obj.forward(164)
        obj.left(90)
        obj.forward(28)
        obj.left(90)
        obj.forward(305)
        
        turtle.done()
        
        
if __name__ == "__main__":
    main = Picture()
    main.drawRectangular()