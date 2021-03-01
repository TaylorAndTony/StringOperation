var = input('输入需要查找最大值的数，空格分隔：')
# 将输入的数据转换成列表
var = var.split(' ')
# 临时判断用的变量
num = 0

# 对于列表中的每一个数 i
for i in var:
    # 如果 num 比 i 小，那么将 i 赋值给 num
    if num < int(i):
        num = int(i)

print(f'最大值为：{num}')
