#write a program that goes through a file and prints out a dictionary of all the words in the file and the largest word and the one most repeated
#we can use the os module to find the path of the file

#import os
#x = os.path.join('/home','allan','word.txt')#for your system use appropriate parameters

fhandle = open('word.txt')
dct = {}
for line in fhandle:
	line = line.strip()
	line = line.split()
	for word in line:
		dct[word] = dct.get(word,0) + 1

#to print the largest word
largest = 0

for k,v in dct.items():
	if len(k) > largest:
		largest = len(k)
		L_word = k
print(largest,L_word)

#the most repeated
count = 0
for k,v in dct.items():
	if v > count:
		count = v 
		w = k
print(w,count)

	 