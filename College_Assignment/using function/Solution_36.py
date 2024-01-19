# Given a List, extract both next and previous elements for each element

list2 = [3, 7, 9, 3]
output = [(list2[i - 1] if i > 0 else None, list2[i + 1] if i < len(list2) - 1 else None) for i in range(len(list2))]
print(output)
