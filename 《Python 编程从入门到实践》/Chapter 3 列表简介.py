# Created on 20190513
# 第 3 章: 列表简介

'''
    - 3.1 列表是什么
        + 3.1.1 访问列表元素
        + 3.1.2 索引从 0 而不是 1 开始
        + 3.1.3 使用列表中的各个值
'''


motocyles = ['honda', 'yamaha', 'suzuki']


'''
    - 3.2.1 修改列表元素
'''
moto = ['honda', 'yamaha', 'suzuki']
moto[0] = 'ducati'
# moto: ['ducati', 'yamaha', 'suzuki']
print('moto:', moto)


'''
    - 3.2.2 在列表中添加元素
        + 1、在列表末尾添加元素 append()
        + 2、在列表中插入元素 insert()
'''
# 1、在列表末尾添加元素 append()
motocyles.append('ducati')
# output: ['honda', 'yamaha', 'suzuki', 'ducati']
print(motocyles)

# 2、在列表中插入元素 insert()
motocyles.insert(1, 'toyota')
# output: ['honda', 'toyota', 'yamaha', 'suzuki', 'ducati']
print(motocyles)



'''
    - 3.2.3 从列表中删除元素
        + 1、使用 del 语句删除元素
        + 2、使用 pop() 方法删除元素: pop() 方法可删除列表末尾的元素，并让你能够直接使用它。(和 js 语法一样的 )
        + 3、弹出列表中任何位置处的元素 pop(index)
        + 4、根据值删除元素 remove(): 如果知道要删除的元素的值，可以使用此方法。
'''
# 1、使用 del 语句删除元素
del motocyles[0]
# ['toyota', 'yamaha', 'suzuki', 'ducati']
print(motocyles)

# 2、使用 pop() 方法删除元素
popped_motocyles = motocyles.pop()
# output: ducati
print(popped_motocyles)
# output: ['toyota', 'yamaha', 'suzuki']
print(motocyles)

# 3、弹出列表中任何位置处的元素 pop(index)
first_owned = motocyles.pop(0)
# toyota
print(first_owned)
# ['yamaha', 'suzuki']
print(motocyles)

# 4、根据值删除元素 remove(): 如果知道要删除的元素的值，可以使用此方法。
motocyles.remove('suzuki')
# ['yamaha']
print(motocyles)
# len(motocyles): 1
print('len(motocyles):', len(motocyles))

print('')

'''
    - 3.3 组织列表
        + 3.3.1 使用方法 sort() 对列表进行永久性排序
            - 列表.sort()
            - sort(reverse=True)
        + 3.3.2 使用函数 sorted() 对列表进行临时排序
            - sorted(列表): 注意此处是函数，使用方式是把列表当作参数传入 
            - sorted(reverse=True)
        + 3.3.3 倒着打印列表 (- **reverse /rɪ'vɜːs/ ~~adj.相反的。 ~~v.逆转，颠倒。 ~~n.背面**)
            - 列表.reverse(): 反转列表中的排列顺序。
        + 3.3.4 使用函数 len() 确定列表的长度
'''
cars = ['Bmw', 'Audi', 'Toyota', 'Subaru']

# cars.sort()
# ['Audi', 'Bmw', 'Subaru', 'Toyota']
# print(cars)

# ['Audi', 'Bmw', 'Subaru', 'Toyota']
print(sorted(cars))

# ['Bmw', 'Audi', 'Toyota', 'Subaru']
print(cars)

cars.reverse()
# ['Subaru', 'Toyota', 'Audi', 'Bmw']
print(cars)

# cars length: 4
length = len(cars)
print("cars length:", length)










