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
        
        obj.color("purple")
        obj.setpos(0,-128)
        obj.speed(4)
        obj.color("aqua")
        obj.hideturtle()
        obj.shape("square")
        obj.circle(10)
        obj.circle(15)
        obj.circle(20)
        obj.circle(25)
        obj.speed(6)
        obj.circle(30)
        obj.circle(35)
        obj.circle(40)
        obj.circle(45)
        obj.speed(7)
        obj.circle(50)
        obj.circle(55)
        obj.circle(60)
        obj.circle(65)
        obj.speed(8)
        obj.circle(70)
        obj.circle(75)
        obj.circle(80)
        obj.circle(85)
        
        turtle.done()
        
        
if __name__ == "__main__":
    main = Picture()
    main.drawRectangular()