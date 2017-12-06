# Задача №1
set_one = set(input('Введите первую строку: '))
set_two = set(input('Введите вторую строку: '))
print(set_one.intersection(set_two))

# Задача №2
size = int(input('Введите максимальное значение исследуемой последовательности: \n'))
list_three = []
list_five = []
list_result = []
for i in range(size + 1):
    if i % 3 == 0:
        list_three.append(i)
    if i % 5 == 0:
        list_five.append(i)
set_three = set(list_three)
set_five = set(list_five)
set_result = (set_three.intersection(set_five))
for element in set_result:
    list_result.append(element)
list_result.sort()
print(list_result)
