# 1.Create a dictionary with keys as numbers 1 to 5 and values as their squares.
def new_list():
    my_dict = {}
    for num in range(1,6):
        my_dict[num] = num**2
    return my_dict
print(new_list())


# 2.Given a dictionary, access the value associated with a specified key and print it.
def specific_key(my_dict):
    if key in my_dict:
        return my_dict[key]
key = input('enter the specific key:')
my_dict = {'name':'Aravind','age':25,'place':'Edison'}
print(specific_key(my_dict))


# 3. Write a function that takes a dictionary and a key as input, returns the value if it exists, or "Key not found" if it doesn’t.
def is_exist(my_dict):
    key = input('Enter the key:')
    if key in my_dict:
        return my_dict[key]
    else:
        return "Key not found"
my_dict = {'name':'Aravind','age':25,'place':'Edison'}
print(is_exist(my_dict))


# 4. Write a function that adds a key-value pair to a dictionary only if the key does not already exist.
def adding_pairs(my_dict, key, value):
    if key not in my_dict:
        my_dict[key] = value
        return my_dict
    else:
        return "Key already exists"


my_dict = {'name': 'Aravind', 'age': 25, 'place': 'Edison'}
key = 'age'
value = 10000
adding_pairs(my_dict, key, value)
my_dict = {'name': 'Aravind', 'age': 25, 'place': 'Edison'}
key = 'salary'
value = 10000
adding_pairs(my_dict, key, value)


# 5. Create a dictionary with three students' names as keys and their scores as values, then update one student’s score.
def updating_dict(my_dict):
    if key in my_dict:
        my_dict[key] = int(value)
    return my_dict
key= input('enter the value:')
value = input('enter the value:')
my_dict = {'aravind': 99, 'sunil': 99, 'venky': 99}
print(updating_dict(my_dict))


# 6. Write a program that removes a specific key from a dictionary if it exists.
def removing_key(my_dict,key):
    if key in my_dict:
        my_dict.pop(key)
        return my_dict
    else:
        return "Key not exists"
my_dict = {'name':'Aravind','age':25,'place':'Edison'}
key = 'place'
print(removing_key(my_dict,key))


# 7. Write a program to check if a specific key exists in a dictionary.
def is_exist(my_dict, key):
    if key in my_dict:
        return "Key exists"
    else:
        return "Key does not exist"
my_dict = {'name': 'Aravind', 'age': 25, 'place': 'Edison'}
key = 'place'
print(is_exist(my_dict, key))


# 8. Given a dictionary, clear all entries and print the dictionary.
def clear_dict():
    my_dict.clear()
    return my_dict
my_dict = {'name':'Aravind','age':25,'place':'Edison'}
print(clear_dict())


# 9. Write a function that returns all keys of a dictionary.
def get_keys(my_dict):
    keys_list = []
    for key in my_dict:
        keys_list.append(key)
    return keys_list
my_dict = {'name':'Aravind','age':25,'place':'Edison'}
print(get_keys(my_dict))


# 10. Write a function that returns all values of a dictionary.
def get_values(my_dict):
    values = my_dict.values()
    output_list = []
    for value in values:
        output_list.append(value)
    return
my_dict = {'name':'Aravind','age':25,'place':'Edison'}
print(get_values(my_dict))


# 11. Given a dictionary, use a loop to print each key and value on a new line.
def get_items(my_dict):
    for key,value in my_dict.items():
        print(key,value)
my_dict = {'name':'Aravind','age':25,'place':'Edison'}
print(get_items(my_dict))


# 12. Write a function that counts the number of keys in a dictionary.
def length_of_keys(my_dict):
    count = 0
    for key in my_dict.keys():
        count += 1
    return f'number of keys in the given dictionary are {count}'
my_dict = {'name':'Aravind','age':25,'place':'Edison'}
print(length_of_keys(my_dict))


# 13. Write a program that removes the key with the smallest value from a dictionary.
my_dict = {'a':3,'b':6,'e':1,'d':8}
sorted_dict = dict(sorted(my_dict.items(), key=lambda x:x[1]))
keys = []
for key in sorted_dict.keys():
    keys.append(key)
print(keys)
smallest_value_key = keys[0]
my_dict.pop(smallest_value_key)
print(my_dict)


# 14. Write a program that combines two dictionaries into one.
def combining_dicts():
    for key,value in dict2.items():
        dict1[key] = value
    return dict1
dict1 = {'a':1,'b':2,'c':3}
dict2 = {'d':4,'e':5,'f':6}
print(combining_dicts())


# 15. Write a function that merges two dictionaries. If there are duplicate keys, add their values.
def merge_dicts(dict1,dict2):
    for key,value in dict2.items():
        if key in dict1:
            value = dict1[key]+value
            dict1[key] = value
        else:
            dict1[key] = value
    return dict1
