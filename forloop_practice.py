# forloop :

name = 'Ashwin'
for i in name :
    print(name)


name = ['Harsh',' Ashwin']
for i in name :
    print(i)
    if i == 'Harsh' :
        print('Hey its me')



numbers = [1,11,8,25,-3]
for i in numbers :
    square = i ** 2
    print(square)



numbers = [8,25,11,6,10]
squares = []
for i in numbers :
    square = i ** 2
    squares.append(square)
print('The list of squares is:',squares)


numbers = (11,22,33,44,55)
for i in numbers :
    square = i ** 3
    print(square)



# for else :

tuple_1 = (2,3,56,78,1,11,25)
for i in tuple_1 :
    print(i)
else :
    print('Loop suceesfully completed and we are in else block!!!')



tuple_2 = (11,25,8,6)
for i in tuple_2 :
    print(i)
    if i == 8 :
        break
else :
        print('Loop sucessfully completed and we are in else block now!!!')
print('out of  for/else')


tuple_3 = (25,11,8,6,24,16)
for i in tuple_3 :
    if i % 8 == 0 :
        print(i)
        break
    else :
        print('There is no number divisible by 6 in this sequence!!')


tuple_4 = (11,6,8,25)
for i in tuple_4 :
    if i % 7 == 0 :
        print(i)
        break 
else :
    print('There is no number divisible by 6 in this sequence !!')
    


# for loop & range () function in python  :

a = range(2,5)
print(a[0])


b = range (2,15,3)
for i in a :
    print(i)


c = range (3,15,-4) # i =2 j = 15  k = -4
for i in a :
    print(i)


# we have to add numbers from 1 to 100 :

total = 0
for i in range (0,101):
    total += i
print(total)






total = 0
for i in range(2,101,2): # 2 4 6 8 .... 100
    total += i
print(total)


total = 0
for i in range (1,101) : # 1 2 3 4 5 .... 100
    if i % 2 == 0:
        total += i
print(total)



# while loop in python :

count = 1
while count < 5 :
    print(count)
    count += 1
print('out from loop')


count = 5
while count >0 :
    print(count)
    count -= 1
print('out from while loop')




count = 5
while count >0 : print(count) ;count -= 1
print('out from while loop')



count = 7 
while count < 9 :
    print(count)
    count += 1
else :
    print('in else block')
print('out from the loop')



count = 5
while count>0 :
    print(count)
    count -= 1
    if count == 3 :
        break
else :
    print('in else block')
print('out from the loop')



number = int(input('enter a number (-7 to quit)'))
while number !=-7 :
    print(number)
    number = int(input('enter a number(-7 to quit'))
else :
    print('in else block')
print('out from loop')


count = 0 
while True:
    print(count)
    count += 1
    if count == 5 :
        break 
else :
        print('in else block')
print('out from loop')


# calculte sum of positive integers :


total = 0 
number = int (input('enter a number (0 to quit):'))
while number !=0 :
    total = total + number 
    number = int(input('engter a number(0 to quit)'))
print(f'total is',{total})






















































