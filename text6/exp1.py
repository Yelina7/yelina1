import random

secret = random.randint(1, 100)  # 1~100随机数，可以自己改范围
max_times = 10
print("====猜数字游戏开始====")
print(f"我想好了1~100之间一个数字，你一共有{max_times}次机会！")

for i in range(1, max_times + 1):
    guess = int(input(f"第{i}次猜测，请输入数字："))
    if guess == secret:
        print(f"恭喜你猜对啦！答案就是{secret}！")
        break
    elif guess > secret:
        print("太大了！")
    else:
        print("太小了！")
else:
    # for循环正常走完（没有break）时执行，代表10次用完没猜对
    print(f"机会用完了，游戏结束！正确答案是：{secret}")
