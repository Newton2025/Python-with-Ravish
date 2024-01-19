#  longest common prefix

strs = ["flower", "flow", "flight"]
prefix = strs[0]

for string in strs[1:]:
    i = 0
    while i < len(prefix) and i < len(string) and prefix[i] == string[i]:
        i += 1

    prefix = prefix[:i]

print(prefix)
