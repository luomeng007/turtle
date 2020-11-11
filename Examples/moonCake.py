# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 05:48:02 2020

@author: 15025

moon cake for Moon Festival
"""

import turtle
import math

# do not let turtle display on screen
turtle.hideturtle()
turtle.speed(15)


# the degree of turtle speed:
#   “fastest”: 0
#   “fast”: 10
#   “normal”: 6
#   “slow”: 3
#   “slowest”: 1

class MoonCake:
    def __init__(self, name: str):
        self.name = name

    def drawMoonCake(self):
        turtle.title("Blessing from Small Inkfish!")
        MoonCake.lace(200, 12)
        turtle.seth(90)
        MoonCake.drawCircle(200, 10, "#F0BE7C", "#F8CD32")
        MoonCake.drawCircle(180, 10, "#FBA92D", "#FBA92D")
        turtle.seth(0)
        MoonCake.interiorDecorativePattern()
        self.addText(-120, -40)
        # we add this and after the program finished itself, it will hold the gui window rather that close it
        turtle.done()

    @staticmethod
    def lace(r: int, n: int):
        """
        月饼的花边
        Parameters
        ----------
        r : int
            the radius of lace.
        n : int
            the total number of lace.
        """
        # lift up pen
        turtle.penup()
        # move pen to position (0, -r)
        turtle.goto(0, -r)
        # the radius of lace of moon cake
        lace_r = math.sin(math.pi / n) * r

        for i in range(n):
            # raise the paintbrush
            turtle.penup()
            # reset the paintbrush, include position and direction
            turtle.home()
            # change the direction of turtle
            turtle.seth(360 / n * i)
            # move paintbrush
            turtle.fd(r)
            # rotate paintbrush anticlockwise several unit
            turtle.left(360 / n * 0.5)
            # paintbrush falling
            turtle.pendown()
            # set color
            turtle.color("#F0BE7C")
            # fill the color of lace
            turtle.begin_fill()
            # start to draw lace
            turtle.circle(lace_r, 180)
            # end the process of filling color
            turtle.end_fill()

    @staticmethod
    def drawCircle(radius, linewidth, color1, color2):
        turtle.goto(radius, 0)
        turtle.color(color1)
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(radius - linewidth, 0)
        turtle.pendown()

        turtle.color(color2)
        turtle.begin_fill()
        turtle.circle(radius - linewidth)
        turtle.end_fill()

    @staticmethod
    def interiorDecorativePattern():
        turtle.color("#F5E16F")
        turtle.penup()
        turtle.goto(0, -180)
        turtle.pendown()
        for _ in range(8):
            turtle.begin_fill()
            turtle.circle(60, 120)
            turtle.left(180)
            turtle.circle(60, 120)
            turtle.end_fill()

    def addText(self, x: float, y: float):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color("Gold")
        turtle.write(self.name, font=("华文隶书", 80, "bold"))


if __name__ == "__main__":
    main = MoonCake("五仁")
    main.drawMoonCake()
