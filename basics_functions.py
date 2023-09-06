# round function excercise :

print(round(7))
print(type(round(7)))

print(round(7,2))
print(type(round(7,2)))

print(round(7.6666,2))
print(type(round(7.6666,2)))

print(round(7.6666))
print(type(round(7.6666)))

print(round(7.5))

print(round(6.5))

print(round(674,2))

print(round(674,-2))

print(round(674,4))

print(round(-8/3))

print(round(-2.5))


# f_strings excercise :

name = 'Ashwin'
age = 22
height = 1.7
print("My name is:"+name,"i am " +str(age),"years old")

print("my name is:", name,"I am",age,"years old", "My height is",height, "meters")

# f_string :

print(f"my name is {name}.I am {age} years old. My height is {height} meters")

print(f"ashwin's father is {age*2} years old.")




# if else  statements excercise :


height = int(input("Enter height in feet:"))
if(height>4):
    print("Buy token")
    print("Now you can board the metro")
else:
    print("No Token required")




height = int(input("Enter height in feet:"))
if(height>4):
    print("Buy token")
    print("Now you can board the metro")
print("Out of if block")


height = int(input("Enter height in feet:"))
if height==3:
    print("Buy token")
    print("Now you can board the metro")
else:
    print("no token required")

# if else coding excercise :

 # problem : check whether given number is even or odd 

number = int(input("Enter the number:"))
if number % 2 == 0:
    print('This number is even')
else:
    print('This number is odd')



# nested if excercise :


a = 52
if a%2 == 0:
    print('even')
    if a>30 :
        print('Number is greater than 30..great :')
print('byee')


# nested if else excercise :

height = int(input('enter your height in feet ?'))
if height>=3:
    print('can ride')
    age = int(input('What is your age?'))
    if age<=18:
        print('pay 250 Rs.')
    else:
        print('pay 500 Rs')
else:
    print ("can't ride")
print('byee')
           
          
# nested elif excercise :


height = int(input('Enter yoyr height in feet:'))
if height>=4:
    print('can ride')
    age = int(input('enter your age?'))
    if age<12:
        print('pay 150 Rs.')
    elif age<=18:
        print('pay 250 Rs.')
    else:
        print('pay 500 Rs.')
else:
    print("can't ride")
print('bye')



# nested if excercise :

# problem : how to calculate bmi and its basic categories :


weight = float(input('Enter weight in kg:'))
height = float(input('Enter your height in meter:'))
bmi = round(weight/height**2)
if bmi<18.5:
    print(f'your BMI is {bmi} and you are under weight.')
elif bmi<25:
    print(f'your BMI is{ bmi} and you have a normal weight.')
elif bmi<30:
    print(f'your BMI is {bmi} and you are overweight.')
elif bmi<35:
    print(f'your BMI is {bmi} and you are obese.')
else:
    print(f'your BMI is {bmi} and you are clinically obese.')




# excercise     

# problem : how to check whether given a year is leap year or not :

year = int(input('which year you want to check?'))
if year % 4 == 0:
    if year % 100 == 0:
        if year %  400 == 0:
            print('leap year')
        else:
            print('not a leap year')
    else:
        print('not a leap year')
else:
    print('Not a leap year')




# multiple if statements :
 
height = int(input('what is your height?'))
bill = 0
if height>=5 :
    print('can ride')
    age = int(input('Enter your age?'))
    if age<15:
        bill = 300
        print('Ticket price is 150 Rs.')
    elif age<20:
        bill = 500
        print('Ticket price is 250 Rs.')
    else :
        bill = 700
        print('Ticket price is 500 Rs.')
        want_photo = input('Do  you want to take a photo(y/n)?')
        if want_photo == 'y' or want_photo == 'Y':
            bill = bill + 100
        print(f'Your total bill is{bill}.')
else:
    print("can't ride")
    print('Thank you.. Enjoy the ride')
             






























