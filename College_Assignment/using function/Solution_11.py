#  check if a string has at least one letter and one number

example_string = "abc123"
has_letter_and_number = any(char.isalpha() for char in example_string) and any(char.isdigit() for char in example_string)
print(has_letter_and_number)
