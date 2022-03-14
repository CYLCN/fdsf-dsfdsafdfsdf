import turtle

p = turtle.Pen()

# from turtle import *
# p = Pen()

# a = 2
# a = 3
# print(a)


# 同样的代码，连续执行n次
# 采用循环
'''
for循环
for 变量 in 范围:
    要循环的代码
范围：可以通过range生成，给range一个整数，
它会生成一个从0开始，到给定的数结束的范围，包含0，不包含给定的数
range(3):范围就是0,1,2
python代码，采用缩进表示层级结构
'''
for i in range(3):
    p.forward(100)
    p.right(90)


# p.forward(100)
# p.right(90)
# p.forward(100)
# p.right(90)
# p.forward(100)
# p.right(90)
p.forward(100)

# hideturtle 作用是将笔的箭头给隐藏起来
p.hideturtle()

turtle.done()