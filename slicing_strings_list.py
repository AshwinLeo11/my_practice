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





#class human:
 #   def __init__(self,num_heart):
  #      self.num_eyes=2
   #     self.num_ears=2
   #     self.num_nose=1
   #     self.num_heart=num_heart

  #  def eat(self):
   #     print('I can eat anything')

    #def play(self):
     #   print('I love to play')

#class male(human):
 #   def __init__(self,name,heart):
  #      super().__init__(heart)
   #     self.name=name
    #def work(self):
     #   print('I can work')

    #def play(self):
     #   super().play() # to access all the methods and attributes of parent class 
      #  print('I love football') # this method overriding 

   # def display(self):
    #    print(f'Hi I am {self.name} and I have {self.num_heart} heart.')

#male_1 = male('Ashwin',1)
#male_1.play()  # this method overriding 
#print(male_1.num_ears)
#male_1.display()
#male_1.eat()
#male_1.work()




#class human:
#    def __init__(self,num_heart):
#        print('calling init from human')
#        self.num_teeth=32
#        self.num_lips=2
#        self.num_heart=num_heart#

#    def walk(self):
#        print('i can walk anywhere i wish')

#    def work(self):
#        print('i can work from home')

#class male:
#    def __init__(self,name):
#        print('calling init from male')
#        self.name=name

#    def flirt(self):
#        print("i can't flirt")

 #   def work(self):
 #       print('i can code')

#class boy(human,male):
#    def __init__(self,name,heart,language):
#        human.__init__(self,heart)
#        male.__init__(self,name)
#        self.language=language

 #   def play(self):
  #      print('i can play football')

 #   def work(self):
 #       print('i can test anything')

 #   def display(self):
 #       print(f'Hi i am from {self.name} and i work on {self.language} ')


#boy_1 = boy('Ashwin',1,'Python')
#print(boy_1.num_teeth)
#print(boy_1.num_heart)
#print(boy_1.language)
#print(boy_1.display)
#male.work




# multilevel inheritance :


#class human:
#    can_breath= True
#    def __init__(self,num_heart):
#        print('calling init from human class')
#        self.eyes=2
#        self.heart=num_heart
#
#    def work(self):
#        print('i can work all the time')
#
#    def eat(self):
#        print('i can eat anywhere')
#
#class male(human):
#    
#    def __init__(self,name):
#       print('calling init from male class')
#        self.name=name
#
#    def sleep(self):
#       print('i can sleep all the time')
#
#class boy(male):
#    def __init__(self,heart,name,can_dance):
#        human.__init__(self,heart)
#        male.__init__(self,name)
#        self.knowing_dance=can_dance

#    def work(self):
#        super().work()
#        print(' i can code')

#boy_2 = boy(1,"Ash",True)
#print(boy_2.name)
#print(boy_2.knowing_dance)
#print(boy_2.can_breath)
#print(boy.mro())






#class Human:
#    def __init__(self,name,age):
#        print('Calling init from Human class')
#        self.name=name
#        self.age=age

#    def eat(self):
#        print('i can eat')

#    def show_details(self):
#        print(f'name: {self.name}, age : {self.age}')

#class Male(Human):
#    def __init__(self,m_name,age,location):
#        print('this is from Male class')
#        Human.__init__(self,m_name,age)
#        self.location=location

#    def work(self):
#        print('i can work')

#class Female(Human):
#    def __init__(self,name,age,can_cook):
#        super().__init__(name,age)
#        self.knowing_cook=can_cook#

#        def show_details_f(self):
#           Human.show_details(self)
#        print(f'knowing_cook : {self.knowing_cook}')

 #       def sleep(self):
 #           print('I can sleep')
#male_1 = Male("Ashwin",22,'coimbatore')
#female_1 = Female('Harshidha',17,True)
#female_1.show_details()
#print(female_1.age)
#print(male_1.work)
#print(Male.mro())







# hybrid inheritance :

#class A:
#    def display(self):
#        print('display from A class')

#class B(A):
#    def display(self):
#        print('Display from b class')

#class C:
#    def show(self):
#        print('Im from C class')

#class D(B,C):
#    def display(self):
#       print('display from c class')


#d1 = D()
#d1.display()
#print(D.mro())





class Car:
    

    def __init__(self,model,year, drive,color):
        print('hai')
        self.model=model
        self.year=year
        self.car_drive =  drive
        self.color  = color

    def display(self):
        print(' new model car')

    def colour(self):

        print('all colours are avilable')

    def show_details(self):
        print(f'name : {self.model} , year : {self.year}, car_drive : {self.car_drive}')
        item1 = { 'model': self.model,'year':self.year,'car_drive':self.car_drive,'color' :self.color}
        return item1

    

class Volkswagen(Car):
   
    
    def show_details(self):
         res = super().show_details()
         print('The parent value is ',res)
         if res['color'] != 'red':
             print('the model is ', res.get('model')) 
             print('the year is ', res.get('year')) 
             res['model'] = 'Innova'
        
         print('=======updated model is', res)
         pass
    

class Toyota(Volkswagen):
     def __init__(self,price):
          self.price=price
          print(f'price : {self.price}')
          if price >350000 and price >500000  :
               print('you can buy the car',)
          else:
               print("you can't buy the car")

     def show_details(self):
          super().colour()
          print('red color only avilable')
          

c1 = Car('SUV','2004', True,'red')
c1.show_details()

c2 = Volkswagen('PoLo','2026', False,'white')
c2.show_details()

c3 = Toyota(300000)
c3.price
# class Toyota(Car):
#     def __init__(self,)








def rating(self):
        print('all are too good in performance')







