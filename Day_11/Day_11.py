#Handling files
#Reading and writing files
#the built in function open takes the name of the file as a parameter and returns a fiel object you can use to read the file
#reading files
#fhandle = open('words.txt')#this file only contains words
#we can iterate througn it and print each word 
for line in fhandle:
	word = line.strip()
	print(word)

fhandle2  = open('file.txt')
files with lines in them
for line in fhandle:
	print(line)#prints all the lines in the fiel file.txt

#if we wanted to write into a file 
fhandle3 = open('file.txt','w')
line = 'i wrote this line'

fhandle3.write(line)
#this would write into the file

#for read mode we leave it without any characters afterwards or add 'r'
#for the append mode use 'a' at the end

#while working with files knowing the path of the file is essential
#the examples above would work because the file is in the same folder with the python file
#to work with files in other folders we use the os module....this helps because for windows we use backslashes..for unix and linux

import os
x = os.path.join('/home', 'Allan','Desktop','file.txt')#for your machine use appropriate parameters
fhandle4 = open(x)
for line in fhandle4:
	print(line)


#You can do so much more with the os module...check it out in the official python documentation page







