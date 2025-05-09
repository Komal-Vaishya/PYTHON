#Deleting a elements from the list
my_dict = {'a': 1, 'b': 2, 'c': 3}
del my_dict['a']
print(my_dict)  # {'a': 1, 'c': 3}



# Assigning string to a variable
a = 'This is a string'
print (a)
b = "This is a string"
print (b)
c= '''This is a string'''
print (c)


# Declaring a list
L = [1, "a" , "string" , 1+2]
print (L)
#Adding an element in the list
L.append(6) 
print (L)
#Deleting last element from a list
L.pop()
print (L)
#Displaying Second element of the list
print (L[1])




tup = (1, "a", "string", 1+2)
print(tup)
print(tup[1])



d = {1: 'Lorem', 2: 'Ipsum', 3: 'Dolerum'}
print(d)



# create dictionary using { }
d1 = {1: 'Game', 2: 'of', 3: 'Thrones'}
print(d1)

# create dictionary using dict() constructor
d2 = dict(a = "House", b = "of", c = "Cards")
print(d2)



d = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))



d = {1: 'Game', 2: 'of', 3: 'Thrones'}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d[1] = "Python dict"

print(d)