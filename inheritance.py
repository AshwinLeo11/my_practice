class human:
    def __init__(self):
        self.num_eyes=2
        self.num_ears=2
        self.num_nose=1

    def eat(self):
        print('u can eat anything')

    def play(self):
        print('I love to play')

class male(human):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def work(self):
        print('i can work')

    def play(self):
        super().play() # to access all the methods and attributes of parent class 
        print('i love football') # this method overriding 

male_1 = male
male_1.play()  # this method overriding 
print(male_1.num_ears)
































































































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
