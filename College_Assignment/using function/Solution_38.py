# Input the string "Honorificabilit" and check for the minimum frequent vowel and maximum frequent consonant

word = "Honorificabilit"
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
vowel_counts = {vowel: word.lower().count(vowel) for vowel in vowels}
consonant_counts = {consonant: word.lower().count(consonant) for consonant in consonants}

min_vowel = min(vowel_counts, key=vowel_counts.get)
max_consonant = max(consonant_counts, key=consonant_counts.get)

print("Min Vowel:", min_vowel)
print("Max Consonant:", max_consonant)
