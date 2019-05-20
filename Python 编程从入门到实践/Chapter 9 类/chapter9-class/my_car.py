# Created in 20190516

'''
    在面向对象编程中，你编写表示现实世界中的事物和情景的类，并基于这些类来创建对象。
    编写类时，你定义一大类对象都有的通用行为。基于类创建对象时，每个对象都自动具备这种通用行为，
    然后可根据需要赋予每个对象独特的个性。
    ** 根据类来创建对象被称为 <实例化>， 这让你能够使用类的实例。 **

    - 类名使用 <大驼峰命名法>
'''



'''
    - 9.4 导入类
        + 9.4.1 导入单个类
        + 9.4.2 在一个模块中存储多个类
        + 9.4.3 从一个模块中导入多个类
        + 9.4.4 导入整个模块
        + 9.4.5 导入模块中的所有类 (不推荐使用)
            - ` from module_name import * `
        + 9.4.6 在一个模块中导入另一个模块
'''

#  9.4.1 导入单个类
# from car import Car

# 9.4.3 从一个模块中导入多个类
# from car import Car, ElectricCar
#
# my_new_car = Car('audi', 'a4', 2016)
# # 2016 Audi A4
# print(my_new_car.get_descriptive_name())
# print(' ')
#
# my_tesla = ElectricCar('tesla', 'roadster', 16)
# # 16 Tesla Roadster
# print(my_tesla.get_descriptive_name())


# 9.4.4 导入整个模块
import car
my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla2 = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla2.get_descriptive_name())