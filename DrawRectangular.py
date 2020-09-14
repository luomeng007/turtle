import turtle
"""
draw a rectangular
problem: why everytime we second time run this program, it will arouse an error:
Traceback (most recent call last):

  File "C:\documents\pythonProgram\python100Day\pictureDraw.py", line 5, in <module>
    turtle.pensize(4)    

"""


# set the width of pen
turtle.pensize(4)
# set the color of pen
turtle.pencolor('red')
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
# start draw
turtle.mainloop()


