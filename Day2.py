#strings
#a string is anything enclosed in double quotes
#the words greeting and shirt_number are variable names
greeting = "Hallo"
shirt_number = "23"

#String slices
#the one here is an index......strings are indexed starting from 0
print(greeting[1:])#will output allo

#String concantation
print(greeting + shirt_number + "?")#will output "Hallo 23 ?"
print(f"{greeting} {shirt_number} {'?'}")#same output as the above statement

#integers
#this are whole numbers
x = 1
y = 2

#floating point
#they are numbers that contain fraction parts
r = 2.5
t = 7.9

#Boolean
#logical values i.e True,False
print(x == y)#this will output False because x is not equal to y
#otherwise it would output True

#Other data types like lists,Tuples,Dictionary and sets will talk more about them later
