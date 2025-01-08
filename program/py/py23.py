#Write a program to demonstrate basic 
#comprehensions on list, set and dictionary.

#List comprehension
#list are mutable and ordered collection of items.
#List comprehension is an elegant way to define and create list in python.
a=[x for x in range(10)]
print(a)

#Set comprehension
#set is an unordered collection of unique items.
#Set comprehension is an elegant way to define and create set in python.
b={x for x in range(10)}
print(b)

#Dictionary comprehension
#Dictionary is an unordered collection of key-value pairs.
#Dictionary comprehension is an elegant way to define and create dictionary in python.
c={x:x*x for x in range(10)}
print(c)