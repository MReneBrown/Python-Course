users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

ids = [1, 2, 3, 4]

mixed_list = [42, 10.3, 'Altuve', ['Kristine', 'Tiffany', 'Jordan', 'Leann']]

mixed_list2 = [42, 10.3, 'Altuve', users]

print(users)
print(mixed_list)
print(mixed_list2)

user_list = mixed_list.pop()
user_list = mixed_list2.pop()

print(user_list)
print(mixed_list)
print(mixed_list2)


nested_lists = [[123], [234], [345]]

print(nested_lists)
