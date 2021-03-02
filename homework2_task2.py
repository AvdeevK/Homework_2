# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# https://drive.google.com/file/d/1401HWFEwu_NxPzdLqHo7HMmAiK4QHxEM/view?usp=sharing

a = int(input('Введите натуральное число: '))

c = a
d = 0
counter_even = 0
counter_odd = 0
while c != 0:
    d = c % 10
    if d % 2 == 0:
        counter_even += 1
    else:
        counter_odd += 1
    c = c // 10

print(f'Количество четных цифр - {counter_even}, количество нечетных цифр - {counter_odd}')
