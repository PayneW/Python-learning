'''
    第 7 章: 包、模块、函数与变量作用域
'''


# while,  while...else
counter = 1
while counter <= 10:
    counter += 1
    print(counter, end=' ')
else:
    print("EOF: end of file")


print(('*' * 76) + '\n')


# for, for...else
group = [['apple', 'banana', 'orange', 'grape'], (1, 3, 5)]
for item in group:
    for sub_item in item:
        if item == 'orange':
            break
        print(sub_item, end=' ')
else:
    print("Group EOF!")


print(('*' * 76) + '\n')


# break, continue
a = [1, 3, 5, 6, 7, 8]
for item in a:
    if item % 2 == 0:
        break
    print(item, end=' ')


print(('*' * 76) + '\n')


# 使用函数 range(): 函数 range() 轻松生成一系列的数字。
# range() 第三个参数为步长
for num in range(0, 10, 2):
    # 0 2 4 6 8
    print(num, end=' ')

print(('*' * 76) + '\n')

# 使用 range() 创建数字列表
# 使用函数 list() 将 range() 的结果直接转换为列表。
numbers = list(range(0, 11))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

print(('*' * 76) + '\n')

num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, len(num2), 2):
    # 1 | 3 | 5 | 7 | 9 |
    print(num2[i], end=' | ')

print(('*' * 76) + '\n')

# 使用切片实现间隔取数，实现方式在第三个参数上 (每隔多少个数取一个值)
num3 = num2[0: len(num2): 2]
# [1, 3, 5, 7, 9]
print(num3)




