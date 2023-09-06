#my_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   #        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
   #       -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
   # list[start:end:step]
 # print my_list[6::-1]



 # string slicing ;

#sample_url ='http://ashwins.com'
#print (sample_url)

# reverse the url :
#print (sample_url[: :-1])


# get the top level domain :
#print (sample_url[-4:])


# print the url without http://
#print (sample_url[7:])



# print the url without  the http:// or the top level of domain :
#print (sample_url[7:-4])


# list,set,tuple comprehension :\

#nums = [1,2,3,4,5,6,7,8,9,10]
#my_list = [n*n for n in nums]
#print(my_list)

# using a map + lambda

#my_list = map(lambda n: n*n, nums)
#print(my_list)

#my_list = [ n for n in nums if n%2 == 0]
#print(my_list)

#my_list = filter(lambda n: n%2 == 0, nums)
#print(my_list)


#my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
#print(my_list) 


# Dictionary comprehensions :
#name  = ['Ashwin','Shaji','Pradeep','Hari','Dravid']
#hero = ['Thar','Batman','Spiderman','Superman','Captain']
#print (zip(names,Heroes))

# i want dict a {'name': 'hero} fo reach name hero in zip (names,heros)

#my_dict = {}
#for name, hero in zip(name,hero) :
#    my_dict[name] =hero
#print(my_dict)

#my_dict ={name : hero for name,hero in zip(name,hero)}
#print(my_dict)


# set comprehensions :

#nums = [1,2,3,4,5,6,7,8,9,10]
#my_set = set()
#for n in nums :
#    my_set.add(n)
#print(my_set)

#my_gen =(n*n for n in nums)
#for i in my_gen :
#    print(i)



# sorting list,Tuples & List :
# ascending order :

#li = [9,1,4,7,2,8,3,5,6]
#s_li = sorted(li)
#print('sorted variable:\t',s_li)
#li.sort()
#print('original variable:\t',li)


# decending order :

#s_li = sorted(li,reverse=True)
#print('sorted variable:\t',s_li)
#li.sort()
#print('original variable:\t',li)

#li = [9,1,4,7,2,8,3,5,6]
#s_li = sorted(li,key = abs)
#print(s_li)

# tuple sorted :

#tup = (8,1,2,7,5,9,4,6,3)
#s_tup = sorted(tup)
#print(s_tup)

# dictionary :

#di = {'Name':'Ashwin','Job':'Python Developer','Age':22,'Company':'Pinnacle 7 Technologies'}
#s_di = sorted(di)
#print(s_di)



#class human:
 #   def __init__(self):
  #      self.num_eyes=2
   #     self.num_ears=2
    #    self.num_nose=1
   # def eat(self):
   #     print('u can eat anything')

   # def play(self):
   #     print('I love to play')

#class male(human):
    #def work(self):
   #     print('i can work')

  #  def play(self):
 #       super().play() # to access all the methods and attributes of parent class 
 #       print('i love football') # this method overriding 

#male_1 = male
#male_1.play()  # this method overriding 
#print(male_1.num_ears)





class human:
    def __init__(self,num_heart):
        self.num_eyes=2
        self.num_ears=2
        self.num_nose=1
        self.num_heart=num_heart

    def eat(self):
        print('I can eat anything')

    def play(self):
        print('I love to play')

class male(human):
    def __init__(self,name,heart):
        super().__init__(heart)
        self.name=name
    def work(self):
        print('I can work')

    def play(self):
        super().play() # to access all the methods and attributes of parent class 
        print('I love football') # this method overriding 

    def display(self):
        print(f'Hi I am {self.name} and I have {self.num_heart} heart.')

male_1 = male('Ashwin',1)
male_1.play()  # this method overriding 
print(male_1.num_ears)
male_1.display()
male_1.eat()
male_1.work()















