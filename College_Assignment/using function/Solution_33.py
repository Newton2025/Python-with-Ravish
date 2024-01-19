# display the words in a phrase that have the greatest and lowest ASCII values of characters

phrase = "Python is awesome"
words = phrase.split()
max_word = max(words, key=lambda w: sum(map(ord, w)))
min_word = min(words, key=lambda w: sum(map(ord, w)))
print("Word with Max ASCII:", max_word)
print("Word with Min ASCII:", min_word)
