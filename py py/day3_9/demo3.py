# 定义一个容器，装一些值
# 常用的一个容器，列表
# 中括号包起来的[]，里面的元素，用逗号隔开
a_list = [1,2,3,['zhangsan','lisi']]
# 可以利用索引(位置)，将列表中的值取出来
# 索引，从左到右，以0开始，也就第一个值的索引是0，第二个值的索引是1....
# 通过索引0，取a_list中第一个值
# print(a_list[0])
# 通过索引1，取a_list中第二个值
# print(a_list[1])
# 通过索引2，取a_list中第三个值
# print(a_list[2])

# range 给定一个值生成一个范围，范围从0开始，到给定的值结束，不包含给定的值
# range(3) 生成的值就是0,1,2
# for i in range(4):
    # print(i)
    # print(a_list[i])

a_b = [1,2,3,['zhangsan','lisi']]
# a_list[3] 通过索引3，取a_list中第4个位置的值，也就是['zhangsan','lisi']
# 因此temp的值就是['zhangsan','lisi']
temp = a_b[3]
# temp[0] 通过索引0，取temp中第1个位置的值，也就是'zhangsan'
print(temp[0])
# 因为temp=a_list[3]，所以temp[0] 也就是a_list[3][0]
print(a_b[3][0])

