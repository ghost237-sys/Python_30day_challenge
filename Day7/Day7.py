#lists
#Enclosed in square brackets...can contain any data type including other lists
x = [1,2,3,'hallo','home',['a',6]]

#list slicing
#getting items from a list using indexing...index start from 0 
print(x[3])#prints the item in index 3
print(x[:2])#from the start to index  2 but not including item in index 2
print(x[::-1])#prints the list in reverse
x[3] = 'new'#changes the item in index 3
print(x)
#list concatenation....adding two lists
y =['lists','A',"B"]
print(x + y)

#using lists with while loops
#the following code demonstrates how powerful strings are
catNames = []#we first create an empty list
while True:#start a while loop that without a break would run forever causing an error
	#the len inbuilt function is used to count the length of the list so as to know the cat number...the first time its length is zero so we add one to get cat number 1
	print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
	name = input()#takes users input name and if empty the whileloop break
	if name == '':
		break
	#adds the name into the empty list 
	catNames = catNames + [name] # the brackets on the name are used to make the name a list for concatination
	#we could also use methods to add the name...
print('The cat names are:')

#for loops in lists
#this is just a simple example u can write much better code with for loops 
for name in catNames:
	print(' ' + name)

#The in and not in Operators
for item in x:#iterates through list
	if item not in "hallo":#if hallo is not in the list we add it
		#append method to add items at the end of the list
		x.append(item)#append is an example of a method used in lists

#the multiple assignment trick
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
#items in cat have been replaced after this
#i should note that the items of variables must be exactly equal as the length of cat
#methods
#index method return the index of item in a list
print(cat.index('color'))#would return 1

#insert
#just like append method but takes two arguments..the position index to insert an item
print(cat.insert(1,'home'))#would add home to the first index without replcing any item in the list


#remove
#removing items using this method...removing items that do not exist returns an error
print(cat.remove('home'))#would remove home from cat


#sort
#sorting a list using this method
#you cannot sort items of different data types....a list with integers and strings cannot be sorted using this method
s = cat.sort()
print(s)#would print a sorted list

#other methods on strings....