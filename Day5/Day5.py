
#loops (for/while)
#used to iterate over items

#for loops in strings
x = 'Hallo'
for i in x:#any word can be used in place of i
	print(i)#this will output the letters one by one downwords

#in integers using range
for k in range(10):
	print(k)

#nested for loops are mostly common with other data types....we will look at them later
#for loops can also be used in lists,dictionaries,sets and touples but i decided not to include that in this part
#that ill look at when am looking at the specific data types

#while loops
#code in a while  loop body will be executed as long as the while state-
#ment’s condition is True
y = 0
while y < 5:
	print('Hello, world.')
	y = y + 1
#Break statement
#the loop breaks at this point
print('while loop 2')
z = 0
while z < 5:
	print('Hello, world.')
	if z == 3:
		break
	z = z + 1

#This is just a basic introduction to for loops and while loops....we will get a deeper look at them as we go on learning
