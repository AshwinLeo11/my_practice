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
    

































































































