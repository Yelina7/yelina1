lst = list(map(int, input("请输入整数列表，空格分隔：").split()))
result = 1
for num in lst:
    result *= num
print(result)