# Python 内置函数


'''
    - map(): 会根据提供的函数对指定序列 (序列包含: 字符串 + 列表list + 元组tuple) 做映射。
    + 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function
     返回值的新列表。
    + 语法: map(function, iterable, ...)
        - function 函数
        - iterable 一个或多个序列
    + Python 3.x 返回迭代器 (迭代器是访问集合元素的一种方式: 集合见:
        \Python3入门加进阶-imooc\20190522174526.png)
'''


# 计算平方数
def square(x):
    return x ** 2


# Python 3.x 返回迭代器
squares = map(square, [1, 2, 3, 4, 5])
for item in squares:
    print(item)
