#ListCreation
#Create an empty list.
empty_list = []
print(empty_list)

#ListCreation
#Create an empty list.
empty_list = []
print(empty_list)

#Create a list containing five different fruits.
fruits = ['Apple','Banana','Cherry','Dates','Mango']
print(fruits)

#Create a list that contains the strings "Red" , "Green" , and "Blue" .
colors = ["Red","Green","Blue"]
print(colors)

#Create a list of three boolean values.
boolean_values = [False,True,True]
print(boolean_values)

#Create a list with five different colors.
colors = ['Red','Yellow','Orange','Blue','Purple']
print(colors)

#Create a list with numbers from 10 to 50 in steps of 10.
step_countof_10 = range(10,51,10)
print(list(step_countof_10))

#Create a list that contains the name of five countries.
countries = ['India','England','Australia','New Zealand','South Africa']
print(countries)

#Create a list with five repeated elements (e.g., 5 times "Hello" ).
repeated_element = ["Hello"]
print(repeated_element*5)

#Create a list of mixed data types (e.g., ["Python", 3.14, True] ).
mixed_elements = ['Python',3.14,True]
print(mixed_elements)

#Assesingelements/Indexing
#Print the first element from the list [1, 2, 3, 4, 5] .
numbers = [1,2,3,4,5]
first_element = numbers[0]
print(first_element)

#Print the last element from the list ["Apple", "Banana", "Cherry"] .
fruits = ["Apple","Banana","Cherry"]
last_fruit = fruits[2]
print(last_fruit)

#Access the third element in the list ["Python", "C++", "Java", "JavaScript"] .
programming_languages = ["Python", "C++", "Java", "JavaScript"]
third_language = programming_languages[2]
print(third_language)

#Print the element at index 2 from the list [10, 20, 30, 40, 50] .
numbers = [10,20,30,40,50]
index_2_element = numbers[2]
print(index_2_element)

#Print the element at index 0 from a list of your choice.
programming_languages = ["Python", "C++", "Java", "JavaScript"]
zero_index_element = programming_languages[0]
print(zero_index_element)

#Access the second element from a list of three numbers
numbers = [100,205,248]
second_element = numbers[1]
print(second_element)

#Access the first and last element from the list ["Sun", "Moon", "Stars"] .
Natural_lights = ["Sun", "Moon", "Stars"]
first_element = Natural_lights[0]
last_element = Natural_lights[2]
print(first_element,last_element)

#. Print the first two elements of a list.
numbers = [10,20,30,40,50]
first_two_elements = numbers[:2]
print(first_two_elements)

#Use negative indexing to print the second last element from the list [1, 2, 3, 4,5] .
numbers = [1,2,3,4,5]
second_last_element = numbers[-2]
print(second_last_element)

#Access the fourth element in the list ["Monday", "Tuesday", "Wednesday", "Thursday","Friday"] .
days = ["Monday", "Tuesday", "Wednesday", "Thursday","Friday"]
fourth_day = days[3]
print(fourth_day)

#Slicing
#Slice and print the first 3 elements from a list of 5 numbers.
numbers = [1,2,3,4,5]
first_three_elements = numbers[0:3]
print(first_three_elements)

#Create a list of 6 elements and slice out the last 2 elements.
numbers = [1,2,3,4,5,6]
last_two_elements = numbers[5:3:-1]
print(last_two_elements)

#Slice the first 4 elements from the list ["Sun", "Moon", "Stars", "Cloud", "Rain"] .
natural_stars = ["Sun", "Moon", "Stars", "Cloud", "Rain"]
first_four_elements = natural_stars[0:4]
print(first_four_elements)

# Create a list of 10 numbers and slice out the first 5 numbers
numbers = list(range(1,11))
first_five_elements = numbers[:5]
print(first_five_elements)

#Slice and print the middle three elements of a 5-element list.
numbers = list(range(1,6))
middle_three_elements = numbers[1:4]
print(middle_three_elements)

# Create a list of 8 numbers and slice every second number.
numbers = list(range(1,9))
slicing_every_secondnumber = numbers[1:8:2]
print(slicing_every_secondnumber)

#Slice out the last 4 elements from the list [10, 20, 30, 40, 50, 60] .
numbers = [10, 20, 30, 40, 50, 60]
last_four_elements = numbers[5:1:-1]
print(last_four_elements)

#Slice and print elements between index 2 and 5 in a list of 8 elements.
numbers = list(range(1,9))
elements_between_2and5 = numbers[3:5]
print(elements_between_2and5)

#Print a slice of the first 3 elements in a list of your choice.
numbers = list(range(1,9))
first_three_elements = numbers[0:3]
print(first_three_elements)

#Create a list of 6 strings and print a slice from index 1 to 4.
numbers = list(range(1,6))
elements_from_index1to4 = numbers[1:5]
print(elements_from_index1to4)

#deletion
#Create a list of five fruits and delete the second fruit.
fruits = ['Apple','Banana','Cherry','Dates','Mango']
del fruits[1]
print(fruits)

