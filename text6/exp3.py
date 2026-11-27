print("====10000以内的水仙花数====")
for num in range(1, 10000):
    s = str(num)
    n = len(s)  # 获取位数
    total = 0
    for c in s:
        total += int(c) ** n
    if total == num:
        print(num, end=" ")
