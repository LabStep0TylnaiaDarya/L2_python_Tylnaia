import random
random_number = random.randint(1, 100)
print("Случайное число от 1 до 100:", random_number)

import datetime
now = datetime.datetime.now()
print("Текущие дата и время:", now)

import math
number = 16
sqrt_value = math.sqrt(number)
print(f"Квадратный корень из {number} с использованием math: {sqrt_value}")

def manual_sqrt(n, precision=0.0001):
    guess = n / 2
    while abs(guess * guess - n) > precision:
        guess = (guess + n / guess) / 2
    return guess

manual_result = manual_sqrt(number)
print(f"Квадратный корень из {number} без math: {manual_result}")
