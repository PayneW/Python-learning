# 9.1.1 创建 Dog 类

'''
    为何必须在方法定义中包含形参 self 呢？
    A: 因为 Python 调用这个 __init__() 方法来创建 Dog 实例时，将自动传入实参 self。每个与
     类相关联的方法调用都自动传递实参 self, 它时一个指向 <实例本身> 的引用，让实例能够访问类中
     的属性和方法。 (tips: self 和 JavaScript 中的 this 都是指向实例，js 中是指向 构造函数
     的实例，Python 是指向类的实例。 js 详细见: js-sundry-goods\《珠峰视频学习》\MVVM 原理
     实现\mvvm\1.mvvm-comments.js)
'''


class Dog:
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化属性 name 和 age"""
        self.name = name
        self.age = age
        
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        """模拟消勾被命令时打滚"""
        print(self.name.title() + " rolled over!") 


# 9.1.2 根据类创建实例
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()