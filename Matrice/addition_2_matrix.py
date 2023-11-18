m1=[]
m2=[]
m=[]
print("Here You Can Add Your 2X2 Matrix")
print("Enter Elements in 1st Matrix")
for i in range(2):
    r1=int(input("Row Element: "))
    m1.append(r1)
    r1=int(input("Coloumb Element: "))
    m1.append(r1)
print("Enter Elements in 1st Matrix")
for i in range(2):
    r2=int(input("Row Element: "))
    m2.append(r2)
    r2=int(input("Coloumb Element: "))
    m2.append(r2)
for i in range(4):
    r=m1[i]+m2[i]
    m.append(r)
print('[{}     {}\n{}     {}]'.format(m[0],m[2],m[1],m[3]))