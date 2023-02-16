#Dictionaries
#they are almost similar to list but their indexes can be of other types not just integers
#indexes for dictionaries are known as keys
#a key with its associated value is called a key-value pair
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
#you can access the values using their keys
print(myCat['size'])#will output fat
#the order of items in a dictionary does not matter when compairing if two dictionaries are equal
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs==ham)#prints out true


#an example of the capabilities of a dictionary is below
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}#first we create a dictionary
while True:
	print('Enter a name: (blank to quit)')
	name = input()
	if name == '':#if one types nothing the loop breaks
		break
	if name in birthdays:#checks whether users input name is in the dictionary
		print(birthdays[name] + ' is the birthday of ' + name)#retreives the value of the name used as a key 
	else:#an alternative if the name is not a key in the dictionaary birthdays
		print('I do not have birthday information for ' + name)
		print('What is their birthday?')
	bday = input()#prompts for users input for birthdate
	birthdays[name] = bday#adds the birthdate to the birthdays dictionary using the name that was not found earlier as a key
	print('Birthday database updated.')


#the keys(),values(), and items() Methods....return list like values
#The values returned by these methods are not true lists:
# They cannot be modified and do not have an append() method. 
#But these data types (dict_keys, dict_values, and dict_items, respectively) can be used in for loops
new = {'color': 'red', 'age': 42}
for v in new.values():
	print(v)#prints out the values in the dictionary wihout their keys...going donwards one by one

for k in new.keys():
	print(k)#prints out keys in the dict going downwards one by one


for i in new.items():
	print(i)#prints out the key-value pairs in tuples going downwards

#you can also use the multiple assignment trick in for loops
for k,v in new.items():
	print("keys:" + k + "value:" + v)#a sample output is...keys: color value:red

#the get method in dictionaries
#the  get() method  in dictionaries takes two arguments: the key of the value to retrieve and a fallback value to return if
#that key does not exist
picnicItems = {'apples': 5, 'cups': 2}
#the picnicItems.get('cups',0)...returns the integer o if 'cups' is not in the dictionary and if its there it returns its value
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')#we use the str to change the value to a string for concatination
#output....I am bringing 2 cups...


#the setdefault method
x = picnicItems.setdefault('bananas' , 4)
#if bananas is not in the dictionary its added and assigned the value 4...if present nothing changes
print(picnicItems)#you will notice that 'bananas':4 was added



