def reversing_integer(given_number):
    reverse_number = 0
    while given_number > 0:
        digit = given_number % 10
        reverse_number = reverse_number*10 + digit
        given_number = given_number // 10
    return reverse_number
print(reversing_integer(12345))