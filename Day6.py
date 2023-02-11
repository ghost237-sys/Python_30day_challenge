#functions
#functions without parameter
def hello():
	print('Howdy!')
	print('Howdy!!!')
	print('Hello there.')

hello()


#functions with parameter
def hello(name):
	print('Hello ' + name)

hello('John')


#return value
def sum(x,y):
	s = x + y
	return s#anything beyond the return statement is not executed
	print('hello')
#to print out the answer you must use print
print(sum(1,4))


#local and global variabels in functions
#any variable declarations outside a function are global and can be used anywhere in the code\
five = 5
def add_5(x):
	print(x + five)
add_5(4)

#any variable defined within a function cannot be used outside the function
def add_6(n): 
	six = 6
	print(n + six)

add_6()
#print(six) #this will cause an error(name six not defined) because the variable six is local to the add_6 function
