
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



tuple_1 = (11,6,-5,'harsh',True)
tuple_2 = (11,22,33,44)
tuple_3 = tuple_1 + tuple_2
print(tuple_3)



tuple_1 = (11,) * 7
print(tuple_1)




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


set_1 ={1,2,7,45,'Ashwin',11,True}
print(set_1)

set_1 = {10,23,45,11,65,'harsh',11}
set_2 = { }
print(type(set_1))
print(type(set_2))


set_1 = {9,8,7,6,5,1,'Ash',11,False}
set_2 = set()
print(type(set_1))
print(type(set_2))

set_1 = {22,44,66,88,22,65,'Harshidha',11}
set_1.add(11)
print(len(set_1))



set_1 = {99,23,19,11,65,'Harshu',11,True}
set_1.remove(11)
print((set_1))


set_1 = {10,23,29,98,23,'Ashu',11,}
set_1.discard(68)
print(set_1)

set_1 = {92,49,17,28,38,'Harshu',False}
set_1.clear()
print(set_1)


set_3 ={'Ashwin','Harshidha','Harshu','Ash'}
set_3.pop()
print(set_3)


set_3 ={'Ashwin','Harshidha','Harshu','Ash'}
print(set_3.pop())

set_3 ={'Ashwin','Harshidha','Harshu','Ash'}
set_3.add((11,25,6,8))
print(set_3)

#set_4 = {11,25,8,6}
#set_4.add(['Ashwin','Harshidha'])
#print(set_4)


# operations on sets :

set_1 = {'Ashwin','Harshidha','Harsh','Ash'}
set_2 = {'harshu','Ash','Harsh','Ashu'}
print(set_1.union(set_2))


set_1 = {'Ashwin','Harshidha','Harsh','Ash'}
set_2 = {'harshu','Ash','Harsh','Ashu'}
print(set_1 | set_2)

set_1 = {'Ashwin','Harshidha','Harsh','Ash'}
set_2 = {'harshu','Ash','Harsh','Ashu'}
set_3 = {'Harshash'}
print(set_1 | set_2 | set_3)

set_1 = {'Ashwin','Harshidha','Harsh','Ash'}
set_2 = {'harshu','Ash','Harsh','Ashu'}
set_3 = {'Harshash'}
print(set_1.union(set_2,set_3))

set_3 = {'Harshidha'}
print(set_3.union(('Ashwin','Harshu')))

set_1 = {'Ashwin','Harshu'}
set_2 = {'Harshkutty'}
set_1.update(set_2)
print(set_1)


# intersection :

set_1 = {'Ashwin','Harshidha','Harsh','Ash'}
set_2 = {'harshu','Ash','Harsh','Ashu'}
set_3 = {'Harshash'}
print(set_1.intersection(set_2,set_3))



set_1 = {'Ashwin','Harshidha','Harsh','Ash'}
set_2 = {'harshu','Ash','Harsh','Ashu'}
set_3 = {'Harshash'}
print(set_1 & set_2)


set_1 = {'Ashwin','Harshidha','Harsh','Ash'}
set_2 = {'harshu','Ash','Harsh','Ashu'}
set_3 = {'Harshash'}
print(set_1.intersection(['ashharsh','ashuharshu']))


set_1 = {'Ashwin','Harshidha','Harsh','Ash'}
set_2 = {'harshu','Ash','Harsh','Ashu'}
set_3 = {'Harshash'}
set_1.intersection_update(set_2)
print(set_1)


set_1 = {'Ashwin','Harshidha','Harsh','Ash'}
set_2 = {'harshu','Ash','Harsh','Ashu'}
set_3 = {'Harshash'}
set_2.intersection_update(set_1)
print(set_1)
print(set_2)


# difference methods :

set_1 = {'Ashwin','Harshidha','Harsh','Ash'}
set_2 = {'harshu','Ash','Harsh','Ashu'}
set_3 = {'Harshash'}
print(set_1.difference(set_2))

set_1 = {'Ashwin','Harshidha','Harsh','Ash'}
set_2 = {'harshu','Ash','Harsh','Ashu'}
set_3 = {'Harshash'}
print(set_1 - set_2)


set_1 = {'Ashwin','Harshidha','Harsh','Ash'}
set_2 = {'harshu','Ash','Harsh','Ashu'}
set_3 = {'Harshash'}
print(set_1.difference(('AshHarshu','HarshuAsh')))


set_1 = {'Ashwin','Harshidha','Harsh','Ash'}
set_2 = {'harshu','Ash','Harsh','Ashu'}
set_3 = {'Harshash'}
print(set_1.difference(set_2,set_3))


# Operations on sets :

set_1 = {1,2,3,4,5}
set_2 = {4,10,7,8,-10}
print(set_1.isdisjoint(set_2))


set_1 = {'Ashwin','Harshidha'}
set_2 = {'Harsh','Ash'}
print(set_1.isdisjoint(set_2))


set_1 = {'Ashwin','Harshidha'}
set_2 = {'Harsh','Ash'}
print(set_1.isdisjoint(['Harshu','Ashu']))

# subset :
 

set_1 = {1,2,3,4,5}
set_2 = {4,10,7,8,-10}
print(set_1.issubset(set_2))



set_1 = {'Ashwin','Harshidha'}
set_2 = {'Harsh','Ash'}
print(set_1 <= set_2)



set_1 = {'Ashwin','Harshidha'}
set_2 = {'Harsh','Ash'}
print(set_1 <= set_1)

# superset :

set_1 = {'Ashwin','Harshidha','Harsh','Ash'}
set_2 = {'Harsh', 'Ash'}
print(set_1.issuperset(set_2))


set_1 = {'Ashwin','Harshidha'}
set_2 = {'Harsh', 'Ash'}
print(set_2.issuperset(set_1))


set_1 = {'Ashwin','Harshidha','Harsh','Ash'}
set_2 = {'Harsh', 'Ash'}
print(set_1.issuperset(set_2))
print(set_1 >= set_2)

# del

set_1 = {'Ashwin','Harshidha','Harsh','Ash'}
set_2 = {'Harsh', 'Ash'}
set_2.clear()
print(set_2)


set_1 = {'Ashwin','Harshidha','Harsh','Ash'}
set_2 = {'Harsh', 'Ash'}
del set_2
print(set_1)












