#Classes and Objects
#we cant complete the whole topic in one day this is just a brief intro
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

#below are some topics that i will look at tommorow
#Operator Overloding
#you can sspecify the behavior of operators on your defined types
#for example the __add__ method to use + to add objects
#polymorphisim
#Functions that work with several types are called polymorphic
#inheritance
#inheritance is the ability to define a new class that is modified version of an existing class
