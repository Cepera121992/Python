a = int(input('Введите результат пробежки в первый день: '))
b = int(input('Введите желаемое расстояние пробежки: '))
day = 1
distance = a
while distance < b:
    a = a + 0.1 * a
    day += 1
    distance = a
print(f'На {day} день спортсмен достиг результата не менее {b} километров')