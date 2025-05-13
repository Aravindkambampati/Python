#Write a function that returns the sum of two numbers.
def sum_of_two_numbers(num1,num2):
    return num1+num2
print(sum_of_two_numbers(4,6))

#Write a function to check if a number is even or odd.
def even_or_odd(num):
    if num%2 == 0:
        return f'given number {num} is even'
    else:
        return f'given number {num} is odd'
print(even_or_odd(6))

#Write a function that takes a string and returns its reverse.
def reverse_of_givenstring(given_string):
    reverse_string = given_string[::-1]
    return reverse_string
print(reverse_of_givenstring('aravind'))

#Write a function that takes a string and returns its reverse.
def reverse_of_givenstring(given_string):
    reverse_string = given_string[::-1]
    return reverse_string
print(reverse_of_givenstring('aravind'))

#Write a function to check if a given string is a palindrome.
def is_palindrome(given_string):
    if given_string == given_string[::-1]:
        return 'given string is a palindrome'
    else:
        return 'given string is not a palindrome'
print(is_palindrome('lol'))

#Write a function that returns the maximum of three numbers.
def maximum_number(given_list):
    for num1 in range(len(given_list)):
        for num2 in range(len(given_list)-num1-1):
            if given_list[num2] > given_list[(num2)+1]:
                given_list[num2],given_list[num2+1] = given_list[num2+1],given_list[num2]
    sorted_list = given_list
    return f'maximum number of given numbers is {sorted_list[-1]}'
print(maximum_number([23,45,125,34,56,89]))

#Write a function that counts the number of vowels in a given string.
def vowels_count(given_string):
    count = 0
    for character in given_string:
        if character in ['a','e','i','o','u']:
            count += 1
    return count
print(vowels_count('kambampati'))

#Write a function that takes a number and returns its square.
def square_of_number(number):
    square_number = number*number
    return square_number
print(square_of_number(5))


# Write a function to calculate the sum of all even numbers in a list.
def sum_of_evennumbers(given_list):
    sum_value = 0
    for num in given_list:
        if num % 2 == 0:
            sum_value += num
    return sum_value
print(sum_of_evennumbers([1, 2, 3, 4, 5, 6]))

#Write a function that removes all vowels from a given string.
def remove_vowels(given_string):
    string_characters = list(given_string)
    list1 = []
    for character in string_characters:
        if character not in ['a','e','i','o','u']:
            list1.append(character)
    return ''.join(list1)
print(remove_vowels('aravind'))

#Write a function to check if two strings are anagrams.
def is_anagram(string1,string2):
    string1_characters = list(string1)
    for character in string2:
        if character not in string1_characters:
            return 'string1 and string2 are not anagrams'
        else:
            return 'string1 and string2 are anagrams'
print(is_anagram('tea','eat'))

#Write a function to flatten a nested list (e.g., [[1, 2], [3, 4]] → [1, 2, 3, 4]).
def flatten(nested_list):
    output_list = []
    for list1 in nested_list:
        output_list.extend(list1)
    return output_list
print(flatten([[1, 2], [3, 4],[5,6]]))

#Write a function that takes two lists and returns a list of common elements.
def common_elements(list1,list2):
    commonelements_list = []
    for num in list1:
        if num in list2:
            commonelements_list.append(num)
    return commonelements_list
list1 = [1,2,3,4,5,6,7,8]
list2 = [3,4,5,6,7,8,9,23,45,65,12,38]
print(common_elements(list1,list2))


# Write a function that returns a list of prime numbers up to a given limit.
def prime_numbers(number):
    primenumbers_list = []
    for num in range(number):
        if num > 1:
            for num2 in range(2, int(num ** 0.5) + 1):
                if num % num2 == 0:
                    break
            else:
                primenumbers_list.append(num)
        else:
            continue
    return primenumbers_list

print(prime_numbers(20))


# Write a function that checks if a number is a perfect square.
def perfect_square(number):
    for num in range(int(number / 2) + 1):
        if num * num == number:
            return f'given number {number} is a perfect square of {num}'
            break
    else:
        return f'given number {number} is not a perfect square'
print(perfect_square(36))

#Write a function to remove the duplicates in the list
def removing_duplicates(input_list):
    output_list = []
    for num in input_list:
        if num not in output_list:
            output_list.append(num)
    return output_list
input_list = [1,2,3,4,5,6,22,22,33,11]
print(removing_duplicates(input_list))


# Write a function that reads a number 'n' in the list, and returns the first 'n' prime numbers
def prime_numbers(number):
    primenumbers_list = []
    for num in range(number + 1):
        if num > 1:
            for num2 in range(2, int(num ** 0.5) + 1):
                if num % num2 == 0:
                    break
            else:
                primenumbers_list.append(num)
        else:
            continue
    return primenumbers_list


def list_of_primenumbers(input_list):
    for num in input_list:
        if num == 1:
            print('1 is neither prime nor composite')
        else:
            output_list = prime_numbers(num)
            print(f'first {num} prime numbers are {output_list}')


input_list = [1, 2, 3, 4, 5, 6, 22, 22, 33, 11]
print(list_of_primenumbers(input_list))

# Write a function to check if given number is greater than all numbers in the list.
input_list = [1, 2, 3, 4, 5, 6, 22, 22, 33, 11]


def is_greater(number):
    for num in input_list:
        if number < num:
            return f'given number {number} is not greater than all the numbers in the list'
    else:
        return f'given number {number} is greater than all the numbers in the list'
print(is_greater(37))
print(is_greater(10))


# Write a function that returns the difference between squares of the numbers in the above list,
# and number of factors for that square including their list of factors
def squares(input_list):
    squares_list = []
    for num in input_list:
        squares_list.append(num ** 2)
    return squares_list


def difference_of_squares(input_list):
    filtered_list = squares(input_list)
    difference_list = []
    for num1 in range(len(filtered_list)):
        for num2 in range(len(filtered_list)):
            if num1 != num2:
                num3 = abs((filtered_list[num1]) - (filtered_list[num2]))
                difference_list.append(num3)
            else:
                continue
    return difference_list


def factors(input_list):
    squares_of_list = squares(input_list)
    total_list = []
    for num1 in squares_of_list:
        count = 0
        factors_list = []
        for num2 in (1, int(num1 ** 0.5) + 1):
            if num1 % num2 == 0:
                if num2 * num2 == num1:
                    count += 1
                    factors_list.append(num2)
                else:
                    count += 2
                    factors_list.append(num2)
                    factors_list.append(int(num1 // num2))
        total_list.append((num1, count, factors_list))
    return total_list


input_list = [1, 2, 3, 4, 5, 6, 22, 22, 33, 11]
print(factors(input_list))
print(difference_of_squares(input_list))

## Help to print ("Hi the square of the number (3) is 9")
def help_square(number):
    return f'Hi the square of the number ({number}) is {number*number}'
help_square(3)


# sorting the list without using any builtin functions
# second largest number in the list
def sort_list(given_list):
    for num1 in range(len(given_list)):
        for num2 in range(len(given_list) - num1 - 1):
            if given_list[num2] > given_list[(num2) + 1]:
                given_list[num2], given_list[num2 + 1] = given_list[num2 + 1], given_list[num2]
    return given_list


def second_largest(given_list):
    sorted_list = sort_list(given_list)
    number = sorted_list[-2]
    return number


given_list = [2, 4, 1, 66, 34, 56, 5, 12]
print(sort_list(given_list))
print(second_largest(given_list))







