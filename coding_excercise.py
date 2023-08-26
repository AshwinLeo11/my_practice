# pizza order program using if statements :



size = input('What size of pizza do you want(S/M/L)?')
bill = 0
if size == 'S' or size == 's':
    bill += 100
    print('Small pizza price is 150 Rs.')
elif size == 'M' or size == 'm':
    bill += 200
    print('Medium pizza price is 250 Rs.')
else :
    bill += 300
    print('Large pizza price is 350 Rs.')

add_pepperoni = input('DO you want pepperoni(y/n)?')
if add_pepperoni == 'y' or add_pepperoni == 'y':
    if size == 'S' or size == 's':
        bill += 50
    else: 
        bill += 80

extra_cheese = input('Do you want extra chesse(y/n)?')
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill += 30

print(f'your final bill is {bill}')  



# Love calculator program using if statments :


name_1 = input('What is your name?')
name_2 = input('What is her name?')
combine_string = name_1 +name_2
lower_case_string = combine_string.lower()

h = lower_case_string.count('h')
s = lower_case_string.count('s')
hs = h + s


a = lower_case_string.count('a')
i = lower_case_string.count('i')
ai = a + i

love_score = int(str(hs) + str(ai))

if love_score <10 or love_score >90:
    print(f'Your love score is{love_score} and you will be mine always.')
elif love_score >=30 and love_score >=50:
    print(f'Your love score is {love_score} and always stay together in yours life.')
else:
    print(f'Your love score is {love_score} and always be happy')




# head or tail program :

import random

side = random.randint(0,1)
print(side)
if side == 1 :
    print('Heads')
else :
    print('Tails')
    


































































