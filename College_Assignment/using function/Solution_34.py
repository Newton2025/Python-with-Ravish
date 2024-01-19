# Transform a string into a matrix with K characters each row

input_string = "abcdefghij"
k = 3
matrix = [input_string[i:i + k] for i in range(0, len(input_string), k)]
print(matrix)
