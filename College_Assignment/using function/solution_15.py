# multiply each number of a given list with a given number using lambda function

numbers = [1, 2, 3, 4]
multiplier = 2
result = list(map(lambda x: x * multiplier, numbers))
print(result)
