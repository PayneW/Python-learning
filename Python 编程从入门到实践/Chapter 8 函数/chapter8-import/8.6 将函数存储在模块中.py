"""
    - 8.6 将函数存储在**模块**(tips: 注意 Python 称为模块，而不是组件/文件 之类)中
        + 8.6.1 导入整个模块
        + 8.6.2 导入特定的函数
        + 8.6.3 使用 as 给函数指定别名
        + 8.6.4 使用 as 给模块指定别名
        + 8.6.5 导入模块中的所有函数
"""

'''Tips: 此文件夹(chapter8-import)在单独的窗口中运行项目才可以正常执行'''

# pizza.py
# def make_pizza(size, *toppings):
#     """概述要制作的匹萨"""
#     print("\nMaking a " + str(size) + "-inch pizza with the following "
#                                       "toppings:")
#     for topping in toppings:
#         print("-" + topping)


# 8.6.1 导入整个模块
# import pizza
# pizza.make_pizza(16, 'pepperoni')


# 8.6.2 导入特定的函数 (只导入需要的函数)
'''
    通过用都好分割函数名，可根据需要从模块中导入任意数量的函数:
    from module_name import function_0, function_1, function_2, ....
'''
from pizza import make_pizza
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 8.6.3 使用 as 给函数指定别名
# from pizza import make_pizza as mp
# mp(16, 'pepperoni')


# 8.6.4 使用 as 给模块指定别名
# import pizza as p
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 8.6.5 导入模块中的所有函数 (Tips: 慎用)
# from pizza import *
# make_pizza(16, 'pepperoni')

