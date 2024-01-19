#length of the longest consecutive elements sequence

nums = [100, 4, 200, 1, 3, 2]
nums_set = set(nums)
max_length = 0

for num in nums_set:
    if (num-1) not in nums_set:
        current_num = num
        current_length = 1

        while (current_num +1) in nums_set:
            current_num += 1
            current_length += 1

        max_length = max(max_length, current_length)

print(max_length)
