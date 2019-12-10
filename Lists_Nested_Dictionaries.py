teams = [
    {
        'astros': {
            '2B': 'Altuve',
            'SS': 'Correa',
            '3B': 'Bregman',
        }
    },
    {
        'angels': {
        'OF': 'Trout',
        'DH': 'Pujols',
        }
    },
]

# print(teams)

# [{'astros': {'2B': 'Altuve', 'SS': 'Correa', '3B': 'Bregman'}}, {'angels': {'OF': 'Trout', 'DH': 'Pujols'}}]

# print(teams[0])

# {'astros': {'2B': 'Altuve', 'SS': 'Correa', '3B': 'Bregman'}}


angels = teams [1].get('angels', 'Team not found')

# print(angels)

# {'OF': 'Trout', 'DH': 'Pujols'}

# print(list(angels.values()))

# ['Trout', 'Pujols']

print(list(angels.values())[1])

Pujols
