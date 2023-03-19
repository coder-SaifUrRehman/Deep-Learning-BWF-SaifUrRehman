my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12]
middle_index = len(my_list) // 2
middle_slice = my_list[middle_index-1:middle_index+2]

print("Three items from frist:", my_list[:3])
print("Three items from the middle of the list are:", middle_slice)
print("Three items from last:", my_list[-3:])