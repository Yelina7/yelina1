excellent = 0
good = 0
medium = 0
pass_ = 0
fail = 0
count = 0
max_score = 10

print("====成绩统计====")
print("请输入成绩（0-100），输入-1提前结束，最多输入10个")
while count < max_score:
    score = int(input("请输入成绩："))
    if score == -1:
        break
    if not (0 <= score <= 100):
        print("成绩无效，请输入0~100！")
        continue
    count += 1
    if score >= 90:
        excellent += 1
    elif score >= 80:
        good += 1
    elif score >= 70:
        medium += 1
    elif score >= 60:
        pass_ += 1
    else:
        fail += 1

print(f"\n统计结果：")
print(f"优：{excellent}人")
print(f"良：{good}人")
print(f"中：{medium}人")
print(f"及格：{pass_}人")
print(f"不及格：{fail}人")
