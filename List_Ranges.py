tags = ['python', 'development', 'tutorials', 'code']

tag_range = tags[1:2]
# 1 is index of what will be printed, 2 is where the output will stop (before 2)

print(tag_range)

tag_range = tags[1:3]
# 1 index of what will be printed, 3 is where outut will stop (before 3)

print(tag_range)

tag_range = tags[1:]
# nothing put after the colon(:) will print to the end of the list/range

print(tag_range)

tag_range = tags[:2]
# nothing before the colon(:) will start at beginning of the list/range

print(tag_range)


tag_range = tags[:-1]
# prints from first of list/range and includes everything but the last element

print(tag_range)

tag_range = tags[:]
# prints all of the list/range-just for learning purposes- pointless for coding

print(tag_range)


['development']
['development', 'tutorials']
['development', 'tutorials', 'code']
['python', 'development']
['python', 'development', 'tutorials']
['python', 'development', 'tutorials', 'code']