import turtle

p = turtle.Pen()

# 设定填充的颜色
p.fillcolor('red')

# ctrl+/  注释快捷键
p.forward(100)
p.right(90)
p.forward(100)
p.right(90)
# 开始填充
p.begin_fill()
p.forward(100)
p.right(90)
p.forward(100)
p.right(90)
# 结束填充
p.end_fill()


turtle.done()