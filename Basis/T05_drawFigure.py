# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/3/29 9:14
software: PyCharm

Description:

"""

import turtle as tt


def fillColor():
    tt.pensize(50)
    tt.pencolor('LightGreen')
    # draw ground
    tt.up(), tt.goto(-400, -200), tt.down(), tt.goto(400, -200)
    # 栅栏
    tt.pensize(20), tt.pencolor('GoldEnrod')
    tt.up(), tt.goto(-400, -150), tt.down(), tt.goto(400, -150)
    tt.up(), tt.goto(-250, -200), tt.down(), tt.goto(-250, -100)
    tt.up(), tt.goto(-100, -200), tt.down(), tt.goto(-100, -100)
    tt.up(), tt.goto(30, -200), tt.down(), tt.goto(30, -100)
    tt.up(), tt.goto(300, -200), tt.down(), tt.goto(300, -100)
    # tree
    tt.pensize(30), tt.pencolor('Olive')
    tt.up(), tt.goto(-150, -200), tt.down(), tt.goto(-150, -120)
    # 树冠
    tt.pensize(1), tt.pencolor('ForestGreen')
    tt.up(), tt.goto(-80, -120), tt.down()
    tt.begin_fill(), tt.seth(60), tt.circle(80, steps=3), tt.end_fill()
    tt.up(), tt.goto(-95, -50), tt.down()
    tt.begin_fill(), tt.seth(60), tt.circle(60, steps=3), tt.end_fill()
    tt.up(), tt.goto(-110, 0), tt.down()
    tt.begin_fill(), tt.seth(60), tt.circle(40, steps=3), tt.end_fill()
    # house wall
    tt.pensize(1), tt.pencolor('RoyalBlue')
    tt.up(), tt.home(), tt.fd(70), tt.right(90), tt.down()
    tt.begin_fill(), tt.fd(200), tt.left(90), tt.fd(200), tt.left(90), tt.fd(200), tt.end_fill()
    # 烟囱
    tt.pensize(30), tt.pencolor('DimGray')
    tt.up(), tt.goto(230, 30), tt.down(), tt.goto(230, 120)
    # 房顶
    tt.pensize(1), tt.pencolor('DeepPink'), tt.up(), tt.home(), tt.down()
    tt.begin_fill(), tt.left(30), tt.fd(200), tt.right(60), tt.fd(200), tt.home(), tt.end_fill()
    # window
    tt.color('Violet'), tt.up(), tt.goto(160, -90), tt.down()
    tt.begin_fill(), tt.seth(45), tt.circle(50, steps=4), tt.end_fill()
    # door
    tt.color('Chocolate'), tt.up(), tt.goto(250, -200), tt.down(), tt.seth(90)
    tt.begin_fill(), tt.fd(120), tt.left(90), tt.fd(60), tt.left(90), tt.fd(120), tt.left(90), tt.fd(60), tt.end_fill()
    # 画炊烟
    tt.up(), tt.goto(250, 160), tt.dot(30, 'AliceBlue')
    tt.goto(270, 200), tt.dot(20, 'AliceBlue')
    tt.goto(300, 200), tt.dot(10, 'AliceBlue')
    # 太阳
    tt.goto(-260, 250), tt.dot(80, 'Gold')


fillColor()
tt.mainloop()