dict1 = {'a':1,'b':2,'f':3}
dict2 = {'a':4,'e':5,'f':6}
print(merge_dicts(dict1,dict2))


# 16. Create a dictionary from two lists: one with keys and one with values.
def create_dict(list1, list2):
    my_dict = {}
    for key in range(len(list1)):
        for value in range(len(list2)):
            if key == value:
                my_dict[list1[key]] = list2[value]
            else:
                continue
    return my_dict


list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3, 4]
print(create_dict(list1, list2))

# def create_dict(list1,list2):
#     list3 = []
#     for key,value in zip(list1,list2):
#         list3.append((key,value))
#         my_dict = dict(list3)
#     return my_dict
# list1 = ['a','b','c','d']
# list2 = [1,2,3,4]
# print(create_dict(list1,list2))


# 17. Write a function that creates a dictionary where the keys are strings and values are their lengths.
def create_dict(string_list):
    my_dict = {}
    for key in string_list:
        my_dict[key] = len(key)
    return my_dict
string_list = ['aravind','venky','sowmya','sai']
print(create_dict(string_list))


# 18. Write a function that returns the minimum value in a dictionary.
def minimum_value(my_dict):
    key_list = []
    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
    for key in sorted_dict:
        key_list.append(key)
    return sorted_dict[key_list[0]]
my_dict = {'aravind': 7, 'venky': 5, 'sowmya': 6, 'sai': 3}
print(minimum_value(my_dict))


# 19. Write a function that returns the maximum value in a dictionary.
def maximum_value(my_dict):
    key_list = []
    sorted_dict = dict(sorted(my_dict.items(),key = lambda x:x[1]))
    for key in sorted_dict:
        key_list.append(key)
    return sorted_dict[key_list[-1]]
my_dict = {'aravind': 7, 'venky': 5, 'sowmya': 6, 'sai': 3}
print(maximum_value(my_dict))


# 20. Write a program that counts the frequency of each letter in a given string and stores it in a dictionary.
def count_letters(given_string):
    my_dict = {}
    for num1 in range(len(given_string)):
        count = 0
        for num2 in range(len(given_string)):
            if given_string[num1] == given_string[num2]:
                count += 1
            else:
                continue

        my_dict[given_string[num1]] = count
    return my_dict
given_string = 'aravind'
print(count_letters(given_string))


# 21. Write a program that creates a dictionary from a list of numbers, with keys as numbers and values as their cubes.
def cubes_dict(my_list):
    my_dict = {}
    for num in my_list:
        my_dict[num] = num**3
    return my_dict
my_list = [1,2,3,4,5,6]
print(cubes_dict(my_list))


# 22. Write a program to find and print the average value of all values in a dictionary.
def average_of_values(my_dict):
    count = 0
    sum = 0
    for value in my_dict.values():
        count += 1
        sum += value
    average_value = sum/count
    return average_value
my_dict = {'aravind': 7, 'venky': 5, 'sowmya': 6, 'sai': 3}
print(average_of_values(my_dict))


# 23. Given a dictionary with multiple people’s ages, write a function that groups people by their age.
def grouping_dict(my_dict):
    grouped_list = []
    for key in my_dict:
        if my_dict[key] == int(age):
            grouped_list.append(key)
        else:
            continue
    return f'{age} age group people are {grouped_list}'
age = input('enter the age:')
my_dict = {'aravind':25,'sai':27,'ravindra':25,'sunil':27}
print(grouping_dict(my_dict))


# 24. Write a function that takes a dictionary and returns the sum of all values.
def sum_of_values(my_dict):
    sum = 0
    for value in my_dict.values():
        sum += value
    return sum
my_dict = {'aravind': 7, 'venky': 5, 'sowmya': 6, 'sai': 3}
print(sum_of_values(my_dict))


# 25. Write a function that returns the top N keys with the highest values from a dictionary.
def get_keys(my_dict):
    keys_list = []
    sorted_dict = dict(sorted(my_dict.items(),key = lambda x:x[1],reverse = True))
    for key in sorted_dict:
        keys_list.append(key)
    total_keys = keys_list[:N]
    return total_keys
N = int(input('Enter number of keys:'))
my_dict = {'aravind': 7, 'venky': 5, 'sowmya': 6, 'sai': 3}
print(get_keys(my_dict))


# 26. Write a program to sort a dictionary by its keys in ascending order.
def sort_by_key(my_dict):
    sorted_dict = dict(sorted(my_dict.items(),key = lambda x:x[0],reverse = False))
    return sorted_dict
my_dict = {'aravind': 7, 'venky': 5, 'sowmya': 6, 'sai': 3}
print(sort_by_key(my_dict))


# 27. Write a program to sort a dictionary by its values in descending order.
def sort_by_values(my_dict):
    sorted_dict = dict(sorted(my_dict.items(),key = lambda x:x[1],reverse = True))
    return sorted_dict
