lst = list(map(int, input("请输入整数列表，空格分隔：").split()))
new_lst = sorted(lst, reverse=True)
print(new_lst)