"""This programm is connected to calculate math sqrt."""
from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(number):
    """=Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Do the main operation."""
    if your_number <= 0:
        return 'Вы ввели недопустимое число.'
    result = calculate_square_root(your_number)
    return (f'Мы вычислили квадратный корень из введённого вами числа. '
            f'Это будет: {result}')


print(message)
print(calc(25.5))
