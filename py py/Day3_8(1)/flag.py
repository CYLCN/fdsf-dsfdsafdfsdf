import turtle

p = turtle.Pen()

# 如果实现某一功能的一段代码，会多次使用
# 那我们可以将其封装成函数
'''
定义函数：
def 函数名(参数):
    函数体(实现功能的代码)
    
使用函数：
函数名(参数)
'''
def move_pen(x,y):
    p.up()
    p.goto(x, y)
    p.down()

def star(x):
    p.begin_fill()
    for i in range(5):
        p.forward(x)
        p.left(72)
        p.forward(x)
        p.right(144)
    p.end_fill()


# 先画长方形
# 1. 先将笔移动到左上角
move_pen(-200,200)

# 2. 画长方形
# p.pencolor('red')
# p.fillcolor('red')
# 第一个是笔的颜色，第二个是填充的颜色
# p.color('blue','red')
# 如果笔的颜色和填充的颜色一样，可以只给一个颜色
p.color('red')
p.begin_fill()
for i in range(2):
    p.forward(400)
    p.right(90)
    p.forward(200)
    p.right(90)
p.end_fill()

# 后画五角星
move_pen(-150,150)
p.color('yellow')


star(40)

move_pen(-20,170)
p.left(30)

star(10)

move_pen(-20,135)

star(10)


turtle.done()