my_dict = {'aravind': 7, 'venky': 5, 'sowmya': 6, 'sai': 3}
print(sort_by_values(my_dict))


# 28. Write a function that takes a dictionary and removes all key-value pairs with even values.
def removing_evenpairs(my_dict):
    count = 0
    for key, value in list(my_dict.items()):
        if value % 2 == 0:
            del my_dict[key]
        else:
            continue
    return my_dict
my_dict = {'aravind': 7, 'venky': 5, 'sowmya': 6, 'sai': 3}
print(removing_evenpairs(my_dict))


# 29. Given a dictionary of employee salaries, create a new dictionary with only those earning above a specified salary.
def filtering_dict(my_dict):
    filtered_dict = {}
    limit = 5000
    for key,value in my_dict.items():
        if value > limit:
            filtered_dict[key] = value
        else:
            continue
    return filtered_dict
my_dict = {'aravind':6000,'sowmya':4000,'venky':9000,'sai':5000}
print(filtering_dict(my_dict))


# 30. Write a program that creates a dictionary where keys are numbers from 1 to N and values are factorials of the keys.
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def factorial_dict(number):
    output_dict = {}
    for key in range(1, number + 1):
        output_dict[key] = factorial(key)
    return output_dict

number = 9
print(factorial_dict(number))


# 31. Write a function that finds the intersection of two dictionaries (keys present in both).
def common_keys(dict1, dict2):
    keys_list = []
    for key in dict1:
        if key in dict2:
            keys_list.append(key)
        else:
            continue
    return keys_list
dict3 = {'a': 1, 'b': 2, 'f': 3}
dict4 = {'a': 4, 'e': 5, 'f': 6}
print(common_keys(dict3, dict4))


# 32. Write a program that finds the difference between two dictionaries (keys in one but not the other).
def notcommon_keys(dict1, dict2):
    keys_list = []
    for key in dict2:
        if key not in dict1:
            keys_list.append(key)
        else:
            continue
    return keys_list
dict3 = {'a': 1, 'b': 2, 'f': 3}
dict4 = {'a': 4, 'e': 5, 'f': 6}
print(notcommon_keys(dict3, dict4))



# 33. Write a function that checks if two dictionaries are equal, regardless of key order.
def is_equal(dict1,dict2):
    for key in dict2:
        if key in dict1:
            continue
        else:
            return 'Both dictionaries are not equal'
    return 'both dictionaries are equal'
dict1 = {'a':1,'b':2,'f':3}
dict2 = {'a':4,'e':5,'f':6}
print(is_equal(dict1,dict2))
dict1 = {'a':1,'b':2,'f':3}
dict2 = {'a':4,'b':5,'f':6}
print(is_equal(dict1,dict2))


# 34. Write a function to find the longest key in a dictionary.
def longest_key(my_dict):
    length = 0
    word = ''
    for key in my_dict:
        word = ''
        if length > len(key):
            continue
        else:
            length = len(key)
            word = key
    return word
my_dict = {'aravind': 6000, 'sowmya': 4000, 'venky': 9000, 'saimotupalli': 5000}
print(longest_key(my_dict))


# 35. Write a function that sorts a dictionary based on the length of its keys.
def sort_dict(my_dict):
    sorted_dict = dict(sorted(my_dict.items(),key = lambda x:len(x[0])))
    return sorted_dict
my_dict = {'aravind':6000,'sowmya':4000,'venky':9000,'saimotupalli':5000}
print(sort_dict(my_dict))


# 36. Given a dictionary, write a program to find keys with the same values and group them together.
def grouping_keys(my_dict):
    grouped_list = []
    for key in my_dict:
        if my_dict[key] == int(age):
            grouped_list.append(key)
        else:
            continue
    return f'{age} age group people are {grouped_list}'
age = input('enter the age:')
my_dict = {'aravind':25,'sai':27,'ravindra':25,'sunil':27}
print(grouping_keys(my_dict))


# 37. Write a program that converts a nested dictionary into a flat dictionary (e.g., {"a": {"b": 1}} becomes {"a.b": 1}).
def flatten_dict(my_dict):
    flat_dict = {}
    for key in my_dict:
        for key1 in my_dict[key]:
            key2 = f'{key}.{key1}'
            value = my_dict[key][key1]
            flat_dict[key2] = value
        return flat_dict
my_dict = {"a": {"b": 1}}
print(flatten_dict(my_dict))


# 38. Write a function that counts the number of keys that start with a particular letter in a dictionary.
def starts_with(my_dict):
    count = 0
    for key in my_dict:
        if key.startswith(letter):
            count += 1
        else:
            continue
    return f'count of keys that starts with {letter} are {count}'
letter = input('enter the letter:')
my_dict = {'aravind':6000,'sowmya':4000,'venky':9000,'saimotupalli':5000}
print(starts_with(my_dict))











