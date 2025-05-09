with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Hello, File!")

with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("Содержимое файла:", content)

with open("example.txt", "a", encoding="utf-8") as file:
    file.write("\nЭто новая строка.")
