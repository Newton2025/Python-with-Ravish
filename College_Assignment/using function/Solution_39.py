# Find out the 3rd highest element from an input list

numbers = [12, 45, 78, 34, 56, 23]
third_highest = sorted(set(numbers), reverse=True)[2]
print(third_highest)
