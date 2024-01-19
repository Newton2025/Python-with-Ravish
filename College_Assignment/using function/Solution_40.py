#  accepts a number as a parameter. The function should return a number that’s the difference between the largest and smallest numbers that the digits can form in the number

def diff_largest_smallest(num):
    digits = [int(digit) for digit in str(num)]
    largest_num = int(''.join(map(str, sorted(digits, reverse=True))))
    smallest_num = int(''.join(map(str, sorted(digits))))
    return largest_num - smallest_num

result = diff_largest_smallest(213)
print(result)
