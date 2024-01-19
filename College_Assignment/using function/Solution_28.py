# Frequency of all numbers in a string

numbers_string = "1234512345"
frequency = {num: numbers_string.count(num) for num in set(numbers_string)}
print(frequency)
