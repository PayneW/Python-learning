# Created in 20190517

# lexicographical /ˌleksikəu'ɡræfikəl/ adj.词典编纂的
# lexicographical order 字典顺序

# Python 字典顺序排序:  k-th Smallest in Lexicographical Order 按字典顺序排列最小的。


#  digit_bit 数字位
def digit_bit(number):
    bit = 1
    test = 1
    divisor = 10
    while test >= 1:
        test = number // divisor
        if test >= 1:
            bit = bit + 1
            divisor = divisor * 10
    return bit


def list_number_digit_bit(input_list):
    result = [digit_bit(i) for i in input_list]
    return result


def lexicon_order(input_list):
    digit_bit_list = list_number_digit_bit(input_list)
    max_bit = max(digit_bit_list)
    alpha = 1 / max_bit
    dict_of_number = {}
    for i in input_list:
        if digit_bit(i) == max_bit:
            dict_of_number[i] = i
        else:
            bit = digit_bit(i)
            new_digit = (i * 10 ** (max_bit - bit)) - 0.5 * alpha * (max_bit - bit)
            dict_of_number[new_digit] = i
    key_of_dict_of_number = list(dict_of_number.keys())
    key_of_dict_of_number.sort()
    lexicon_order_number = [dict_of_number[i] for i in key_of_dict_of_number]
    return lexicon_order_number


def find_the_number(n, k):
    number_list = list(range(1, n + 1))
    lexicon_order_number = lexicon_order(number_list)
    result = lexicon_order_number[k - 1]
    print('The lexicographical order is: ', lexicon_order_number)
    print('so the ', k, 'th smallest number is:', result)
    return result


print(lexicon_order(range(130)))
exit()
# find_the_number(n=130, k=5)
# exit()

for i in range(10):
    print(i)
    r = find_the_number(n=13, k=i)
    print(r)
    print('~' * 79)

