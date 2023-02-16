#sets
#they are collections of unique data...elements of a set cannot be duplicate
#for example
student_id = {112,114,116,118,115}
print('Student Id', student_id)

#if we try to use duplicate values in sets...python removes one item from the duplicate ones
student_id2 = {112,114,116,118,115,115}
print(student_id2)

#adding itemsin a set using the add method
student_id2.add(235)
print(student_id2)

#the update method
#used to update the set with items of other collection types
companies = {'Lacoste','Ralph Lauren'}
tech_companies = ['apple','google','apple']
companies.update(tech_companies)
print(companies)#all unique elements of tech_companies are added to the set companies

#python set provides different built-in methods to perfom mathematical set operations like union,intersection,subtraction,and symetric difference
#the Union of Two Sets..the union of two sets A and B include all elements of set A and B
A = {1,3,5,4}
B = {0,2,4}
print(A | B)
print(A.union(B))



#set intersection
#this are common elements between A and B
print(A & B)
print(A.intersection(B))

#the difference o two sets
print(A-B)#elements in set A that are not in B
print(A.difference(B))


#Set Symmetric Difference...includes all elements in A and B without common elements
print(A^B)
print(A.symmetric_difference(B))


#There are other python set methods but we will not look at them hear




