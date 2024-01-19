# Alphabets ladder Pattern

char = ord('A')
for i in range(1, 6):
    for j in range(i):
        print(chr(char), end=" ")
        char += 1
    print()
