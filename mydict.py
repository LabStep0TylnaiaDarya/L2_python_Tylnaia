student = {
    "имя": "Анна",
    "возраст": 20,
    "курс": 2
}
print("Информация о студенте:", student)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print("Объединенный словарь:", merged_dict)

key_to_check = "возраст"
if key_to_check in student:
    print(f"Ключ '{key_to_check}' есть в словаре, значение: {student[key_to_check]}")
else:
    print(f"Ключ '{key_to_check}' отсутствует в словаре.")
