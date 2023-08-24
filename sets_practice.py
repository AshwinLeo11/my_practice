#excercise 1

x = set ('abcde')
y = set ('xyzhk')
print(x)


# excercise 2

x = set ('basha')
y = set ('hanis')
z = x-y
a = x|y
b = x&y
c = x^y
d = x>y, x<y
print(z)
print(a)
print(b)
print(c)
print(d)


# excercise 3

z = set (['b','d'])
z.add('SPAM')
print(z)



# excercise 4

z = set ('b','d')
z.update(set(['X','Y']))
print(z)