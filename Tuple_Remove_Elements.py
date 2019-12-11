post = ('Python Basics', 'Intro Guide to Python', 'Some Cool Python Content', 'Published')

# Removing elements from end of tuple

# post = post[:-1]

# print(post)

# ('Python Basics', 'Intro Guide to Python', 'Some Cool Python Content')

# post = post[:-2]

# print(post)

# ('Python Basics', 'Intro Guide to Python')


# Removing elements from beginning of tuple

# post = post[1:]

# print(post)

# ('Intro Guide to Python', 'Some Cool Python Content', 'Published')

# Removing specific element (messy/not recommended)

post = list(post)
# ['Python Basics', 'Intro Guide to Python', 'Some Cool Python Content', 'Published']
post.remove('Published')
# ['Python Basics', 'Intro Guide to Python', 'Some Cool Python Content'] LIST []
post = tuple(post)
# ('Python Basics', 'Intro Guide to Python', 'Some Cool Python Content') TUPLE ()
print(post)


