"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""
import math

sales_prices = [
    100, 
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3
]

# sales_prices.sort()
# print(sales_prices)
# [1, 3, 10, 40, 83, 100, 100, 220, 400]

# elements = len(sales_prices)
# print(elements)
# 9

# fifth_item = sales_prices[4]
# print(fifth_item)
# 83
# -------------------------------------------
# sorted_list = sorted(sales_prices)
# num_of_sales = len(sorted_list)
# first_sales_items = sorted_list[:math.floor(num_of_sales/2)]
# last_sales_items = sorted_list[-(math.floor(num_of_sales/2)):]
# median = sorted_list[math.floor(num_of_sales/2):(math.floor(num_of_sales/2)+1)]

# print(sorted_list)
# print(num_of_sales)
# print(first_sales_items)
# print(last_sales_items)
# print(median)

# [1, 3, 10, 40, 83, 100, 100, 220, 400]
# 9
# [1, 3, 10, 40]
# [100, 100, 220, 400]
# [83]


sorted_list = sorted(sales_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)

first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice + 1)]
print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)

[1, 3, 10, 40, 83, 100, 100, 220, 400]
9
[1, 3, 10, 40]
[100, 100, 220, 400]
[83]





