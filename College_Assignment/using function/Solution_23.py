# all positive and negative numbers in a list

numbers = [3, -1, 8, -4, 5]
positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num < 0]
print("Positive Numbers:", positive_numbers)
print("Negative Numbers:", negative_numbers)
