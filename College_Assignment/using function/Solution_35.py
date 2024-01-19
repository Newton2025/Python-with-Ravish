# extract only the numbers from a list which have some specific digits

list1 = [3456, 23, 128, 235, 982]
digit_list = [2, 3, 5, 4]
output = [num for num in list1 if any(str(digit) in str(num) for digit in digit_list)]
print(output)
