#A palindrome is a word that is spelled the same backward and forward, like “noon”
#and “redivider”. Recursively, a word is a palindrome if the first and last letters are the
#same and the middle is a palindrome

#Write code that prints True if a string is a palindrome
x = input("Enter a string: ")
print("Checking if its a palindrome.......")

y = x[::-1]
print(x==y)
