# coding=utf-8
import turtle
import time

turtle.begin_poly()  
# 同时设置pencolor=color1, fillcolor=color2
turtle.color("red")
  
#turtle.begin_fill()
for i in range(50):
	turtle.circle(i*10)
	turtle.left(126)
  
turtle.mainloop()