# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
# https://drive.google.com/file/d/1401HWFEwu_NxPzdLqHo7HMmAiK4QHxEM/view?usp=sharing

def summator(n):
    if n == 1:
        s = 1
        return s
    else:
        s = (-0.5) ** (n - 1)
        return s + summator(n - 1)


n = int(input('Введите число элементов ряда: '))
summa = summator(n)
print(f'Сумма ряда равна {summa}')
