# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/3/29 8:53
software: PyCharm

Description:
    draw triangle
"""

import turtle as tt


# draw by using direction
# def drawTriangle():
#     # clear everything on canvas
#     tt.reset()
#     tt.seth(45)
#     tt.fd(100)
#     tt.right(90)
#     tt.fd(100)
#     # let turtle go back to the center of canvas
#     tt.home()
#
#
# drawTriangle()
# tt.mainloop()
# ======================================================================================================================
# draw by using goto
def drawTriangle():
    # clear everything on canvas
    tt.goto(100, 100)
    tt.goto(200, 0)
    tt.goto(0, 0)


drawTriangle()
tt.mainloop()