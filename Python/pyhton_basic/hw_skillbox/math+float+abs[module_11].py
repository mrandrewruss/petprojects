# Задача 1. Конвертация
eur = float(input("Укажите стоимость покупки Евро: "))
usd = round(eur / 1.05, 2)
rub = round(usd * 60.87, 2)
print(f"USD = {usd}")
print(f"Стоимость EUR в рублях: {rub}")

price = float(input("\nВведите стоимость товара в евро: "))

rub = round(price * 1.25 * 60.87, 2)
print(f"Товар стоит: {rub} рублей")


# =========================================================
# Задача 2. Грубая математика
import math

quantity_numbers = int(input('Введите кол-во чисел: '))

print()
for i in range(1, quantity_numbers + 1):
  print(f'Введите число {i}: ', end = '')
  number = float(input())
  if number > 0:
    number = math.ceil(number)
    log = math.log(number)
    print(f'\nx = {number}  log(x) = {log} \n')
  else:
    number = math.floor(number)
    exp = math.exp(number)
    print(f'\nx = {number}  exp(x) = {exp}\n')


# =========================================================
# Задача 3. Убийца Steam
import math
size = float(input('Укажите размер файла для скачивания: '))
speed = float(input('Какова скорость вашего соединения? '))
progress = 0

print()
for sec in range(1, math.ceil(size / speed + 1)):
  progress += speed
  if progress > size:
    progress = size
  print(f"Прошло {sec} сек. Скачано {int(progress)} из {int(size)} Мб ({math.ceil(progress / (size * 0.01))}%)")


# =========================================================
# Задача 4. Первая цифра

# Что нужно сделать
# Дано положительное действительное число X. Выведите его первую цифру после десятичной точки. При решении этой задачи нельзя пользоваться условной инструкцией, циклом или строками.

x = float(input('Укажите положительное действительное число X: '))

print(f"First number after '.' character: {int((x * 10) % 10)}")


# =========================================================
# Задача 5. Вот это объёмы!
import math

r = float(input('Введите радиус случайной планеты: '))
earhtV = 10.8321 * (10 ** 11)
volume = 4 / 3 * math.pi * (r ** 3)
result = round(earhtV / volume, 3)

print()
if earhtV > volume:
  print(f"Объём планеты Земля больше в {result} раз")
else:
  total_result = round(1 / result, 3)
  print(f'Объём планеты Земля меньше в (1/{result}) = {total_result} раз' )


# =========================================================
# Задача 6. Метеостанция

# Для удобства работы сотрудников международной метеостанции
# каждый день нужно распечатывать различные таблицы
# соответствия градусов по шкале Цельсия и Фаренгейта.
#
# Напишите программу,
# которая принимает на вход три целых числа
# в градусах Цельсия: нижняя граница температуры, верхняя граница температуры и шаг.
#
# Программа выводит на экран
# таблицу соответствия градусов Цельсия градусам Фаренгейта
# от нижней до верхней границы с указанным шагом.
#
# Обеспечьте контроль ввода.
# Верхняя граница должна печататься, даже если последний шаг “перепрыгнул “ ее.
# Известно, что 0С соответствует 32F,
# а каждый градус Цельсия эквивалентен 1.8 градусам Фаренгейта.
#
# Пример:
#
# Ввод:
# Нижняя граница: 0
# Верхняя граница: 50
# Шаг: 20
#
# Вывод:
# C        F

# 0        32
# 20       68
# 40       104
# 50       122

t_C_low = int (input ('Нижняя граница: '))
t_C_up = int (input('Верхняя граница: '))
step = int (input ('Шаг: '))
print('Вывод: ')
print('C', '  ', 'F', '\n')
for t in range (t_C_low, t_C_up, step):
   t_F = round(t * 1.8 + 32)
   print (t, '\t', t_F)
   if t + step > t_C_up:
     t = t_C_up
     t_F = round(t * 1.8 + 32)
     print ( t, '\t', t_F)


# =========================================================
# Задача 7. Ход конём

# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
#
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.
x = float (input('Введите расположение коня по горизонтали: '))
y = float (input('Введите расположение коня по вертикали: '))
xSquare = int(x*10)
ySquare = int(y*10)
if (xSquare > 10 or xSquare < 0 and ySquare > 10 or ySquare < 0):
  print('Клетки с такой координатой не существует')
else:
 x_new = float (input('Введите местоположение точки на доске по горизонтали: '))
 y_new = float (input('Введите местоположение точки на доске по вертикали: '))
 xSquare_new = int(x_new *10)
 ySquare_new = int(y_new *10)

 dx = abs(xSquare_new - xSquare)
 dy = abs(ySquare_new - ySquare)
 print('Конь в клетке (' + str(xSquare) + ', ' + str(ySquare) + '). Точка в клетке (' + str(xSquare_new) + ', ' + str(ySquare_new) + ').')

 if (dx == 1 or dx == 2) and (dy == 1 or dy == 2):
    print('Да, конь может ходить в эту точку.')
 else:
    print('Конь не может ходить в эту точку')

# =========================================================
# Задача 8. Часы

# С начала суток часовая стрелка повернулась на угол в α градусов.
# Определите на какой угол повернулась минутная стрелка с начала последнего часа.
# Входные и выходные данные — действительные числа.
#
# При решении этой задачи нельзя пользоваться условными операторами и циклами.
angle_hour = float(input('Введите угол часовой стрелки в градусах: '))
angle_minute = angle_hour % 30 * 12
print('Угол минутной стрелки', angle_minute, 'градусов')


# =========================================================
# Задача 9. Уравнение

# Даны действительные коэффициенты a, b, c,
# при этом a≠0.
# Решите квадратное уравнение ax^2+bx+c=0 и выведите все его корни.
#
# Если уравнение имеет два корня,
# выведите два корня в порядке возрастания,
# если один корень — выведите одно число,
# если нет корней — не выводите ничего
import math

a = float(input('Введите коэффициент a: '))
while a == 0:
  print('Вы указали некорректное значение a.', end = '')
  a = float(input('Введите коэффициент a (≠ 0): '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))

D = b ** 2 - 4 * a * c
if D == 0:
  x = -b / (2 * a)
  print('\nУравнение имеет один корень: ', x)
elif D > 0:
  x1 = (-b + math.sqrt(D)) / (2 * a)
  x2 = (-b - math.sqrt(D)) / (2 * a)
  if x1 > x2:
    print('Корни уравнения: ', x1, end = '')
    print(',', x2)
  else:
    print('Корни уравнения: ', x2, end = '')
    print(',', x1)
