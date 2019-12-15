num_list = range(1, 11)
cubed_nums = []

# for num in num_list:
#     cubed_nums.append(num ** 3)

# print(list(num_list))
# print(cubed_nums)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


# num_list = range(1, 11)

# cubed_nums = [num ** 3 for num in num_list]   # List comprehension

# print(list(num_list))
# print(cubed_nums)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


# num_list = range(1, 11)
# even_numbers = []

# for num in num_list:
#     if num % 2 == 0:
#         even_numbers.append(num)

# print(list(num_list))
# print(even_numbers)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [2, 4, 6, 8, 10]


num_list = range(1, 11)
# even_numbers = []

# for num in num_list:
#     if num % 2 == 0:
#         even_numbers.append(num)

even_numbers = [num for num in num_list if num % 2 == 0]

print(list(num_list))
print(even_numbers)

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[2, 4, 6, 8, 10]



