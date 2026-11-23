a1 = int(input("请输入首项："))
q = int(input("请输入公比（不等于1，小于36的正整数）："))
n = int(input("请输入自然数n："))

s = a1 * (q ** n - 1) / (q - 1)
s = int(s)   # 要求关键步骤使用int()
print("前n项和：", s)
