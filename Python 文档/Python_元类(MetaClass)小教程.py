'''
    # Python 元类 (MetaClass) 小教程 (https://lotabout.me/2018/Understanding-Python-MetaClass/)
     > 目录 (Table of contents)
     - (1)、爷爷 = 元爸爸
     - (2)、类是动态创建得
     - (3)、类得创建过程
     - (4)、元类得应用
        + (4-1)、强制子类实现特定方法
        + (4-2)、注册所有子类
        + (4-3)、new vs init
     - (5)、小结
     - (6)、参考
'''


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


''' - (1) 爷爷 = 元爸爸
        + Meta is a prefix used in English to indicate a concept which is an 
        abstraction behind another concept, used to complete or add to the 
        latter. Meta 是英语中使用得前缀，用于表示概念，该概念是另一个概念的抽象概念，用于
        完成或添加后者。 
'''

# 我们都知道 Python 里一切都是对象，那么事对象就有对应的 "类(class)" 或称 "类型(type)"。
# Python 中可以用 `type(obj)` 来得到对象的类型:
print(type(10))    # <class 'int'>
print(type([1, 2, 3]))     # <class 'list'>
print(type({'a': 1, 'b': 2}))  # <class 'dict'> (dictionary) 字典


class DoNothing:
    pass


x = DoNothing
print(type(x))  # <class 'type'>

# 根据上面的输出可以看到 '类(class) 的类型(type) 都是 type'。那么 `type` 的类型又是什么？
# A: 答案，`type`的类型还是 `type`, 是一个递归的类型。
print(type(type))   # <class 'type'>

'''
    对象的类型叫做类(class)，**类的类型就称作元类(meta-class)**。是不是很像 "爸爸的爸爸叫
    爷爷"？ 换句话说，'普通类(class)' 可以用来生成实例(instance), 同样的，元类
    (meta-class) 也可以生成实例，生成的实例就是 '普通类'了。
'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

