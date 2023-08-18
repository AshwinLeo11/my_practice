"""
Problem:
Solution:
"""


import decimal
from fractions import Fraction
f = 2.5                                      #Convert float->fraction:two args
z = Fraction(*f.as_integer_ratio())           
print(z)

# excercise 2
"""
hai
"""
from decimal import Decimal
s = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') + Decimal('0.3')
print(s)


# exercise 3

f = decimal.Decimal(1) / decimal.Decimal(7)
print(f)


# excercise 4

decimal.getcontext().prec = 4
g = decimal.Decimal(1) / decimal.Decimal(7)
print(g)



# excercise 5
a = decimal.Decimal('1.00') / decimal.Decimal('3.00')
print(a)


# excercise 6


with decimal.localcontext() as ctx:
    ctx.prec = 2
    b=decimal.Decimal('1.00') / decimal.Decimal('3.00')
    print(b)



# excercise 7



a = decimal.Decimal('1.00') / decimal.Decimal('3.00')
print(a)



# Fraction excercise 1



from fractions import Fraction
x = Fraction(1,3)
y = Fraction(2,3)
print((x,y),(x+y),(x-y),(x*y))

# excercise 2

g = Fraction('.25')
j = Fraction('1.25')
print(g,j,(g+j))



# numeric excercise


a = 1/3.0
b = 4/6.0
print((a,b),(a+b),(a-b),(a*b))


# excersise 2

a = Fraction(1,10) + Fraction(1,10) + Fraction(1,10) + Fraction(3,10)
print(a)


# excercise 3
b = Decimal(0.1) + Decimal(0.1) + Decimal('0.1') + Decimal(0.3)
print(b)


# excercise 4

decimal.getcontext().prec = 2
a = decimal.Decimal(1) / decimal.Decimal(3)
print(a)

# excercise 5

k = decimal.Decimal(str(1/3)) + decimal.Decimal(str(6/12))
print(k)


# excercise  6


b = Fraction.from_float(1.75)
print(b)

# excercise 7


l= Fraction(*(1.75).as_integer_ratio())
print(l)