#Create a list [10, 20, 30, 40, 50] and delete the element at index 3.
numbers = [10, 20, 30, 40, 50]
del numbers[3]
print(numbers)

# Create a list and remove its first element.
numbers = [10, 20, 30, 40, 50]
numbers.pop(0)
print(numbers)

#Create a list of 6 colors and delete the last element
colors = ['Red','Yellow','Orange','Blue','Purple','Black']
del colors[-1]
print(colors)

#Delete the element "Blue" from the list ["Red", "Green", "Blue", "Yellow"] .
colors = ["Red", "Green", "Blue", "Yellow"]
colors.remove('Blue')
print(colors)

#Remove the number 3 from the list [1, 2, 3, 4, 5] .
numbers = [1,2,3,4,5]
numbers.remove(3)
print(numbers)

# Delete the last element from the list [100, 200, 300, 400, 500] .
numbers = [100, 200, 300, 400, 500]
del numbers[-1]
print(numbers)

#Remove all elements from a list using clear() .
numbers = [100, 200, 300, 400, 500]
numbers.clear()
print(numbers)

#Delete an element using pop() from a list of five numbers.
numbers = list(range(1,6))
numbers.pop()
print(numbers)

#Create a list of animals and delete the animal at index 2.
animals = ['ant','bat','cat','dog','elephant','frog']
animals.pop(2)
print(animals)

#Intermediate level list creation
#Create a list of even numbers from 2 to 20.
even_numbers = list(range(2,21,2))
print(even_numbers)

# Create a list with the squares of numbers from 1 to 5.
squares_list = []
for num in range(1,6):
    squares_list.append(num*num)
print(squares_list)

#Create a list using a loop that contains multiples of 5 from 5 to 50.
multiples_of_5 = []
for num in range(5,51):
    if num%5==0:
        multiples_of_5.append(num)
print(multiples_of_5)

#Create a list of characters from a string (e.g., ["P", "y", "t", "h", "o", "n"] ).
given_string = 'aravind'
characters_of_string = list(given_string)
print(characters_of_string)

# Create a list of prime numbers between 1 and 20.
prime_numbers = []


def is_prime(num):
    if num > 1:
        for num2 in range(2, int(num ** 0.5) + 1):
            if num % num2 == 0:
                return False
                break
        else:
            return True
    else:
        return False


for num in range(1, 21):
    if is_prime(num) is True:
        prime_numbers.append(num)
print(prime_numbers)

# Create a list of random numbers using a for loop.
import random
randomnumbers_list = []
for num in range(1, 11):
    random_number = random.randint(1, 99)
    randomnumbers_list.append(random_number)
print(randomnumbers_list)

#Create a list of numbers from 10 to 100, but only include numbers divisible by 10.
multiples_of_10 = []
for num in range(10,101):
    if num%10==0:
        multiples_of_10.append(num)
print(multiples_of_10)

# Create a list with a repeated number using list multiplication (e.g., [7] * 5 )
given_list = [7]
output_list = []
for num in range(1, 10):
    list_multiplication = given_list * num
    output_list.append(list_multiplication)
print(output_list)


# Create a list using a list comprehension that contains the first 10 multiples of 3.
multiples_of_3 = [num * 3 for num in range(1, 11)]
print(multiples_of_3)

#Create a list that combines two separate lists into one (e.g., list1 + list2 ).
numbers1 = list(range(1,11,2))
numbers2 = list(range(2,11,2))
numbers3 = numbers1+numbers2
print(numbers3)

#Accessing Elements/Indexing
#Access every second element from a list of 10 numbers.
numbers = list(range(1,11))
for num in range(1,len(numbers),2):
    print(numbers[num])

#Print the first three characters from a list created from a string (e.g., "Hello" ).
given_string = 'Hello'
for num in range(3):
    print(given_string[num])

# Access the third element from the list [True, False, True, False].
given_list = [True, False, True, False]
print(given_list[2])

# given_list = [True, False, True, False]
# count = 0
# for num in range(len(given_list)):
#     count += 1
#     if count == 3:
#         print(given_list[num])


#Access the element at index 5 from the list [1, 2, 3, 4, 5, 6, 7] .
given_list = [1,2,3,4,5,6,7]
print(given_list[5])

#Print the element at index -3 from a list
given_list = [1,2,3,4,5,6,7]
print(given_list[-3])

#Use a loop to print every element in a list.
given_list = [1,2,3,4,5,6,7]
for num in given_list:
    print(num)


#Print the last 3 elements from a list using negative indexing.
given_list = [1,2,3,4,5,6,7]
print(given_list[6:3:-1])

#Access the middle element in the list [1, 2, 3, 4, 5] .
# numbers = [1,2,3,4,5]
# print(numbers[2])


numbers = [1,2,3,4,5]
length = len(numbers)
if length%2 == 0:
    middle_element = int(length/2)
else:
    middle_element = int((length+1)/2)
middle_element_index = middle_element-1
print(numbers[middle_element_index])

