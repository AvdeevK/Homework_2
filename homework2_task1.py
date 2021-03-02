'''
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
   Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает
   новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
   Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова
   запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его
   в качестве делителя.
'''


# https://drive.google.com/file/d/1401HWFEwu_NxPzdLqHo7HMmAiK4QHxEM/view?usp=sharing

def calculator(chrctr, first, second):
    if chrctr == '*':
        c = first * second
        return c
    if chrctr == '/':
        if (second == 0):
            return f'Введенный Вами знаменатель равен нулю'
        else:
            c = first / second
            return c
    if chrctr == '+':
        c = first + second
        return c
    if chrctr == '-':
        c = first - second
        return c
    else:
        return f'Попробуйте ввести другую операцию'


character = input('Введите операцию между числами a ? b: ')

while character != '0':
    a = int(input('Введите первое число a = '))
    b = int(input('Введите второе число b = '))
    result = calculator(character, a, b)
    print(f'Результат операции a {character} b = {result}')
    character = input('Для выхода нажмите 0 или ведите операцию между числами a ? b: ')
