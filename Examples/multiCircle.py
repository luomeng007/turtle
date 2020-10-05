# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:47:16 2020

@author: 15025

draw circle
"""

import turtle 


class Picture:
    def drawRectangular(self):
        obj = turtle.Turtle()
        
        obj.hideturtle()
        obj.penup()
        obj.setpos(0,-128)
        obj.pendown()
        obj.speed(7)
        obj.color("purple")
        obj.shape("square")
        obj.begin_fill()
        obj.circle(90)
        obj.end_fill()
        obj.circle(100)
        obj.color("aqua")
        obj.circle(105)
        obj.color("purple")
        obj.circle(110)
        obj.color("aqua")
        obj.circle(115)
        obj.color("purple")
        obj.circle(120)
        obj.color("aqua")
        obj.circle(125)
        obj.color("purple")
        obj.circle(130)
        obj.color("aqua")
        obj.circle(135)
        obj.color("purple")
        obj.circle(140)
        obj.color("aqua")
        obj.circle(145)
        obj.color("purple")
        obj.circle(150)
        obj.color("aqua")
        obj.circle(155)
        obj.color("purple")
        obj.circle(160) 
        obj.pensize(6)
        obj.setpos(0,177)
        obj.showturtle()
        
        turtle.done()
        
        
if __name__ == "__main__":
    main = Picture()
    main.drawRectangular()