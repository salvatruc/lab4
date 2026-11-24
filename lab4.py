import random

# Создаём случайный массив из 10 целых чисел
numbers = [random.randint(1, 100) for _ in range(10)]

# Выводим исходный массив
print("Массив до сортировки:", numbers)

# Сортируем массив методом пузырька
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        # Меняем соседние элементы местами, если они стоят не по порядку
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Выводим отсортированный массив
print("Массив после сортировки:", numbers)
