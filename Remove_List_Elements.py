users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

print(users)

users.remove('Jordan')
# if you know the value in a list-this is the way to go. Searches  
# entire collection and removes the element with that value

print(users)

popped_user = users.pop()   
# removes the last element in list-returns element to be used
# popping the last element out of list/grabbing it to use it

print(popped_user)
print(users)

del users[0]
# when you know the list and the index value in 
# the list and you want that element deleted

print(users)


# ['Kristine', 'Tiffany', 'Jordan', 'Leann']
# ['Kristine', 'Tiffany', 'Leann']
# Leann
# ['Kristine', 'Tiffany']
# ['Tiffany']