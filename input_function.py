# input function excercise
input("what is your name?")


print("Hello"+" "+"Jenny")


# excercise 2

print("Hello"+" "+input("what is your name?"))

# excercise 3

print("Hey Jenny"+" "+input("what is your name?"+" "+"how are you"))


# variables excercise-1 

name = input("What is your name?")
length = len(name)
print(length)


# ecxcercise-2

a = 1
b ="harsh"
print(a)
print(b)

# excercise-3

a = "Ash"
b = "Harsh"
print(a+b)



# swap 2 numbers excercise  

a = input("enter value of a = ")
b = input("enter value of b = ")
temp = a
a = b
b = temp
print("a=" + a)
print("b=" + b)



# primitive data types excersise 

var_1 = 3
print(type(var_1))

var_1 = 0o1232
var_2 = 0x103
var_3 = 123
print(type(var_1))
print(type(var_2))
print(type(var_3))


name_1 = "Jenny khatri"
name_2 = "cs faculty"
print(name_1 + name_2)
print(name_1[6] +name_2[1])



#   excercise-2



name_1 = "123"
name_2 = "1"
a = 1
print("123" + "1")



print("Jenny\'s \n \"Lectures\"")
print(5* "Jenny\'s  \\n \"Lectures\"")

# excercise-3


var = True
print(var)
print(type(var))



# excercise-4


a=1
b=2
var = a<b
print(var)
print(type(var))



# type_error excercise


print(len("Ashwin"))

length = len("Harshu")
print("Your name has " +str(length) + " characters")
new_length = str(length)
print(type(new_length))
print(type(length))


print(int("10") + int("10"))
 
print(10 + float("10"))

name ="123"
print(10 + int(name))



# excercise

first_number = input("enter first number: ")
second_number = input("enter second number: ")
sum = int(first_number) + int (second_number)
print(sum)
