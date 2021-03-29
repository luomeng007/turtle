# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/3/29 9:08
software: PyCharm

Description:
    draw single dot
"""

import turtle as tt


def drawDot():
    tt.reset()
    # hide turtle
    tt.ht()
    tt.dot(20, 'Green')


drawDot()
tt.mainloop()
