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



data = [
    [-225,0,'blue',100],
    [0,0,'black',100],
    [225,0,'red',100],
    [-112.5,-100,'orange',100],
    [112.5,-100,'green',100]
]

# for i in range(5):
#     draw_circle(data[i][0],data[i][1],data[i][2],data[i][3])

for i in data:
    draw_circle(i[0],i[1],i[2],i[3])

turtle.done()

