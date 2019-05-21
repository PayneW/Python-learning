# Created in 20190517


'''
    ## 10.4 存储数据
    - 10.4.1 使用 json.dump() 和 json.load()
        + 函数 json.dump() 接受 2 个实参:
            - (1) 要存储的数据
            - (2) 可用于存储数据的文件对象
'''

import json


l1 = [1, 2, 3, 54]
d1 = {'k1': 'v1'}

ret = json.dumps(l1)




'''
    - link: http://yshblog.com/blog/104
    - Python 的 json 模块基本用于: 最常用的 2 个方法:
        + (1) dumps: 把字典转换成 json 字符串
        + (2) loads: 把 json 字符串转换成字典
'''




