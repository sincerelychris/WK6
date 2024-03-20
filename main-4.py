# collection is single "variable" used to store multiple values
# list is a collection of ordered and changeable values

# List  = [] ordered and changeable. Duplicates OK 


fruits = ["banana" , "apple" , "orange" , "grape" , "pear" , "blueberry"]

# computer counts from 0


print(fruits[2])
print(fruits[:2])
print(fruits[2:])
print(fruits[::2])
print(fruits[::-1])

#LIST METHODS

# append()	Adds an element at the end of the list
fruits.append("strawberry")
# SHOWS LENGTH OF LIST
print(len(fruits))
# ALLOWS YOU TO REPLACE A ELEMENT IN A LIST WITH SOMETHING ELSE
fruits[0] = "raspberry"
# ALLOW YOU TO CHOOSE WHERE TO INSERT
fruits.insert(0, "pineapple")
#removes
fruits.pop(0)
#abc order
fruits.sort()
# clear()	Removes all the elements from the list
fruits.clear()

print(fruits)