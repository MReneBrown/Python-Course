# name = 'Kristine'
# age = 12
# product = 'Python eLearning course'

# greeting = "Hi {0}', you are listed as {1} years old and you have purchased: {2}...".format(name, age, product)

# print(greeting)

# Hi Kristine', you are listed as 12 years old and you have purchased: Python eLearning course...


# name = 'Kristine'
# age = 12
# product = 'Python eLearning course'

# greeting = "Product Purchase: {2} - Hi {0}, you are listed as {1} years old.".format(name, age, product)

# print(greeting)

# Product Purchase: Python eLearning course - Hi Kristine, you are listed as 12 years old.


# name = 'Kristine'
# age = 12
# product = 'Python eLearning course'

# greeting = "Product Purchase: {2} - Hi {0}, you are listed as {1} years old. - {3}".format(name, age, product, 'Jordan')

# print(greeting)

# Product Purchase: Python eLearning course - Hi Kristine, you are listed as 12 years old. - Jordan


name = 'Kristine'
age = 12
product = 'Python eLearning course'
from_account = 'Jordan'

greeting = f"Product Purchase: {product} - Hi {name}, you are listed as {age} years old. - {from_account}"
print(greeting)

Product Purchase: Python eLearning course - Hi Kristine, you are listed as 12 years old. - Jordan