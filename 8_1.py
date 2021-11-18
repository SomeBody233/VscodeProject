import turtle as t
#导入turtle模块
#定义函数
def DrawCricle(n):
    for i in range(4):
        t.fd(n)#往前走
        t.lt(90)#左转90°
t.pensize(2)#笔的大小
t.speed(5)#海龟的速度
for i in range(50,300,50):
    DrawCricle(i)
t.hideturtle()#隐藏画笔海龟
t.done()