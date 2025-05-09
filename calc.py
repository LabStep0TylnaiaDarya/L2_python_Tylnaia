# Простой калькулятор, обрабатывающий выражения вида: число операция число (например, 2 + 2)

def calculate(expression):
    try:
        tokens = expression.strip().split()
        if len(tokens) != 3:
            return "Ошибка: введите выражение в формате 'число операция число' (например, 2 + 2)"

        num1 = float(tokens[0])
        operator = tokens[1]
        num2 = float(tokens[2])

        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Ошибка: деление на ноль"
            return num1 / num2
        else:
            return "Ошибка: неизвестная операция"
    except ValueError:
        return "Ошибка: убедитесь, что введены числа"

user_input = input("Введите выражение (например, 3 + 4): ")
result = calculate(user_input)
print("Результат:", result)
