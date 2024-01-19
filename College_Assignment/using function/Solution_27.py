#  accept the strings which contain all vowels

def contains_all_vowels(s):
    vowels = set("aeiou")
    return set(s.lower()) >= vowels

example_string = "education"
result = contains_all_vowels(example_string)
print(result)
