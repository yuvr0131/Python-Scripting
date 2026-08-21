# Lists
# LISTS- 
"""friends=["Kevin","Karen","Jim","Oscar","Toby"]
friends[1]="Mike"
print(friends[0][2])
print(friends[-3])
print(friends[1:])
print(friends[1:3])"""

#o/p
"""v
Jim
['Mike', 'Jim', 'Oscar', 'Toby']
['Mike', 'Jim']"""

#List Functions
lucky_numbers=[4,8,15,16,23,42]
friends=["Kevin","Karen","Jim","Oscar","Toby"]

"""# extend function
friends.extend(lucky_numbers)
print(friends)

#append function
friends.append("creed")
print(friends)

#insert
friends.insert(1,"kelly")
print(friends)


#remove
friends.remove("Jim")
print(friends)"""

#o/p
"""['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42]
['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42, 'creed']
['Kevin', 'kelly', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42, 'creed']
['Kevin', 'kelly', 'Karen', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42, 'creed']"""

"""#pop
friends.pop()
print(friends)

#o/p
['Kevin', 'Karen', 'Jim', 'Oscar']

#index
print(friends.index("Jim")) #o/p: 2"""


"""#sort
friends.sort()
print(friends) #o/p: ['Jim', 'Karen', 'Kevin', 'Oscar']"""

"""#reverse
friends.reverse()
print(friends) #o/p: ['Toby', 'Oscar', 'Jim', 'Karen', 'Kevin']"""

"""#copy
friends2=friends.copy()
print(friends2) #o/p:['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby']"""

