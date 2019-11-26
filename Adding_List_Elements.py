tags = ['python', 'development', 'tutorials', 'code']

# Nope
# tags[-1] = 'Programming'
# ['python', 'development', 'tutorials', 'Programming']
# overwrites the last item in the list

# tags.extend('Programming')
# ['python', 'development', 'tutorials', 'code', 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
# extend takes each element within the string and treated it as its own character

# tags.extend(['Programming'])
# wrap the string in the list syntax, [], adds as one single element(word in this case)
# ['python', 'development', 'tutorials', 'code', 'Programming']

# new_tags = tags.extend(['Programming'])
# None 
# tags.extend() Does not return anything. Nothing is there to be stored in a variable

# tags.extend(['Programming'])

new_tags = tags + ['Programming']

print(tags)
print(new_tags)

['python', 'development', 'tutorials', 'code']
['python', 'development', 'tutorials', 'code', 'Programming']
