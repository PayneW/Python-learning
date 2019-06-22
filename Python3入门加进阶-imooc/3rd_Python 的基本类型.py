# Python 的基本数据类型

'''
    ## 第3章: 理解什么是代码与 Python 的基本类型
    > 3-1: 什么是代码，什么是写代码

    > 3-2: 数字: 整型与浮点型
     - Number: 数字
            + 整数: int
            + 浮点数: float  (其他语言: 单精度(float), 双精度(double))
            + 函数 type()

    > 3-3: 2、8、10、16 进制
        + Python 中如何表示各种进制
            - 0b/0B*** : 表示 2 进制
            - 0o/0O*** : 表示 8 进制
            - 0x/0X*** : 表示 16 进制

    > 3-4: 各进制的表示与转换
        - Python 各种进制的相互转换
            + 8/10/16 进制转 2 进制: bin(x) 函数
            + 2/8/16 进制转 10 进制: int(x) 函数
            + 2/8/10 进制转 16 进制: hex(x) 函数
            + 2/10/16 转换成 8 进制: oct(x)

    > 3-5: 数字: 布尔类型与复数
        - 数字操作符:
            + + : 加
            + - : 减
            + * : 乘
            + / : 除
            + // : 整除 (只保存整数部分)
            + ** : 乘方
        - - bool 布尔类型:
            + True (首字母大写，切记)
                - bool(1)  输出: True
            + False (首字母大写，切记)
                - bool(0)  输出: False
        - complex 复数

    > 3-6: 字符串: 单引号与双引号

    > 3-7: 多行字符串

    > 3-8: 转义字符
        - 转义字符:
            + \t : 横向制表符
            + \' : 单引号
            + \n : 换行符
            + \r : 回车

    > 3-9: 原始字符串
        - 在字符串前面加上 `r` 既可
            + ```
                # c:\northwind\northwest
                print(r'c:\northwind\northwest')
              ```

    > 3-10 --> 3-12: 字符串运算 一/二/三


'''


'''
    > 3-2: 数字: 整型与浮点型
     - Number: 数字
        + 整数: int
        + 浮点数: float  (其他语言: 单精度(float), 双精度(double))
        + 函数 type()
'''
# <class 'int'>
print(type(1))
# <class 'int'>
print(type(-1))

# <class 'float'>
print(type(1.1))
# <class 'float'>
print(type(1.1111111111111111111111))

num = 1 + 0.1
print(num)

# <class 'float'>
# / : 除
# tips: 2/2 = 1.0, 所以输出是一个浮点型 float
print(type(2/2))

# <class 'int'>
# // : 整除 (只保存整数部分)
print(type(2//2))
# output --> 2//2:  1
print("2//2: ", 2//2)

print("~" * 60)
class Student(object): pass
s = Student()
# <class '__main__.Student'>
print(type(s))
# <class 'type'>
print(type(Student))
# <class 'type'>
print(type(int))
print("~" * 60)


''' 
    > 3-3: 10、2、8、16 进制
        + Python 中如何表示各种进制
            - 0b/0B*** : 表示 2 进制
            - 0o/0O*** : 表示 8 进制
            - 0x/0X*** : 表示 16 进制
'''
# Python 表示 2 进制
print("Start", "~" * 60)
# 3
print(int(0b11))
# 21
print(int(0b10101))
print("Over", "~" * 60)


''' 
    > 3-4: 各进制的表示与转换 
    - Python 各种进制的相互转换
        + 8/10/16 进制转 2 进制: bin(x) 函数
        + 2/8/16 进制转 10 进制: int(x) 函数
        + 2/8/10 进制转 16 进制: hex(x) 函数
        + 2/10/16 转换成 8 进制: oct(x)
'''
print("Start", "~" * 60)

# 88 conversion binary: 0b1011000
print("88 conversion binary:", bin(88))
# bool(1): True
print("bool(1):", bool(1))
# bool('abc'): True
print("bool('abc'):", bool("abc"))

# bool([]): False (tips: python 中空值都会认为是 false)
print("bool([]):", bool([]))
# bool({}): False
print("bool({}):", bool({}))


print("Over", "~" * 60)

''' 
    > 3-10 --> 3-12: 字符串运算 一/二/三
    -  
'''
print("Start:", "~" * 60)

str_hello = "Hello "
str_world = "world"
print(str_hello + str_world)
# Hello Hello Hello
print(str_hello * 3)

two_str = "Hello world"
# two_str[0]: H
print("two_str[0]:", two_str[0])
# two_str[3]: l
print("two_str[3]:", two_str[3])

# two_str[0:3]: Hel
''' tips: ** 切片:《python编程入门到实战》中 4.4 节是列表切片, 此处是字符串切片。** '''
print("two_str[0:3]:", two_str[0:3])

# two_str[0:-1]: Hello worl
''' 第二个索引为负数，返回字符串(列表)长度和负数相加后的数字项 '''
print("two_str[0:-1]:", two_str[0:-1])

# two_str[-3:]: rld
''' 第一个索引为负数，返回离字符串(列表)末尾相应距离的元素(即: 从末尾数相应数字的项) '''
print("two_str[-3:]:", two_str[-3:])


print("Over:", "~" * 60)


"""
    add: https://python-guide.gitbooks.io/python-style-guide/content/style-guide/code.html
"""

''' - 字符串: 尽量不要用 `+` 号拼接字符串，使用 `%s` 模板或 `join()` 方法拼接。 '''

# 正确写法，使用 join
print(' '.join(["Spam", "eggs", "and", "spam"]))

# 正确写法
print('%s %s %s %s' % ('Spam', 'eggs', 'and', 'spam'))
