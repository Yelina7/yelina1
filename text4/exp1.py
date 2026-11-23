from functools import reduce

# 输入示例：[{1,2}, {2,3}, {3,4}]
lst = eval(input("输入包含若干集合的列表："))
res = reduce(lambda a, b: a | b, lst)
print("并集：", res)
