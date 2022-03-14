
# data这个列表里面有5个值，每一个值又是一个列表，每个值里面又包含4个值
data = [
    [-225,0,'blue',100],
    [0,0,'black',100],
    [225,0,'red',100],
    [-112.5,-100,'orange',100],
    [112.5,-100,'green',100]
]

# 如果我想取出red，怎么取
#data[2][2]

#range(5) 产生一个范围，范围里面的值是0,1,2,3,4
# i从这个范围里面取值，一次取一个
# 首先取0，i的值就为0，其次取1，i的值就为1...
# data[0],data[1]...
for i in range(5):
    print(data[i][2])
    print('=======')
#
#
#
# i = 0
# print(data[i])
# i = 1
# print(data[i])
# i = 2
# print(data[i])
#
# for i in range(3):
#     print(i)
#     print(data[i])
#     print('======')