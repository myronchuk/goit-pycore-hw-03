import random

def get_numbers_ticket(min, max, quantity):
    if min >= max:
        raise ValueError("Мінімальне число повинно бути меншим за максимальне.")
    if min < 1 or max < 1:
        raise ValueError("Числа повинні бути невід'ємними.")
    if max > 1000:
        raise ValueError("Максимальне число не повинно перевищувати 1000.")
    if quantity < 1 or quantity > (max - min + 1):
        raise ValueError("Кількість унікальних чисел перевищує діапазон.")
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)

try:
    min = int(input('Введіть мінімальне число: '))
    max = int(input('Введіть максимальне число: '))
    quantity = int(input('Введіть кількість унікальних чисел: '))
    ticket = get_numbers_ticket(min, max, quantity)
    print('Ваші лотерейні числа:', ticket)
except ValueError as e:
    print("Помилка:", e)
except Exception:
    print("Виникла невідома помилка. Перевірте введені дані.")
