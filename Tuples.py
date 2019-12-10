# List:  []
# Dictionary:  {}
# Tuple:  ()

# Tuple: Immutable   Same as Strings being Immutable
# List:  Mutable

# post = ('Python Basics', 'Intro Guide to Python', 'Some Cool Python Content')

# title, sub_heading, content = post

# title = post[0]
# sub_heading = post[1]
# content = post[2]

# print(title)
# print(sub_heading)
# print(content)

# Python Basics
# Intro Guide to Python
# Some Cool Python Content


# post = ['Python Basics', 'Intro Guide to Python', 'Some Cool Python Content']

# post.sort()

# title, sub_heading, content = post

# print(title)
# print(sub_heading)
# print(content)

# Intro Guide to Python           Sorts alplabetically will mess things up with assignments 
# Python Basics                   to the variables if it is used as a list instead of a tuple
# Some Cool Python Content



post = ('Python Basics', 'Intro Guide to Python', 'Some Cool Python Content')

post.sort()

title, sub_heading, content = post

print(title)
print(sub_heading)
print(content)

# Traceback (most recent call last):
#   File "Tuples.py", line 40, in <module>
#     post.sort()
# AttributeError: 'tuple' object has no attribute 'sort'  CANNOT BE SORTED!