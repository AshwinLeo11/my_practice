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

#z = set ('b','d')
#z.update(set(['X','Y']))
#print(z)




# Tuples :

tuple = (11,6,-5,'harsh',True)
print(tuple)



tuple_1= (11,6,-5,'harsh',True)
print(tuple_1[-2])

 # type :

tuple_2 = (11,6,-5,'harsh',True)
print(type(tuple_2))


tuple_1 = (11,6,-5,'harsh',True)
tuple_2 = (14,)
print(type(tuple_2))

tuple_2 = (11,6,-5,'harsh',True)
print(tuple_2[1:4])

tuple_2 = (11,6,-5,'harsh',True)
print(len(tuple_2))


tuple_1 = (11,6,-5,'harsh',True)
tuple_2 = (11,22,33,44)
tuple_3 = (tuple_1,tuple_2)
print(len(tuple_3))

tuple_1 = (11,6,-5,'harsh',True)
tuple_2 = (11,22,33,44)
tuple_3= tuple_1 + tuple_2
print(tuple_2)



tuple_1 = (11,6,-5,'harsh',True)
tuple_2 = (11,22,33,44)
tuple_3 = tuple_1 + tuple_2
print(min(tuple_2))


tuple_1 = (11,6,-5,'harsh',True)
tuple_2 = (11,22,33,44)
tuple_3 = tuple_1 + tuple_2
print(tuple_2.count(11))


tuple_1 = (11,6,-5,'harsh',True)
tuple_2 = (11,22,33,44)
tuple_3 = tuple_1 + tuple_2
print(tuple_2.index(11))



#tuple_1 = (11,6,-5,'harsh',True)
#tuple_2 = (11,22,33,44)
#tuple_3 = tuple_1 + tuple_2
#list_1 = [1,2,3,4,5]
#print(tuple(list_1))



tuple_1 = (11,) * 7
print(tuple_1)


















