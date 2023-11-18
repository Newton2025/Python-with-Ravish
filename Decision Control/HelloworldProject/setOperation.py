s = set()

s.add("Kamlesh")

print("{} is the first set".format(s))

s1 = s.copy()

s1.add("Gaurav")

s1.add("HOwrah")

print("{} is the second set".format(s1))


s2 = s1.difference(s)

print("{} is the difference set".format(s2))
