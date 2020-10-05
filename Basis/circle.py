# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 06:47:02 2020

@author: 15025

if we set the steps, the figure will be drawed with straight lines
"""

import turtle


class Debug:
    def __init__(self, radius:float, extent: float, steps:int):
        # when radius is position, direction is anticlockwise
        # when radius is negative, direction is clockwise 
        self.radius = radius
        self.extent = extent
        self.steps = steps
        
    def drawCircle(self):
        # turtle.circle(self.radius, self.extent, self.steps)
        turtle.circle(self.radius, self.extent)
        

if __name__ == "__main__":
    main = Debug(80, 180, 3)
    main.drawCircle()
