# Created in 20190517

import json

# numbers = [2, 3, 4, 6, 7, 0, 11]
# file_numbers = 'numbers.json'
# with open(file_numbers, 'w') as f_num:
#     json.dump(numbers, f_num)


import os


def greet_user():
    """问候用户，并指出其名字"""
    filename = 'username.json'

    # 如果 username.json 文件已存在
    if os.path.exists(filename):
        with open(filename) as f_obj:
            username = json.load(f_obj)
            print("Welcome back, " + username + "!")
    else:
        username = input("你叫什么名字？ ")
        # 如果文件不存在就创建文件并写入
        with open(filename, "w") as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")


greet_user()
