numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
new_list = []
for i in numbers:
    if i != None:
        new_list.append(i)
numbers[4] = sum(new_list)/(len(numbers))


# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
