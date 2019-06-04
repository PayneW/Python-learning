# Created on 20190513

# 第四章 操作列表

'''
    - 4.1 遍历整个列表
'''


'''
    - 4.2 避免缩进错误
'''

'''
    - 4.3 创建数字列表
        + 4.3.1 使用函数 range(): 函数 range() 轻松生成一系列的数字。
        + 4.3.2 使用 range() 创建数字列表
            - 使用函数 list() 将 range() 的结果直接转换为列表。
        + 4.3.3 对数字列表进行简单的统计计算: 
            - min()
            - max()
            - sum()
        + 4.3.4 列表解析 (list comprehensions): 
            - 列表解析将 for 循环和创建新元素的代码合并成一行，并自动附加新元素。
            > **comprehension /kɒmprɪ'henʃ(ə)n/  n.理解，理解力，合理**
'''
numbers = list(range(1, 6))
# [1, 2, 3, 4, 5]
print(numbers)
print(' ')

# squares.py
squares = []
for value in range(1, 11):
    # 2 个星号 (**) 代表乘方运算
    squares.append(value ** 2)

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(squares)
print(' ')


''' 4.3.3 对数字列表进行简单的统计计算 '''
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# 0
print(min(digits))
# 9
print(max(digits))
# 45
print(sum(digits))
print(' ')


'''
    - 4.3.4 列表解析: 使用列表解析重写上面 squares.py (tips: 列表解析可以看作是 for 循环语句的简写形式)
        - (1) anther_squares 为列表名
        - (2) value ** 2 表达式计算平方值
        - (3) for value in range(1, 11): for 循环用于给表达式提供值，注意此处 for 循环末尾无冒号
'''
another_squares = [value ** 2 for value in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(another_squares)


# P54 Try It Yourself
# 使用一个for 循环打印数字 1~20 (含)。
twenty = [value for value in range(1, 21)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(twenty)


'''
    - 4.4 使用列表的一部分
        + 4.4.1 切片
        + 4.4.2 遍历切片
        + 4.4.3 复制列表

'''
print("Start:", "~" * 60)

players = ['charles', 'martina', 'michael', 'florence', 'eli']

''' 4.4.3 复制列表 '''
players_copy = players[:]

# ['charles', 'martina', 'michael']
print(players[0:3])

# ['martina', 'michael', 'florence']
# print(players_copy[1:4])

''' 如果没有指定第一个索引，Python 将自动从列表开头开始: '''
# ['charles', 'martina', 'michael', 'florence']
# print(players_copy[:4])

''' 如果省略第二个索引，切片终止于列表末尾。 '''
# ['michael', 'florence', 'eli']
# print(players_copy[2:])

''' 第一个索引为负数，返回离列表末尾相应距离的元素(即: 从末尾数相应数字的项) '''
# Output: ['michael', 'florence', 'eli']
# print(players_copy[-3:])

# ['charles', 'martina']
''' 第二个索引为负数，返回列表长度和负数相加后的数字项 '''
print(players_copy[:-3])

print("Over:", "~" * 60)


'''
    - 4.5 元组 tuple /'tʌpl/ (不可变的列表称为元组)
        + 4.5.1 定义元组: 使用圆括号来标识。 Python 将不能修改的值称为不可变的，而不可变的
            列表被称为 元组。
            - dimensions /dɪ'menʃ(ə)n/ = (200, 500) 
        + 4.5.2 遍历元组中的所有值
        + 4.5.3 修改元组变量
'''
print("Start:", "~" * 60)

dimensions = (200, 500)
print(dimensions[0])    # 200
print(dimensions[1])    # 500

print("Over:", "~" * 60)






