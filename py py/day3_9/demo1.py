import turtle

p = turtle.Pen()

# 设置笔的宽度
p.width(2)
# for i in range(10):
#     p.width(i)
#     p.forward(10)

# 设置笔的颜色
# p.pencolor('red')
# 设置填充的颜色
# p.fillcolor('blue')
# 同时设置笔和填充的颜色
# p.color('red','blue')
# 开始填充
# p.begin_fill()
# 结束填充
# p.end_fill()
# 向前
# p.forward(10)
# 向后
# p.back(100)
# 左转角度
# p.left(90)
# 右转角度
# p.right(90)
# 抬起笔
# p.up()
# 放下笔
# p.down()
# 移动到指定坐标
# p.goto(100,100)

# 逻辑 决定着你代码水平的高与低
# 但是我们测试的代码水平普遍要求不高

# circle  圆
# 通过指定半径以及角度来画弧线
# 第一个参数是半径，第二个参数是角度
p.circle(100)
p.up()
p.goto(150,0)
p.down()
p.circle(100)
# p.circle(-100)

turtle.done()