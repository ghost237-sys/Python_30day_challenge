#Classes and Objects

#A class is simply a user defined type 
#an object is an instance of a class
#for example;
class time:
	"""this is a class"""

t1 = time()#this is an object
print(t1)#this would output <__main__.time object at 0x7fd5218cfbe0>
#its an object of the type time
#you can assign values to an instance...this values are called Attributes
#attributes
time.hour = 10
time.minute = 39
print(time.hour)# would output 10


#methods
#this is a function that is associated with a particular class but they are invoked differently from the syntax for calling a function
#the __init__ method is a special method that gets invoked when an object is instantiated

class Time:#note this class has an uppercase T
	def __init__(self,hour,minute,second):
		self.hour = hour
		self.minute = minute
		self.second = second
		#the __str__method
		#this is a special method that is used to return a string representation of an object
	def __str__(self):
		return '%.2d:%.2d:%.2d'%(self.hour,self.minute,self.second)


T1 = Time(14,30,12)#you have to input the parameters as defined in the class 
print(T1.hour)#this would output 14 and so on

time = Time(9,45,0)
print(time)#insted of outputing the type it prints out the 09:45:00

 
#another common example on the topic of classes and objects is below

class Dog:#defined the class Dog
	def __init__(self,name,age,breed):
		self.name = name 
		self.age = age
		self.breed = breed

	def bark(self):
		print('bark')

	def getInfo(self):
		return { 'name': self.name,'age': self.age,'breed': self.breed}

dog1 = Dog('Tom',2,'rotweiler')#we create an object by the name dog1...this is an instance of the class Dog

print(dog1.name)#would output tom
dog1.bark()#we use the method bark....and the output here is 'bark' as defined in the method bark in the class Dog
print(dog1.getInfo())#this returns a dictionary containing the information of dog1 as defined in the method getInfo 
#we use print because the method getInfo uses the return keyword

dog2 = Dog("Chuck",5,"chiuaua")#another instance(object) of the class Dog
#you can have as may objects as u want

dog2.bark()#would output 'bark'

#operator overloading...this is defining operators for custom classes that allow operators such as + and * to used on them
class vector:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __add__(self,other):#this method takes the value of first.x and adds it to second.x and then takes the value of second.y and adds it to the first.y and returns an object from the class vector
		return vector(self.x + other.x,self.y + other.y)

first = vector(5,7)
second = vector(3,9)
result = first + second#this returns an object with two values x and y
print(result.x)#outputs 8
print(result.y)#outputs 16
#the methods __init__ __add__ are called magic methods in python
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |
#python also provideds magic methods for comparisons
#an example is as shown below
__lt__ for <
__le__ for <=
__eq__ for  ==
__ne__ for !=
__gt__ for >
__ge__ for >=

#inheritance
#inheritance is the ability to define a new class that is modified version of an existing class
#look at the example below
class pet:
	def __init__(self,name,age):
		self.name = name 
		self.age = age

class cat(pet):#we add the class pet in parenthesis and cat inherits the init function from the class pet...hence we do not define the method init in cat
	def speak(self):
		print(f'i am {self.name} and am {self.age} years old')
		print('meow')

class cow(pet):
	def speak(self):
		print(f'i am {self.name} and am {self.age} years old')
		print('MOOO')

s = cat('Tim',12)
print(s)#would output i am Tim and am 12 years old meow

#if we wanted to add another attribute to the class cat....lets say a color
class cat(pet):
	def __init__(self,name,age,color):
		Super.__init__(name,age)
		self.color = color
	def speak(self):
		print(f'i am {self.name} and am {self.age} years old and am {self.color} in color')


s2 = cat('jon',12,'blue')
print(s2)

#this are just basic uses of inheritance...in more complex exercises one would see the importance of using classes and inheritance

#Class attributes are attributes in a class that are not defined inside a methdo
class new:
	person = 0
	def __init__(self,name):
		self.name = name
		person+=1

x = new('Mathius')
y = new('Henry')

print(new.person)#this will output 2 because the init method has been used twice by x and by y
#class methodes
#to use class methods we use the sign @...this is a class method decorator
#they are called by a class which is passed to the cls parameter of the mehod
class Rectangle:
	def __init__(self,width,height):
		self.width = width
		self.height = height
	def calculate_area(self):
		return self.width * self.height

	@classmethod
	def new_square(cls,side_length):
		return cls(side_length,side_length)#returns a class object with sidelength,sidelength as parameters

square = Rectangle.new_square(5)#note that the method is called by the class Rectangle
print(square.calculate_area())

 #static methods
 #they are similar to class methods, except they don't receive any additional arguments; they are like normal functions that belong to a class
class Calculator:
	@staticmethod
	def add(a,b):
		return a + b 

n1 = 1
n2 = 45
 print(Calculator.add(n1,n2))#displays 46



#this are just basic usage of classes and objects in python...once you start complex projects you get their importande



	
