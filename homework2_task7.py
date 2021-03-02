# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
# https://drive.google.com/file/d/1401HWFEwu_NxPzdLqHo7HMmAiK4QHxEM/view?usp=sharing

def summator(num):
    if num == 1:
        return 1
    else:
        return num + summator(num - 1)


n = int(input(f'Введите число элементов ряда: '))
formula = int(n*(n+1)/2)
summa = summator(n)
if formula == summa:
    print(f'Сумма ряда тождественно равна расчётной формуле {formula}={summa}')

else:
    print('Формула и сумма ряда не равны')
