# usernames = [
#     'jon',
#     'tyrion',
#     'theon',
#     'cersei',
#     'sansa',
# ]

# for username in usernames:
#     if username == 'cersei':
#         print(f'Sorry, {username}, you are not allowed')
#         continue
#     else:
#         print(f'{username} is allowed')


usernames = [
    'jon',
    'tyrion',
    'theon',
    'cersei',
    'sansa',
]

for username in usernames:
    if username == 'cersei':
        print(f'{username} was found at index {usernames.index(username)}')
        break
    print(username)

jon
tyrion
theon
cersei was found at index 3






