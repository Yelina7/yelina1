# 输入三位整数
num = int(input("请输入一个三位整数："))
a = num // 100        # 百位
b = num // 10 % 10    # 十位
c = num % 10          # 个位
sum_val = a + b + c
print(f"百位{a} + 十位{b} + 个位{c} = {sum_val}")