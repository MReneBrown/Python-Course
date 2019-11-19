# from functools import reduce

# numbers = [ 1, 2, 3, 4, 5 ]

# def my_sum(a, b):
#     return a + b

# result = reduce(my_sum, numbers)

# print(result)    15

# from functools import reduce
# numbers = [ 5, 6, 7, 8 ]

# def the_sum(a,  b):
#     return a + b

# result = reduce(the_sum, numbers)

# print(result)     26


# Initial Value (55)
# from functools import reduce
# numbers = [8, 9, 10, 11]

# def my_sum(a, b):
#     return a + b

# result = reduce(my_sum, numbers, 55) # initial value 55 plus first list item 8, etc.

# print(result)   93


# from functools import reduce
# numbers = [ 1, 2, 3, 4 ]

# def my_sum(a, b):
#     return a + b

# result = reduce(my_sum, numbers, 45)

# print(result)     55




# from functools import reduce
# from operator import add

# numbers = [ 1, 2, 3, 4, 5 ]

# result = reduce(add, numbers)

# print(result)   15


# from functools import reduce

# numbers = [ 1, 2, 3, 4, 5 ]

# result = reduce(lambda x,y: x+y, numbers)

# print(result)     15


# from functools import reduce

# numbers = [ 14, 34, 24, 22, 44 ]

# result = reduce(lambda x,y: x+y, numbers)

# print(result)    138


from functools import reduce
from operator import add

srtList=['I ', 'Love ', 'poftut.com']

result = reduce(lambda x,y: x+y, srtList)

print(result)

