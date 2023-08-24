# add digit of number excercise :

number = input("enter a two digit number: ")
first_digit = number[0]
second_digit = number[1]
new_1 = int(first_digit)
new_2 = int(second_digit)
print(new_1 + new_2)



#  Arithimetic operator excercise :

print(5+2)

print(5/2)

print(4/2)

print(4//2)

print(4**2)

print(5 % 2)

print(5 + 2 * 3 - 1 + 10 / 5)

a = 5
b = 3
print(a/b)


# BMI excercise


weight = input("Enter weight in kg: ")
height =input("Enter height in meter: ")
BMI = int(weight)/float(height) ** 2
print(int(BMI))



# assignment operator excercise :

a = 5
print(a)

a,b,c = 3,4,5
print(a,b,c)

a,b =4,3
c = a + b
a += 2
c += a  #c=c+a
print(c)

a = 2
b = 6
c = a + b
a += 2
c //= a  #c=c/a
print(c)


# comparison operators excercise :

a =5

print(a==5)
print(a<=5)
print(a<5)
print(a!=5)
print(a>6)
print(a>=5)



# logical operators excercise :

# AND

a = 4
b = 3
print(a<3 and b==3)
print(a>3 and b==3)


a,b = 3,6
c = False
print(a<=3 and c)


# OR

a = 6
b = 1
print(a<6 or b==1)


a,b = 3,6
c = False
print(a<=3 or c)


# NOT

a = 8
b = 2
c = True
print(not(c))


# bitwise operators excercise :


a = 6
b = 8
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(~b)
print(a << 2)
print(a >> 2)
print(a << 5)
print(a >> 3)
print(a << 4)
print(a << 6)

# excercise :

# and

a = 26
b = 23
print(a & b)

# or

a,b =17,24
print(17 | 24)

# XOR

a,b = 17,24
print(17 ^ 24)

#  NOT

a = 45
print(not(a))

# left shift

a = 68
print(a <<2)

# Right shift

a = 56
print(a >> 3)


# identity operators excercise :

a = 7
b = 7
print(id(a))
print(id(b))
print(a is b)
print( a is not b)


a = 4
b = '4'
print(id(a))
print(id(b))
print(a is b)
print( a is not b)

a = 6
print(id(a))
a = 2
print(id(a))

a = 5
b = 5.0
print(id(a))
print(id(b))
print(a is b)


#  membership operators  excercise :

str = 'Harsh Ash'
print('S'in str)
print('r' in str)
print('Harshash'in str)
print('h' not in str)
print('o' not in str)


list_1 =[4,8,11,6,25]
print(11 in list_1)
print(25 in list_1)
print(7 not in list_1)

 





































































