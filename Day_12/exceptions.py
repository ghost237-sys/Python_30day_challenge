#a simple program with a try except 
try:
	age = int(input("please Enter your age:"))
except ValueError:
	print("please Enter a number")
finally:
	print('Thank YOu')

print(f'You are {age} years old')