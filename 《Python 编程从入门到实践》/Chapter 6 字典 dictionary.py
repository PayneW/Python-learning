# Created on 20190514
# 第 6 章 -- 字典

'''
- **thick /θɪk/ ~~adj.厚的，粗的。 ~~n.浓厚。 ~~v.浓缩**
- **crust /krʌst/ n.外壳，面包皮**
- **topping /'tɒpɪŋ/ ~~n.糕点上的装饰配料，构成顶部的东西。 ~~adj.杰出的，高耸的**
- **mushroom /'mʌʃruːm/  ~~n.蘑菇。 ~~.adj.蘑菇形的，迅速生长的。 ~~采蘑菇，迅速生长**
    + --> You ordered a thick-crust pizza with the following toppings: mushrooms,
          extra cheese.
         你点了一个厚皮披萨, 加上面的配料： 蘑菇、额外的奶酪。
'''


# 6.2.6 由类对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}
# Sarah's favorite language is Python.
print("Sarah's favorite language is " + favorite_languages['sarah'].title() +
      ".")

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(' Hi ' + name.title() + ', I see your favorite language is ' +
              favorite_languages[name].title() + "!\n")


# 6.3 遍历字典
# 6.3.1 遍历字典中所有的键-值对: 字典.items()
# 6.3.2 遍历字典中所有的键: 字典.keys()
# 6.3.2 遍历字典中所有的值: 字典.values()



# 6.4.1 字典列表
# 创建一个用于存储外星人的空列表
aliens = []
# 创建 30 个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 显示前 5 个外星人
for alien in aliens[:5]:
    print(alien)
print('...')

# 显示创建了多少个外星人
print('Total number of aliens: ' + str(len(aliens)))


# 6.4.2 在字典中存储列表
fav_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in fav_languages.items():
    print('\n' + name.title() + 's favorite languages are:')
    for language in languages:
        print('\t' + language.title())
print("\n")

# 6.4.3 在字典中存储字典
users = {
    'a_einstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'm_curie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}
for username, user_info in users.items():
    print('Username: ' + username)

    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print('\t Full name:' + full_name.title())
    print('\t Location: ' + location.title())






