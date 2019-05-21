# Created on 20190513

'''
    - 2.3.1 修改字符串的大小写
        + title(): 以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写。
        + upper(): 将字符串全部改为大写。
        + lower(): 将字符串全部改为小写。
'''
name = 'Ada lovelace'
# Ada Lovelace
print(name.title())
# ADA LOVELACE
print(name.upper())
# ada lovelace
print(name.lower())
# Ada lovelace
print(name)

print('')


# 2.3.3 用制表符或换行符来添加空白
# Language:
# 	Python
# 	C
# 	Javascript
print('Language: \n\tPython\n\tC\n\tJavascript')


'''
    - 2.3.4 删除空白:
        + strip(): /strɪp/ vt.剥去，剥夺。 n.带，条状
        + lstrip(): left strip 删除做空白
        + rstrip(): right strip 删除右空白
'''
favorite_language = ' python  of course '
print('')
print(favorite_language.rstrip())
print(favorite_language.strip())

print('')


'''
    - 2.4 数字:
        + 2.4.1 整数
        + 2.4.2 浮点数
        + 2.4.3 使用函数 str() 避免类型错误
'''
age = 30
message = 'Happy ' + str(age) + 'rd Birthday!'
# Happy 30rd Birthday!
print(message)