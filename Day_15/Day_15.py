#Regular expressions
#in python they can be accessed using the re module...and is accessed as follows
import re

#to avoid confusion while working with regular expressions,we could use raw strings as r'expression'

#re.match
#After you define a regular expression the re.match function can be used to determine whether it matches at the beginning of a string
#if it does,match returns an object representing the match if not it returns None
#here is an example
pattern = r'spam'

x = re.match(pattern,'spamsausagespam')
print(x)#returns an object...<re.Match object; span=(0, 4), match='spam'>
#the objects have several methods such as group...returns string matched,start...returns the starting position of the match,end...returns the ending positon
print(x.group())#returns the string matched

#re.search
#finds a match of a pattern anywhere in the string
y = re.search(pattern,'eggspamsausagespam')
print(y.group())#returns the string matched

#re.findall...returns a list of all substrings that match a patter
z = re.findall(pattern,'eggspamsausagespam')
print(z)#displays...['spam', 'spam']

#re.sub--replaces all occurences of the pattern in string with repl, substituting all occurences,unless count is provided....it returns the modified string
#syntax
#re.sub(pattern,repl,string,count=0)
#example
st = 'My name is David. Hi David.'
pattern = r"David"
newst = re.sub(pattern,'Amy',st)
print(newst)#...displays My name is Amy. Hi Amy.

#metacharacters..they allow you to create regular expressions to represent concepts like "one or more repetition of a vowel"
#dot(.)
#this matches any character other than a new line
pattern = r'gr.y'
if re.match(pattern,'grey'):
	print('match1')#displays match1
if re.match(pattern,'blue'):
	print('match')#this returns nothing

#^ and $ for the start and end of a string respectively
pattern = r'^gr.y$'

if re.match(pattern,'grey'):
	print('match2')#displays match
if re.match (pattern,'stingray'):
	print('match')#does not display anything because the start doesn't match

#Character Classes...they provide a way to match only one of a specific set of characters...we put the characters it matches inside square brackets
pattern = r'[aeiou]'

if re.search(pattern,'grey'):
	print('match3')#displays match3
if re.search(pattern,'rhythm myths'):
	print('match4')#displays nothing because the string being matched does not containing any of the letters in pattern

#character classes can also match ranges of charaters
#the class [a-z] matches any lowercase alphebetic...and [0-9] matches any digit
#multiple ranges can be included in one class...[A-Za-z] matches a letter of any case
pattern = r'[A-Z][A-Z][0-9]'
if re.search(pattern,"LS8"):
	print('match5')#dispays match5
if re.search(pattern,'1ab'):
	print('match')#does not display anything

#when you place ^ at the start of a charcter class to invert it
pattern = r'[^A-Z]'
if re.search(pattern, 'this is all quiet'):
	print('match6')
if re.search(pattern, 'THSIALLSHOUTING'):
	print('match')#does not display anything

#(*)
#this * means zero or more repetions of the previous thing
pattern = r'egg(spam)*'#this matches strings that start with egg and follow with zero or more spams

if re.match(pattern,'egg'):
	print("match7")#displays match7
if re.match(pattern,'spam'):
	print("match")#does not display anything

#(+)
#means one or more repetitions
pattern = r'g+'
if re.match(pattern,"g"):
	print('match8')#displays match8
if re.match(pattern,'abd'):
	print('match')#displays nothing
# (?)
#means zero or one repetitions
pattern = r"ice(-)?cream"

if re.match(pattern,'ice-cream'):
	print('match9')#displays
if re.match(pattern,'icecream'):
	print('match10')#displays
if re.match(pattern,'ice--cream'):
	print('match')#does not display
#({})
#curly braces can be used to represent the number of repetitions between two numbers
#the regular expression {x,y} means between x and y repetions of something
#{0,1} is the same as ?
pattern  = r'9{1,3}$'#matches strings that have 1 to 3 nines
if re.match(pattern,'9'):
	print('match11')#displays
if re.match(pattern,'9999'):
	print('match')#does not display

#groups
# a group can be created by surrounding part of a regular expression with paranthesis
pattern = r'egg(spam)*'

if re.match(pattern,'egg'):
	print("match12")#displays match12
if re.match(pattern,'spam'):
	print("match")#does not display

#the content of groups in a match can be accessed using the group function
#group(0) returns the whole match...and group(n) where n is greater than 0 returns the nth group from the left
pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern, 'abcdefghijklmnop')
if match:
	print(match.group())#displays abcdefghi
	print(match.group(0))#displays abcdefghi
	print(match.group(2))#displays de


#There are several kind of special groups...two useful ones are name groups and non-capturing groups
#named groups have the format(?P<name>...) where name is the name of the group and ... the content
#they are same as normal groups but can be accesed by group(name)
#non capturing groups have the format(?...) they are not accessible by the group method so they can be added to an existing regular expressinon without breaking the numbering

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern,'abcdefghi')
if match:
	print(match.group("first"))#displays abc
	print(match.groups())#displays ('abc','ghi')

#(|)means or ....red|blue means red or blue

#special sequences...they are written as a backslash followed by another character
#example..a backslash and a number between 1 and 99 e.g \1 or \17 matches the expression of the group of that number

# \d for digits.....\D anything that is not  a digit
# \s for whitespace  \S anything that is not a whitespace
# \w word characters \W anything that is  not a word character

pattern = r'(\D+\d)'#matches one or more non digits followed by a digit
match = re.match(pattern,"Hi 999!")
if match:
	print('Match')#displays
#i think there are more special sequences...you can search on google






