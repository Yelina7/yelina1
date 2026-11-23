s = input("输入任意字符串：")
freq = {}
for ch in s:
    if ch.isalnum():  # 判断是否是字母或数字
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
print("字母数字频次字典：", freq)
