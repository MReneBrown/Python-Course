# def greeting(name):
#     print(f'Hi {name}!')

# greeting()
# greeting('Kristine')

# Traceback (most recent call last):
#   File "Function_Default_Args.py", line 4, in <module>
#     greeting()
# TypeError: greeting() missing 1 required positional argument: 'name'

# -------------------------------------

# def greeting(name = 'Guest'):
#     print(f'Hi {name}!')

# greeting()
# greeting('Kristine')

# Hi Guest!
# Hi Kristine!

# -------------------------------------

def some_function(collection = []): # NEVER set default argument as a list!!!!
    collection.append(1)
    print(id(collection)) # Prints where in memory this is saved
    return collection

print(some_function())

# 2650556862784
# [1]

# Other part of progream
print(some_function()) 

2650556862784
[1, 1]
# each additional time called w/in program it 
# will add to previous appended number
# BAD PRACTICE!


















