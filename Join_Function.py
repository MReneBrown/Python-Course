#  https://www.google.com/search?q=python+development+tutorial

uri = 'https://www.google.com/search?q='
tags = ['python', 'development', 'tutorial']
formatted_tags = '+'.join(tags)
formatted_tags2 = '-'.join(tags)
formatted_tags3 = '***'.join(tags)
query_uri = f' {uri}{formatted_tags}'
query_uri2 = f' {uri}{formatted_tags2}'
query_uri3 = f' {uri}{formatted_tags3}'


print(formatted_tags)
print(formatted_tags2)
print(formatted_tags3)
print(query_uri)
print(query_uri2)
print(query_uri3)


python+development+tutorial
python-development-tutorial
python***development***tutorial
https://www.google.com/search?q=python+development+tutorial
https://www.google.com/search?q=python-development-tutorial
https://www.google.com/search?q=python***development***tutorial