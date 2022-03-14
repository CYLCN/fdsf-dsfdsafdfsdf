# 引入画图的工具包
import turtle

# 生成一支笔
p = turtle.Pen()

# 设置填充的颜色
p.fillcolor('red')

# 设置笔的颜色
p.pencolor('red')
# 设置笔的速度
p.speed(1)

# 把笔拿起来
p.up()
# 调整的笔的位置，让笔到指定的坐标
p.goto(-100,0)
# 将笔放下去
p.down()

p.right(30)

p.begin_fill()
for i in range(5):
    p.forward(100)
    p.left(72)
    p.forward(100)
    p.right(144)

p.end_fill()

# 隐藏箭头
# p.hideturtle()

# p.forward(100)
# p.left(72)
# p.forward(100)
# p.right(144)
#
# p.forward(100)
# p.left(72)
# p.forward(100)
# p.right(144)

# p.forward(100)
# p.left(72)
# p.forward(100)
# p.right(144)
# p.forward(100)
# p.left(72)
# p.forward(100)


turtle.done()
