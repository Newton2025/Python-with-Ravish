#  capitalize the first and last character of each word in a string

example_string = "hello world"
capitalized_string = ' '.join([w[0].upper() + w[1:-1] + w[-1].upper() if len(w) > 1 else w.upper() for w in example_string.split()])
print(capitalized_string)
