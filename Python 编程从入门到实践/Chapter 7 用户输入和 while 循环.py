# Created on 20190514

# parrot.py
# message = input('Tell me something, and I will repeat it back to you: ')
# print('Said: ', message)


## 7.2.3 使用标志
# prompt = '\nTell me something, and I will repeat it back to you,'
# prompt += '\nEnter "quit" to end the program.'
#
# active = True
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         active = False
#     else:
#         print(message)


# 7.2.4 使用 break 退出循环
write = '\nPlease enter the name of a city you have visited,'
write += '\nEnter "quit" when you are finished.'

# while True:
#     city = input(write)
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")


# 7.2.5 再循环中使用 continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


