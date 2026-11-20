p1 = list(map(int, input("输入第一个点坐标x y：").split()))
p2 = list(map(int, input("输入第二个点坐标x y：").split()))
d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
print(d)