"""
    ### 第 8 章: Python 函数 (这里的讲解没有《Python 编程从入门到实践》 第8章的函数讲的
        的好，所以细节讲解见: Chapter8函数.py)
    - 8-1 认识函数
    - 8-2 函数的定义及运行特点
    - 8-3 如何让函数返回多个结果
    - 8-4 序列解包与链式赋值
    - 8-5 必须参数与关键字参数
    - 8-6 默认参数
    - 8-7 可变参数
    - 8-8 关键字可变参数
    - 8-9 变量作用域
    - 8-10 作用域链
    - 8-11 global关键字
    - 8-12 划算还是不划算

    - recursion /rɪ'kɜːʃ(ə)n/ n.递归，递归式
"""

import sys
sys.setrecursionlimit(1000000)


def add(x, y):
    result = x + y
    return result


print(add(1000, 100000))


def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    return damage1, damage2


skill1_damage, skill2_damage = damage(3, 6)
print(skill1_damage, skill2_damage)


# - 序列解包
# a = 1
# b = 2
# c = 3
a, b, c = 1, 2, 3
d = 1, 2, 3
print(type(d))  # <class 'tuple'>
