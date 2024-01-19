#  maximum difference between two successive elements

nums = [3, 6, 9, 1]
nums.sort()
max_gap = 0

for i in range(1, len(nums)):
    max_gap = max(max_gap, nums[i] - nums[i - 1])

print(max_gap)
