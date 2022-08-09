import re

# print('==============String=================')
# print('String: task_1')
# st1_2 = input('Enter string: ')
# res_string_1 = ''
# for item in st1_2:
#     if item.isdigit():
#         res_string_1 += item + ','
# print(res_string_1)

# print('======================================')
#
# print('String: task_2')
# st1_2 = input('Enter string: ')
# num_list = re.findall('[0-9]+', st1_2)
# res_string_2 = ''
# for item in num_list:
#     res_string_2 += item + ', '
# print(res_string_2)


# print('==============List Comprehension=================')
# print('List: task_1')
# st2_1 = input('Enter string: ')
# print([i.upper() for i in st2_1])

# print('List: task_2')
# max_num = int(input('Enter max number: '))
# numbers = range(max_num)
# list_num = []
# for item in numbers:
#     if item %2 != 0:
#         list_num.append(item**2)
# print(list_num)


print('==============Function=================')
print('===створити функцію яка виводить ліст======')
def print_list(*args):
    list = []
    for value in args:
        list.append(value)
    print(list)
print_list(25, 45, 25)

print('==створити функцію яка приймає три числа та виводить та повертає найбільше.==')
def return_print_max_number(*args):
    list = []
    for num in args:
        list.append(num)
    print(max(list))
    return max(list)
return_print_max_number(25, 10, 45)

print('==створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше==')
def return_min_print_max_number(*args):
    list = []
    for num in args:
        list.append(num)
    print(max(list))
    return min(list)
return_min_print_max_number(25, 10, 45)


list = [14, 10, 8, 55, 20, 24]

print('==створити функцію яка повертає найбільше число з ліста==')
def return_max_num_from_list(list):
    return max(list)
return_max_num_from_list(list)
print(return_max_num_from_list(list))

print('== створити функцію яка повертає найменьше число з ліста==')
def return_min_num_from_list(list):
    return min(list)
return_min_num_from_list(list)
print(return_min_num_from_list(list))

print('==створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.==')
def sum_of_list(list):
    return sum(list)
sum_of_list(list)
print(sum_of_list(list))

print('==створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.==')
def arithmetic_mean(list):
    return sum(list)/len(list)
arithmetic_mean(list)
print(arithmetic_mean(list))

