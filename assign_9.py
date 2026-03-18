#1 task
def missing_elements(my_list: list) -> list:
    if not my_list:
        return []
    
    presence_dict = {}
    for x in my_list:
        presence_dict[x] = True
    missing = []

    start = my_list[0]
    end = my_list[-1]

    for i in range(start, end + 1):
            if i not in presence_dict:
                missing.append(i)
    return missing


#2 task
def count_occurrences(my_list: list) -> dict:
    if len(my_list) == 0:
        return None
    
    count = {}
    for x in my_list:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    
    return count


#4 task
def common_elements(list1: list, list2: list) -> list:
    s1 = set(list1)
    s2 = set(list2)
    return s1 & s2


#5 task
def char_frequency(my_string: str) -> dict:
    frequency = {}
    for x in my_string:
        if x in frequency:
            frequency[x] += 1
        else: frequency[x] = 1
    return frequency


#6 task
def unique_words(my_string: str) -> int:
    words = []
    splitted = my_string.split()
    for x in splitted:
        if x not in words:
            words.append(x)
    return len(words)


#7 task
def word_frequency(my_string: str) -> dict:
    frequency_dict = {}
    splitted = my_string.split()
    for x in splitted:
        if x in frequency_dict:
            frequency_dict[x] += 1
        else: frequency_dict[x] = 1
    return frequency_dict


#8 task
def count_in_range(my_list: list, start: int, end: int) -> int:
    unique = set()

    for x in my_list:
        if start <= x <= end:
            unique.add(x)
    return len(unique)


#9 task
def swap_dict(d: dict) -> dict:
    swapped = {}
    for k, v in d.items():
        if v not in swapped:
            swapped[v] = k
    return swapped


#10 task
def is_subset(set1: set, set2: set) -> bool:
    return set2.issubset(set1)


#11 task
def list_intersection(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))


#12 task
def list_union(list1: list, list2: list) -> list:
    return list(set(list1) | set(list2))


#13 task
def most_frequent(my_list: list) -> int:
    count = {}
    for x in my_list:
        if x not in count:
            count[x] = count.get(x, 0) + 1
    return max(count, key=count.get)


#14 task
def least_frequent(my_list: list) -> int:
    count = {}
    for x in my_list:
        count[x] = count.get(x, 0) + 1
    return min(count, key=count.get)