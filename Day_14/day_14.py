#user defined modules
#pre defined modules in python are like math...to access them we use the keyword import
import math
print(math.sqrt(16))#this will output 4
#now for user defined modules are simply other files you write that contain a piece of code you want to use without redudancy


#we create a new python file  where we will be importing a function in....... the same folder
#a simple example is as below
from new import * #the symbol * is used to import everything inside the new
print(add(2,3))
print(sub(16,2))

#when the files are in different folders we import as follows
from other import second
second.myfunc()#prints hello world

#you could also use
from other.second import *
myfunc()


#if the folder other has more than one one file we would have to create a __init__.py file inside it in order to use the notation below
#we the line __all__=['second','third'] in the __init__ file...the list contains all the files in the folder we are importing from
from other import *
third.thirdfunc()#this displays this is the third file


#incase we have a subfolder....we do it as follows
from other.subother import fourth
fourth.lst_func()

#we could also do it like this
from other.subother.fourth import *
lst_func()


#note that the __pycache__ folder is created by python automatically...i think in all ides
#thats simply how you import your own modules
#this is just a simple guide through...it is helpful when working with big chunks of code