"""
manual_exponent(2, 3)   2*2*2 or cubed
#> 8

manual_exponent(10,2)     10*10 or squared
#> 100
"""
from functools import reduce

# def manual_exponent(num, exp):
#     counter = exp - 1  # the first ((num)or 2) in ex. is the initial num. 
#     #If not subtracted it would be multiplied one too many times
#     total = num

#     while counter > 0:
#         total *= num
#         counter -= 1

#     return total

# print(manual_exponent(2, 3))
# print(manual_exponent(10, 2))
# print(manual_exponent(3, 3))
# print(manual_exponent(10, 5))

"""
2 ^ 3
2 x 2 x 2
"""

def manual_exponent(num, exp):
    computed_list = [num] * exp
    return (reduce(lambda total, element: total * element, computed_list))


print(manual_exponent(2, 3))
print(manual_exponent(10, 2))
print(manual_exponent(3, 3))
print(manual_exponent(10, 5))


# def some_func(total, element):
#     return total * element

# [2, 2, 2]

# some_func(2, 2)
# some_func(4, 4)


