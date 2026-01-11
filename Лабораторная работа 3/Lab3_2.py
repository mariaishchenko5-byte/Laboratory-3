# TODO Напишите функцию find_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(group1, group2, delimiter=","):
    list1 = group1.split(delimiter)
    list2 = group2.split(delimiter)

    common_participants = set(list1).intersection(set(list2))

    return sorted(list(common_participants))

print("С разделителем вертикальная линия (|):")
result = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print(f"Общие участники: {result}")
print()

# C разделителем-запятой (как в задании по умолчанию)
participants_group_a = "Иванов,Петров,Сидоров"
participants_group_b = "Петров,Сидоров,Смирнов"
print("Пример с разделителем-запятой:")
result = find_common_participants(participants_group_a, participants_group_b)
print(f"Общие участники: {result}")