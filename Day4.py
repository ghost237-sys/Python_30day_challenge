#Control flow using if/elif/else
#if statements are used to run code if a certain condition holds
if 10 > 5:
	print("10 greater than 5")

#nested if statements
#if statements inside other if statements...if the first condition is False the second if statement wont run
num = 12
if num > 5:
	print("Bigger than 5")
	if num <= 47:
		print("Between 5 and 47")

#else statements
#runs if the if statement is False
if num == 120:
	print("num is equal to 120")
else:
	print("Not equal to  120")
#else can also be used inside nested if statements
if num != 10:
	print("num is not 10")
	if num == 20:
		print("num is equal to 20")
	else:
		print('Num is not equal to 20')
		
#elif statements
#used to check many conditions.....used because if else statements get to long thus elif(else if)
if num > 5 :
	print("Bigger than 5")
elif num < 6:#statement is false so this print wont run
	print("Smaller  than 6")
elif num > 40:
	print("Bigger than 40")
