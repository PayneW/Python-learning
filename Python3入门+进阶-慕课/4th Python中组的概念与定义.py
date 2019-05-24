# Python 列表   Created in 20190522

# (1, 2, 3, 4, 5, 7)
print((1, 2, 3) + (4, 5, 7))

# (1, 2, 3, 1, 2, 3, 1, 2, 3)
print((1, 2, 3) * 3)

#
# <class 'int'>
print(type((1)))


''' 如何定义空元组: () '''
# <class 'tuple'>
print(type(()))

''' 如何定义只有一个元素的元组: (1,) '''
# <class 'tuple'>
print(type((1,)))


list_1 = [1, 2, 3, 4, 5, 6]
''' 确定一项是不是在一个列表中 '''
if 3 in list_1:
    print("Yes I have")

''' len() 函数，取得列表的长度 '''
print(len(list_1))  # 6

''' max()/min()/sum() '''
print(max(list_1))  # 6
print(min(list_1))  # 1

print(max("Hello world!"))

''' 
    函数 ord() : 对表示单个 Unicode 字符的字符串，返回代表它 Unicode 码点的整数。
    例如 ord('a') 返回整数 97， ord('€') （欧元符合）返回 8364 。这是 chr() 的逆函数。
'''
print(ord('a'))     # 97
print(ord('$'))     # 36


''' 集合 (set) '''
# {1, 2, 5, 6}
print({1, 2, 3, 4, 5, 6} - {3, 4})
# {3, 4}
print({1, 2, 3, 4, 5, 6} & {3, 4})
# {1, 2, 3, 4, 5, 6, 7}
print({1, 2, 3, 5, 6} | {4, 7})

''' 定义一个空的集合 '''
print(type(set()))


''' 
    - 字典 dictionary
        + 定义一个空的字典: {}   
'''
