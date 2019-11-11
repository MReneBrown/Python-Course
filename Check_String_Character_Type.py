# api_data = '5'
# greeting = 'Hi'

# print(api_data.isalpha())
# print(greeting.isalpha())

# False
# True

# print(api_data.isnumeric())
# print(greeting.isnumeric())

# True
# False


api_data = '5'
greeting = 'Hi there' # space " " causes a false negative because it isn't alpha/numeric

print(greeting.isalpha())

False