# strip pulls all empty/white spaces out of string on run

# url = '    https://google.com            '

# print(url)

#     https://google.com     
# has the spaces that were coded into the string


# url = '    https://google.com            '

# print(url.strip())

# https://google.com




# lstrip starts at left side of string and finds what 
# has been identified and strips it out on run

# url = 'https://google.com'

# print(url.strip('https://'))  

# google.com


# url = 'https://google.com'

# # print(url.strip('https://'))  

# print(url.lstrip('https://')) 

# google.com




# rstrip starts at right side of string and finds what 
# has been identified and strips it out on run

url = 'https://google.com'

# print(url.strip('https://'))  

url = url.lstrip('https://')
url = url.rstrip('.com')
url = url.capitalize()

print(url) 

Google


