# написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
#
# запишите 5 тудушек
# и выведете все

# def notebook():
#     todo_list: list[str] = []
#
#     def add_todo(todo: str)-> None:
#         nonlocal todo_list
#         todo_list.append(todo)
#
#     def get_all()->list[str]:
#         nonlocal todo_list
#         return todo_list
#
#     return add_todo, get_all
#
# add_todo, get_all = notebook()
#
# add_todo('wake up')
# add_todo('drink cofe')
# add_todo('go to work')
#
# print(get_all())


# 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)
#
# Пример:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

# def expanded_form(num: int)-> str:
#     sting = str(num)
#     zero_count = len(sting)-1
#     return '+'.join(value+'0'*(zero_count-i) for i,value in enumerate(sting) if value != '0')
#
# print(expanded_form(142008))

# создать декоратор который будет считать сколько раз была запущена функция
# и будет выводит это значение после каждого запуска функции

# def dec_counter_func(func):
#     count = 1
#
#     def inner(*args, **kwargs):
#         nonlocal count
#         print(f'{count=}')
#         func(*args, **kwargs)
#         print('-'*20)
#         count += 1
#     return inner
#
# @dec_counter_func
# def func_test():
#     print('func-test')
#
# @dec_counter_func
# def func_test2():
#     print('func-test2')
#
# func_test()
# func_test2()
# func_test2()
# func_test()
# func_test()
# func_test()
# func_test()


# створити декоратор який буде рахувати кількість запущених функцій продекорованих цим декоратором
def make_decorator(func):
    count = 1

    def inner(*args, **kwargs):
        nonlocal count
        print(f'{count=}')
        func(*args, **kwargs)
        print('-'*20)
        count += 1
    return inner

decor = make_decorator

@decor
def func_test():
    print('func-test')

@decor
def func_test2():
    print('func-test2')

func_test()
func_test2()
func_test2()
func_test()
func_test()
func_test()
func_test()


# вивести послідовність Фібоначі, кількість вказана в знінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)

# number = int(input('How many numbers?'))
# fib_list = []
# def fibonacci(num):
#     if num <= 1:
#         return num
#     else:
#         return (fibonacci(num-1) + fibonacci(num-2))
#
# if number <= 0:
#     print('Enter number >= 1')
# else:
#     print('Fibonacci numbers:')
#     for i in range(number):
#         fib_list.append(str(fibonacci(i)))
#     print(f'x={number}->', ', '.join(tuple(fib_list)))

# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3

