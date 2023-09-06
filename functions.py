def hello_func() :
    return 'Hello Function.'
print(hello_func())




def hello_func() :
    return 'hello function.'
print(hello_func().upper())


def hello_func(greeting) :
    return '{} function.' .format(greeting)
print(hello_func('Hi'))



def hello_func(greeting, name ='You'):
    return '{},{}'.format(greeting,name)
print(hello_func('Hi',name ='Ashwin'))


def student_info (*args,**kwargs):
    print(args)
    print(kwargs)

student_info('math','art',name='Ashwin',age=22)

courses = ['maths','physics']
info = {'name':'Ashwin','age':22}
student_info(courses,info)


def student_info (*args,**kwargs):
    print(args)
    print(kwargs)

student_info('math','art',name='Ashwin',age=22)

courses = ['maths','physics']
info = {'name':'Ashwin','age':22}
student_info(*courses,**info)

# import modules and exploring :

from my_module import find_index as ash
courses = ['English','Compsci','Physics']
index = ash(courses,'Compsci')
print(index)



from my_module import find_index, test
courses = ['Maths','English','Compsci']
index = find_index(courses,'English')
print(index)
print(test)



from my_module import find_index, test, test_1
courses = ['Maths','English','Compsci']
index = find_index(courses,'English')
print(index)
print(test)
print(test_1(5))


