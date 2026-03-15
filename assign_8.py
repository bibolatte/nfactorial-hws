#1 task
def count_unique_elements(my_list: list) -> int:
    unique_elems = []
    for x in my_list:
        if x not in unique_elems:
            unique_elems.append(x)
    return len(unique_elems)


#2 task
def remove_duplicates(my_list: list) -> int:
    unique_elems = []
    for x in my_list:
        if x not in unique_elems:
            unique_elems.append(x)
    return(unique_elems)


#3 task
def reverse_list(my_list: list) -> list:
    return list(reversed(my_list))


#4 task
def max_value(my_list: list) -> int:
    max_val = my_list[0]
    for x in my_list:
        if x > max_val:
            max_val = x
    return max_val
print(max_value([1, 2, 3, 4, 5]))


#5 task
def min_value(my_list: list) -> int:
    min_val = my_list[0]
    for x in my_list:
        if x < min_val:
            min_val = x
    return min_val
print(min_value([1, 2, 3, 4, 5]))


#6 task
def sum_values(my_list: list) -> int:
    total = 0
    for x in my_list:
        total = total + x
    return total


#7 task
def average(my_list: list) -> float:
    counter = 0
    sum = 0
    for x in my_list:
        sum = sum + x
        counter += 1

    average_num = sum / counter
    return average_num


#8 task
def find_index(my_list: list, element: int) -> int:
    i = 0
    while i < len(my_list):
        if my_list[i] == element:
            return i
        i += 1
    return -1


#9 task
def is_sorted(my_list: list) -> bool:
    if len(my_list) <= 1:
        return True
    
    for x in range(len(my_list)):
        if my_list[x] > my_list[x+1]:
            return False
        
    return True


#10 task
def count_frequency(my_list: list, element: int) -> int:
    counter = 0
    for x in my_list:
        if x == element:
            counter += 1
    return counter


#11 task
def find_mode(my_list: list) -> int:
    mode = my_list[0]
    max_count = 0

    for x in my_list:
        current_count = my_list.count(x)
        
        if current_count > max_count:
            max_count = current_count
            mode = x
            
    return mode


#12 task
def remove_all(my_list: list, element: int) -> list:
    new_list = []
    
    for x in my_list:
        if x!= element:
            new_list.append(x)
    return new_list


#13 task
def rotate_left(my_list: list, k: int) -> list:
    if not my_list: return my_list
    k = k % len(my_list)
    return my_list[k:] + my_list[:k]

#14 task
def rotate_right(my_list: list, k: int) -> list:
    if not my_list: return my_list
    k = k % len(my_list)
    return my_list[-k:] + my_list[:-k]


#15 ефыл
def find_intersection(list1: list, list2: list) -> list:
    intersection = []
    for x in list1:
        if x in list2:
            if x not in intersection:
                intersection.append(x)
    return intersection


#16 task
def find_union(list1: list, list2: list) -> list:
    union = list1.copy()
    for x in list1:
        if x not in list2:
            union.append(x)
    return union


#17 task
def find_difference(list1: list, list2: list) -> list:
    difference = []
    for x in list1:
        if x not in list2:
            difference.append(x)
    return difference