#Print all elements except the last two from the list [100, 200, 300, 400, 500] .
# numbers = [100,200,300,400,500]
# print(numbers[0:3])

numbers = [100,200,300,400,500]
list1 = []
list2 = []
list1.append(numbers[-1])
list1.append(numbers[-2])
for num in numbers:
    if num not in list1:
        list2.append(num)
print(list2)

# Use a for loop to print the index and value of each element in a list.
numbers = [100,200,300,400,500]
for num1 in range(len(numbers)):
    num2 = numbers[num1]
    print(f'{num2} is the value with the index {num1}')

# Slicing:
# Slice and print every third element in a list of 10 numbers.
# numbers = list(range(1,11))
# for num in numbers:
#     if num%3 == 0:
#         print(num)


numbers = list(range(10))
total_three_sets = int(len(numbers) // 3)
count = 0
value_count = 0
while count < total_three_sets:
    value_count += 3
    value_index = value_count - 1
    print(numbers[value_index])
    count += 1

#Create a list of 8 elements and slice it in reverse order.
input_list  = list(range(1,9))
reverse_list = input_list[::-1]
print(reverse_list)


#Slice and print the last three elements from a list of 7 numbers.
input_list = list(range(7))
length = len(input_list)
start_index = length-1
end_index = start_index-3
last_three_elements = input_list[start_index:end_index:-1]
print(last_three_elements)

#Create a list of 12 numbers and print a slice from index 3 to index 8.
input_list = list(range(12))
sliced_list = input_list[3:9]
print(sliced_list)

#Slice and print the first half of a list with 8 elements.
input_list = list(range(8))
middle_index = (int(len(input_list))) // 2
first_half = input_list[:middle_index]
print(first_half)

#Create a list of 9 numbers and print a slice that skips every second element.
input_list = list(range(9))
sliced_list = input_list[::2]
print(sliced_list)

#Slice and print the elements between index 1 and 5 from the list [1, 2, 3, 4, 5,6] .
input_list = [1,2,3,4,5,6]
sliced_list = input_list[2:5]
print(sliced_list)

# Create a list of the first 10 letters of the alphabet and slice every other letter
alphabet = 'abcdefghijklmnopqrstuvwxyz'
first_10_letters = alphabet[:10]
letters_list = list(first_10_letters)
print(letters_list)
remaining_letters = alphabet[10:]
for letter in remaining_letters:
    print(letter)

#Print a reversed slice of the first 5 elements in a list of 10 numbers.
input_list = list(range(10))
middle_element = int(len(input_list)) // 2
first_half = input_list[:middle_index]
reversed_first_half = first_half[::-1]
print(reversed_first_half)


#Create a list of 7 colors and slice the middle three colors
colors_list = ['red','white','black','orange','green','purple','yellow']
middle_index = int(len(colors_list)) // 2
first_color = middle_index-1
second_color = middle_index
third_color = middle_index+1
start_index = first_color
end_index = third_color+1
middle_three_colors = colors_list[start_index:end_index]
print(middle_three_colors)

#Deleting Elements
# Delete the element at index 2 from the list [10, 20, 30, 40, 50] .
given_list = [10,20,30,40,50]
del given_list[2]
print(given_list)

# #Create a list and delete all elements that are greater than 50.
input_list = [23, 12, 45, 65, 23, 45, 87, 67, 34]
count = 0
while count < len(input_list):
    if input_list[count] < 50:
        count += 1
        continue
    else:
        input_list.remove(input_list[count])
print(input_list)

# input_list = [23,12,45,65,23,45,87,67,34]
# output_list = []
# for num in input_list:
#     if num < 50:
#         output_list.append(num)
#     else:
#         continue
# print(output_list)


#Use pop() to remove and print the last element from the list [5, 10, 15, 20] .
given_list = [5,10,15,20]
last_element = given_list.pop()
print(last_element)

#Delete an element using remove() from the list [1, 2, 3, 4, 5]
given_list = [1,2,3,4,5]
given_list.remove(3)
print(given_list)

#Use del to remove the element at index 3 from a list of 6 numbers.
input_list = list(range(6))
print(input_list)
del input_list[3]
print(input_list)

# Create a list and delete every second element using a loop.
step = 0
input_list = list(range(8))
print(input_list)
while step < len(input_list):
    if step % 2 == 0:
        step += 1
        continue
    else:
        del input_list[step]
        step += 1

print(input_list)

#Remove the element "Python" from a list of strings
strings_list = ['java','javascript','Python','Scala']
python_string  = 'Python'
if python_string in strings_list:
    strings_list.remove(python_string)
print(strings_list)


#Delete the entire list using the del keyword.
numbers = list(range(10))
print(numbers)
del numbers[::]
print(numbers)

#Use pop() to remove the first element of a list and print the modified list
numbers = list(range(1,10,2))
print(numbers)
numbers.pop(0)
print(numbers)


#Create a list and delete elements based on their value using a list comprehension.
input_list = list(range(1,20,2))
print(input_list)
deleting_elements = [input_list.remove(num) for num in input_list]
deleting_elements



