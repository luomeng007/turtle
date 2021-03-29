# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/3/29 9:01
software: PyCharm

Description:
    fill color
"""

import turtle as tt


def fillColor():
    tt.reset()
    tt.pencolor('Red')
    tt.fillcolor('Blue')
    tt.begin_fill()
    tt.goto(100, 100)
    tt.goto(200, 0)
    tt.goto(0, 0)
    tt.end_fill()


fillColor()
tt.mainloop()