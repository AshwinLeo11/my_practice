
# single inheritance :


class human:
    def __init__(self,num_heart):
        self.num_eyes=2
        self.num_ears=2
        self.num_nose=1
        self.num_heart=num_heart

    def eat(self):
        print('u can eat anything')

    def play(self):
        print('I love to play')

class male(human):
    def __init__(self,name,heart):
        super().__init__(heart)
        self.name=name
    def work(self):
        print('i can work')

    def play(self):
        super().play() # to access all the methods and attributes of parent class 
        print('i love football') # this method overriding 

    def display(self):
        print(f'Hi I am{self.name} and I have{self.num_heart} heart.')

male_1 = male('Ashwin',1)
male_1.play()  # this method overriding 
print(male_1.num_ears)
male_1.display()




# multiple inheritance :


class human:
    def __init__(self,num_heart):
        print('calling init from human')
        self.num_teeth=32
        self.num_lips=2
        self.num_heart=num_heart

    def walk(self):
        print('i can walk anywhere i wish')

    def work(self):
        print('i can work from home')

class male:
    def __init__(self,name):
        print('calling init from male')
        self.name=name

    def flirt(self):
        print("i can't flirt")

    def work(self):
        print('i can code')

class boy(human,male):
    def __init__(self,name,heart,language):
        human.__init__(self,heart)
        male.__init__(self,name)
        self.language=language

    def play(self):
        print('i can play football')

    def work(self):
        print('i can test anything')

    def display(self):
        print(f'Hi i am from {self.name} and i work on {self.language} ')


boy_1 = boy('Ashwin',1,'Python')
print(boy_1.num_teeth)
print(boy_1.num_heart)
print(boy_1.language)
print(boy_1.display)
male.work



# multilevel inheritance :


class human:
    can_breath= True
    def __init__(self,num_heart):
        print('calling init from human class')
        self.eyes=2
        self.heart=num_heart

    def work(self):
        print('i can work all the time')

    def eat(self):
        print('i can eat anywhere')

class male(human):
    can_walk = False
    def __init__(self,name):
        print('calling init from male class')
        self.name=name

    def sleep(self):
        print('i can sleep all the time')

class boy(male):
    def __init__(self,name,heart,can_dance):
        human.__init__(self,heart)
        male.__init__(self,name)
        self.knowing_dance=can_dance

    def work(self):
        super().work()
        print(' i can code')

boy_2 = boy(1,'Ash',True)
print(boy_2.name)
print(boy_2.knowing_dance)
print(boy_2.can_breath)
print(boy_2.can_walk)
print(boy.mro())



# Hierarchical inheritance :

class Human:
    def __init__(self,name,age):
        print('Calling init from Human class')
        self.name=name
        self.age=age

    def eat(self):
        print('i can eat')

    def show_details(self):
        print(f'name: {self.name}, age : {self.age}')

class Male(Human):
    def __init__(self,m_name,age,location):
        print('this is from Male class')
        Human.__init__(self,m_name,age)
        self.location=location

    def work(self):
        print('i can work')

class Female(Human):
    def __init__(self,name,age,can_cook)
        super().__init__(name,age)
        self.knowing_cook=can_cook

        def show_details_f(self):
            Human.show_details(self)
        print(f'knowing_cook : {self.knowing_cook}')

        def sleep(self):
            print('I can sleep')
male_1 = Male("Ashwin",22,'coimbatore')
female_1 = Female('Harshidha',17,True)
print(female_1.age)
print(female_1.sleep)
print(male_1.work)
print(male_1.mro())

        

# hybrid inheritance :

class A:
    def display(self):
        print('display from A class')

class B(A):
    def display(self):
        print('Display from b class')

class C:
    def show(self)
        print('Im from  C class')

class D(B,c):
    def display(self):
        print('display from c class')


d1 = D()
d1.display()
print(D.mro())




# 

class Car:
    can_drive = True

    def __init__(self,year):
        self.year=year

    def display(self):
        print(' new model car')

    def colour(self):
        print('all colours are avilable')

    def model(self):
        print('some models only avilable')

    

class Volkswagen(Car):
    def __init__(self,rating):
        print('')
        



class Toyota(Car):
    def __init__(self,)








def rating(self):
        print('all are too good in performance')




























































#class car:
 #   def fun_1(self):
  #      print('This was a new car_1')

   # def fun_2(self):
    #    print('This was a new car_2')

    #def fun_3(self):
    #   print('This was a new car_3')

    #def fun_4(self):
     #   print('This was new car_4')
#class volkswagen(car):
 #   def fun_5(self):
   #     super().fun_1()
  #      print('Red polo')
#class hyundai(car):
 #   def fun_6(self):
  #      super().fun_1()
   #     print('white city')



# hybrid inheritance :

#class games:
 #   def display(self):
  #      print('love to play')

#class cricket(games):
 #   def display(self):
  #      print('i love cricket')

#class chess:
 #   def show(self):
  #      print('indoor game')

#class football(cricket,chess):
 #   def display(self):
  #      print('pyaar')

#play = football()
