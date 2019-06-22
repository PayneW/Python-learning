# Created on 20190515


# 8.1 定义函数
def greet_user(username):
    """
    文档字符串注释 (docstring) 描述了函数是做什么的。文档字符串用三个引号括起，
    Python使用它们来生成有关程序中函数的文档
    """
    print("Hello, " + username.title() + "!")

# Hello, Kell!
# greet_user('kell')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""
    - 8.2 传递实参
        + 8.2.1 位置实参
            - 1、调用函数多次
            - 2、位置实参的顺序很重要
        + 8.2.2 关键字实参
        + 8.2.3 默认值
        + 8.2.4 等效的函数调用
        + 8.2.5 避免实参错误
"""


# 8.2.2 关键字实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(animal_type='dog', pet_name='Peter')


# 8.2.3 默认值
def des_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    # I have a dog.
    # My dog's name is Willie.
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".\n")


des_pet(pet_name='willie')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""
    - 8.3 返回值
        + 8.3.1 返回简单值
        + 8.3.2 让实参变成可选的
        + 8.3.3 返回字典
        + 8.3.4 结合使用函数和 while 循环
"""


# 8.3.2 让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + middle_name
    return full_name.title()


# - **musician /mjuː'zɪʃ(ə)n/ n.音乐家**
#   + Do you guys know any musicians? 你们俩有认识玩音乐的人吗？
musician = get_formatted_name('jimi', 'hendrix')
print(musician)  # Jimi

musician = get_formatted_name('john', 'hooker', 'lee')
# John Lee Hooker
print(musician + '\n')


# 8.3.3 返回字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    return {'first': first_name, 'last_name': last_name}


musician = build_person('jimi', 'hendrix')
# {'first': 'jimi', 'last_name': 'hendrix'}
print(str(musician) + '\n')
print(" ")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""
    - 8.4 传递列表
        + 8.4.1 在函数中修改列表
        + 8.4.2 禁止函数修改列表
"""


# 传递列表
def greets_user(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello(你好), " + name.title() + "!"
        print(msg)


def run():
    user_names = ['hannah', 'ty', 'margot']
    greets_user(user_names)
    print(" ")


run()


# 8.4.1 在函数中修改列表
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，知道没有未打印的设计为止
    打印每个设计后，都将其以到列表 completed_models 中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 模拟根据设计制作 3D 打印模型的过程
        print("Printing model(印刷模型): " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\n下面为打印好的模型: ")
    for completed_model in completed_models:
        print(completed_model)


def main():
    unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    completed_models = []
    print_models(unprinted_designs, completed_models)
    show_completed_models(completed_models)


main()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""
    - 8.5 传递任意数量的实参 (tips: *toppings --> 创建一个名为 toppings 的空元组)
        + 8.5.1 结合使用位置实参和任意数量实参
        + 8.5.2 使用任意数量的关键字实参 (tips: **user_info 中的两个星号让 Python 创建一
          个名为 user_info 的空字典.)
"""


# 传递任意数量的实参
# 参数名 *toppings 中的星号让 Python 创建一个名为 toppings 的空元组(4.5 章)，并将收到的
# 所有值都封装到这个元组中。即: ('mushrooms', 'green peppers', 'extra cheese')
def make_pizza(*toppings):
    """概述要制作的匹萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)


make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 8.5.2 使用任意数量的关键字实参
# (tips: **user_info 中的两个星号让 Python 创建一个名为 user_info 的空字典.)
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = dict()
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(
    'albert',
    'einstein',
    location='princeton',
    field='physics')
print('\nuser_profile: ', user_profile)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""
    - 8.6 将函数存储在**模块**(tips: 注意 Python 称为模块，而不是组件/文件 之类)中
        + 8.6.1 导入整个模块
        + 8.6.2 导入特定的函数
        + 8.6.3 使用 as 给函数指定别名
        + 8.6.4 使用 as 给模块指定别名
        + 8.6.5 导入模块中的所有函数
"""








