'''
for 循环
for 变量 in 范围:
    要循环的代码
'''

# 用range生成一个范围
# for i in range(3):
#     print(i)


# a_list = [1,2,3,4]
# for i in a_list:
#     print(i)
data = [
    [-225,0,'blue',100],
    [0,0,'black',100],
    [225,0,'red',100],
    [-112.5,-100,'orange',100],
    [112.5,-100,'green',100]
]

for i in data:
    print(i[2])

