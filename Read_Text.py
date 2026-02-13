def file(name):
    with open(name, 'r', encoding='utf-8') as f:    # 读取文件
        text = f.read()

    for char in '.,!?;:"()':                        # 清理标点符号
        text = text.replace(char, ' ')

    words = text.lower().split()                    # 统一小写、按空格划分单词

    freq = {}                                       # 字典统计词频
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    list = []                                      # 转换为列表
    for word, count in freq.items():
        list.append((word, count))

    n = len(list)                                  # 冒泡排序
    for i in range(n):
        for j in range(0, n - i - 1):
            if list[j][1] < list[j + 1][1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp

    print(f"文件: {name}")                           # 输出结果
    print(f"单词总数: {len(words)}")
    print(f"不同单词数: {len(freq)}")
    print("高频词:")
    for i in range(min(10, n)):
        word, count = list[i]
        print(f"{i + 1:2d}. {word:15s} : {count:3d}")

file("The Gift of the Magi.txt")                                  # 调用文件
