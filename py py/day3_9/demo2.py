import turtle

p = turtle.Pen()

# 设置笔宽
p.width(3)

# 调整画板大小
# turtle.screensize(2000,750)

# 定义一个移动笔位置的函数
def move_pen(x,y):
    # 将笔抬起
    p.up()
    # 移动到指定位置
    p.goto(x,y)
    # 将笔放下
    p.down()

# 定义一个画圆的函数
# x、y表示笔的坐标，color表示笔的颜色，radius表示圆的半径
def draw_circle(x,y,color,radius):
    # 使用上面定义的move_pen函数移动笔的位置
    move_pen(x, y)
    # 设置笔的颜色
    p.color(color)
    # 根据半径画圆
    p.circle(radius)

# 调用上面定义的函数draw_circle
# 定义函数的时候，设定了笔的坐标、颜色、圆的半径
# 因此在使用时，需要传坐标，颜色、半径
# 坐标(-225,0)，颜色：blue，半径：100
draw_circle(-225,0,'blue',100)

draw_circle(0,0,'black',100)

draw_circle(225,0,'red',100)

draw_circle(-112.5,-100,'orange',100)

draw_circle(112.5,-100,'green',100)


turtle.done()

