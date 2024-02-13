# TODO Напишите функцию find_common_participants
def find_common_participants(group_1, group_2, razdelitel = ','):
    group_1_list = group_1.split(razdelitel)
    group_2_list = group_2.split(razdelitel)
    group_1_set = set(group_1_list)
    group_2_set = set(group_2_list)
    common_participants = list(set.intersection(group_1_set, group_2_set))
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group))
