#  find numbers divisible by nineteen or thirteen from a list of numbers using Lambda

numbers = [19, 26, 13, 39, 52, 65]
divisible_by_19_or_13 = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))
print(divisible_by_19_or_13)
