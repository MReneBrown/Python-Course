tags = ['drum', 'flute', 'guitar', 'xylophone', 'saxophone', 'clarinet', 'trumpet', 'trombone', 'french horn', 'tuba']

tag_range = tags[4:]
print(tag_range)

tag_range = tags[:2]
print(tag_range)

tag_range = tags [2:3]
print(tag_range)

number_of_tags = len(tags)
print(number_of_tags)

tags.sort()

print(tags)

tags.sort(reverse=True)

print(tags)

totals = [2548, 5, 64891, 94, 0, 595158, 54, 2, 8535481567]

print(totals)

totals.sort()

print(totals)

totals.sort(reverse=True)

print(totals)

last_item = tags[-1]

print(last_item)

first_item = tags[0]

print(first_item)

fifth_item = tags[4]

print(fifth_item)


['saxophone', 'clarinet', 'trumpet', 'trombone', 'french horn', 'tuba']
['drum', 'flute']
['guitar']
10
['clarinet', 'drum', 'flute', 'french horn', 'guitar', 'saxophone', 'trombone', 'trumpet', 'tuba', 'xylophone']
['xylophone', 'tuba', 'trumpet', 'trombone', 'saxophone', 'guitar', 'french horn', 'flute', 'drum', 'clarinet']
[2548, 5, 64891, 94, 0, 595158, 54, 2, 8535481567]
[0, 2, 5, 54, 94, 2548, 64891, 595158, 8535481567]
[8535481567, 595158, 64891, 2548, 94, 54, 5, 2, 0]
clarinet
xylophone
saxophone
