# list

numbers = [10,3,5,7]
print(numbers[3])


names = ['Ashwin','Harshidha']
print(names)

mix_list = [11,'Harshidha',True,1.3]
print(mix_list)


numbers = [ 2,4,1,7,5]
print(len(numbers))

# list slicing :

numbers = [3,4,5,8,1]
print(numbers[1:3])

numbers = [3,56,24,12,23,-84]
print(numbers[0:5:2])

numbers = [ 11,33,55,63,67,34,]
print(numbers[1:3])


# sort the list :

numbers = [ 1,45,79,23,11,45,11,-94]
numbers.sort()
print(numbers)

# reverse  :

numbers = [2,34,54,-23,-11,11]
numbers.reverse()
print(numbers)


# min & max functions :

numbers = [ 9,25,1,-1,7,-4,3]
print(max(numbers))

print(min(numbers))


# add :
# append (add one data item ) :

numbers = [1,56,67,83,45,12]
numbers.append(11)
print(numbers)


# insert (specific index) :

numbers = [ 23,34,56,78,98,23,45,43,62]
numbers.insert(2,11)
print(numbers)

# extend (add end of the list more than one data item) :

numbers = [ 23,34,56,78,98,23,45,43,62]
numbers.extend([45,43,11,23,61])
print(numbers)

# Change the list :

numbers = [ 23,34,56,78,98,23,45,43,62]
numbers[4] = 11
print(numbers)


numbers = [ 23,34,56,78,98,23,45,43,62]
numbers [1:4]= [22,33,55]
print(numbers)


# remove       :

numbers = [23,34,56,78,98,23,45,43,62]
numbers.remove(43)
print(numbers)


numbers = [23,34,56,78,98,23,45,43,62]
print(numbers.pop(6))
print(numbers)



# count   :

#numbers = [23,34,56,78,98,23,45,43,62]
#numbers.count()
#print(numbers)



#index :






# clear




# len :

list_1= [4,3,4,6,67,76,2]
len(list_1)



# randomization  :

import random

a =random.randint(1,7)
print(a)


a = random.randrange(1,4)
print(a)


a = random.random()
print(a)


a = random.uniform(1,3)
print(a)


l = [2,45,11,8,67]
a = random.choice(l)
print(a)


l = [2,45,11,8,67]
a = random.shuffle(l)
print(l)



































