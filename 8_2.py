import turtle
tony = turtle.Pen()#绘图状态，获取画笔

for i in range(60):
    tony.circle(i)#画圆
    tony.right(90)#画完一个圈向右转90°
    tony.speed(100)#速度为100
turtle.exitonclick()
#绘画结束后点击一下退出程序