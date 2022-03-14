import turtle

p = turtle.Pen()

# 定义一个移动笔的函数
def move_pen(x,y):
    p.up()
    p.goto(x,y)
    p.down()

# 1. 先画一个最外层的大圆，白底的
# 先将笔往下方移动，目的是确保太极在画板的中间
move_pen(0,-100)
# 画一个半径为200的大圆
p.circle(200)

# 2. 画两个半圆，连成中间的分割线，并填充上黑色
p.fillcolor('black')
p.begin_fill()
# 2.1 先画一个左半圆
# 半圆的直径为大圆的半径，半圆的半径就是100
p.circle(100,180)
# 2.2 再画一个右半圆
p.circle(-100,180)
# 两个半圆就能够连成中间的分割线
# 画完两个半圆之后的填充，不符合预期，因此补画一个大的半圆，将笔回到起始点，然后再填充
p.circle(-200,180)
p.end_fill()

# 3. 画剩下的两个小圆
# 3.1 先画下方的小圆
# 移动的坐标点，为下方的半圆的圆心，位置可自己调整
move_pen(0,0)
p.begin_fill()
# 小圆的半径，自己定的是30，可随心调整
p.circle(30)
p.end_fill()

# 3.2 再画上方的小圆
# 移动的坐标点，为上方的半圆的圆心，位置可自己调整
move_pen(0,200)
p.fillcolor('white')
p.begin_fill()
# 小圆的半径，自己定的是30，可随心调整
p.circle(-30)
p.end_fill()

# 隐藏画笔的箭头
p.hideturtle()

# 将画的图，保存为eps格式的文件
ts = turtle.getscreen()
ts.getcanvas().postscript(file='test.eps')

# 利用PIL库，将eps文件转为jpg文件，PIL需要安装
from PIL import Image
im = Image.open('test.eps')
im.save('test.jpg','JPEG')


# turtle.done()

