def add(a, b):
    return a + b

print("Сумма 5 и 3 =", add(5, 3))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 7
print(f"Число {number} простое?" , is_prime(number))

def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

nums = [10, 20, 30, 40]
print("Среднее значение:", average(nums))