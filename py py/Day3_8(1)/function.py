import turtle

p = turtle.Pen()

'''
定义函数：
def 函数名(参数):
    函数体(实现功能的代码)

使用函数：
函数名(参数)
'''

# 定义函数时，设定了两个参数，x和y
def move_pen(x,y):
    p.up()
    p.goto(x,y)
    p.down()

# 使用函数时，就需要给参数x以及参数y传值
move_pen(-200,100)

move_pen(0,0)

move_pen(200,200)

turtle.done()