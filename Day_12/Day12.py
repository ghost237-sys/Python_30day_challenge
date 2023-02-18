#Exception handling in python...the try statements
#they come in two...first one handles exceptions while the second one executes and finalizes code whether exceptions occur or not

#try/except/else
#am using an example to explain how it works
def bad(list,n):#a funtion that takes a list and an index and prints out the value at that index
	print(list[n])

try:
	bad([1,2,2],2)#we use 3 which will raise an IndexError but we avoid it using the try except 
except IndexError:
	print('The list is not that long')
finally:
	print('good for you')#this always prints 

#if a value like 2 was used instead of 3 the error would not occur
#the statements after the finally always run

#There is many errors that can occur.....TypeError,SyntaxError,AttributeError



