# cumulative sum of a list

original_list = [1, 2, 3, 4, 5]
cumulative_sum = [sum(original_list[:i + 1]) for i in range(len(original_list))]
print(cumulative_sum)
