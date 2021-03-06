from math import pi  # Потрібно імпортувати число pi в нашу програму для подальшої роботи

import sympy  # Імпортуємо математичний пакет сампай, який дозволить нам виконати інтегрування та записати підінтегральну функію
from sympy import exp, cos, sin  # З цього пакету ми будето використовувати експоненту,сінус та косинус тому імпортуємо їх в нашу програму

a = 0  # Нижня границя
b = pi/2  # Верхня границя
n = int(input('Введіть кількість розбиттів: '))  # Вводимо кількість розбиттів, у нашому випадку '100'

x = sympy.symbols('x')  # Оголошуємо, що в нас буде змінна 'х' у функціях
h = (b-a)/(n*2)  # Обчислюємо крок
result_integration = sympy.integrate((exp(cos(x))*sin(x)),x)  # Інтегруємо, щоб побачити вигляд інтегралу та вручну порахувати відносну похибку
start_integral = exp(cos(x)) * sin(x)  # Записуємо функцію початкового інтегралу
x_0 = start_integral.subs(x,a)  # Підставляємо значення першого значення в підінтегральну функцію та вираховуєм значення
x_2n = start_integral.subs(x,b)  # Підставляємо значення останнього значення в підінтегральну функцію та вираховуєм значення
area_chet = 0  # Вводимо змінну, в яку будемо заносити численне значення площі кожного парного кроку
area_nechet = 0  # Вводимо змінну, в яку будемо заносити численне значення площі кожного непарного кроку
for i in range(2,2*n,2):  # Проходимо по парним значенням та подвоюємо кількість відрізків
    x_i = a + 2*h  # Визначаємо значення вузлу
    a += 2*h  # Готуємо а до наступної ітерації
    result_digit = start_integral.subs(x,x_i)  # Підставляємо значення x_і у початкову функцію та знаходимо площу цієї частини
    area_chet += result_digit  #  Додаємо значення до змінної,яка зберігає суму парних значень
area_chet = area_chet*2  # Суму парних підінтегральних функцій ми множимо на 2
a = 0  # Скидуємо значення нашої змінної, щоб вона знову дорівнювала нижній границі
for j in range(1,2*n+1,2):  # Проходимо по непарним значенням та подвоюємо кількість відрізків
    x_j = a + h  # Визначаємо значення вузлу
    a += 2*h  # Готуємо а до наступної ітерації
    result_digit_nechet = start_integral.subs(x,x_j)  # Підставляємо значення x_j у початкову функцію та знаходимо площу цієї частини
    area_nechet += result_digit_nechet  # Додаємо значення до змінної,яка зберігає суму непарних значень
area_nechet = area_nechet * 4   # Суму значень непарних підінтегральних функцій ми множимо на 4
area = (h/3)*(x_0+x_2n+area_chet+area_nechet)  # Знаходимо загальну площу та множимо її на h/3
print(f'Значення інтегралу: {area} ')  # Вивід наших результатів
print(f'Інтегрована функція: {result_integration}')
