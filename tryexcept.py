try:
    number = int(input("Введите число: "))
    print("Вы ввели число:", number)
except ValueError:
    print("Ошибка: нужно ввести именно число!")

try:
    with open("nofile.txt", "r", encoding="utf-8") as file:
        data = file.read()
        print("Содержимое файла:", data)
except FileNotFoundError:
    print("Ошибка: файл не найден.")
