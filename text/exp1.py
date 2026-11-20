# 输入
lstA = list(map(int, input("请输入列表A，空格分隔：").split()))
lstB = list(map(int, input("请输入列表B，空格分隔：").split()))
# zip会自动匹配到短列表结束
res_dict = dict(zip(lstA, lstB))
print(res_dict)