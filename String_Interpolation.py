# name = 'Kristine'
# greeting = f'Hi {name}'
# print (greeting)

# Hi Kristine

# name = 'Kristine'
# greeting = f'Hi {2 + 2}'
# print(greeting)

# Hi 4

# name = 'Kristine'
# greeting = f'This is my {bracket} blog post'
# print(greeting)

# Traceback (most recent call last):
#   File "string_interpolation.py", line 14, in <module>
#     greeting = f'This is my {bracket} blog post'
# NameError: name 'bracket' is not defined

# name = 'Kristine'
# greeting = f'This is my \{bracket\} blog post'
# print(greeting)

#  File "string_interpolation.py", line 23
#     greeting = f'This is my \{bracket\} blog post'
#                ^
# SyntaxError: f-string expression part cannot include a backslash

# name = 'Kristine'
# greeting = f'This is my {{bracket}} blog post'
# print(greeting)

# This is my {bracket} blog post

name = 'Kristine'
product = 'Python elearning course'

email_content = f"""
Hi {name}

Thank you for purchasing {product}

Regards,

Sales Team
"""
print(email_content)


Hi Kristine

Thank you for purchasing Python elearning course

Regards,

Sales Team
