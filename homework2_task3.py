# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# https://drive.google.com/file/d/1401HWFEwu_NxPzdLqHo7HMmAiK4QHxEM/view?usp=sharing

def detector(a):
    counter = 0
    while a != 0:
        a //= 10
        counter += 1
    return counter


number = int(input('Введите натуральное число: '))
temp_number = number
grade = detector(number)
reverse_number = 0
while grade > 0:
    grade -= 1
    reverse_number += (temp_number % 10) * 10 ** grade
    temp_number //= 10

print(f'Исходное число {number}, перевернутое число {reverse_number}')
