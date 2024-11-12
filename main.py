### Задание 6
# Написать программу, которая:
# - Создаёт случайный список из **20** значений по **4** случайных целых чисел от **-10** до **10**.
# - Находит все уникальные комбинации пар из этих значений и выводит их в виде списка кортежей.
# - Пользователь вводит целое число.
# - Вычисляет количество пар, чья сумма меньше заданного пользователем значения.
import random # Импортируем модуль random для генерации случайных чисел.
from itertools import combinations # Импортируем combinations для создания пар.
random_list = [random.randint(-10, 10) for _ in range(20)]  # Генерируем список случайных чисел.
print("Случайный список:", random_list) # Выводим сгенерированный список.
unique_pairs = set(combinations(random_list, 2))  # Создаем множество пар из случайного списка.
print("Уникальные пары:", unique_pairs) # Выводим уникальные пары.
user_input = int(input("Введите целое число: ")) # Пользователь вводит целое число.
count = 0 # Инициализируем счетчик пар с суммой меньше заданного числа.
for pair in unique_pairs:  # Перебираем каждую уникальную пару.
    if sum(pair) < user_input: # Проверяем, если сумма пары меньше введенного числа.
        count += 1 # Увеличиваем счетчик, если условие выполнено.
print(f"\nКоличество пар, чья сумма меньше {user_input}: {count}") # Выводим количество пар, сумма которых меньше введенного числа.