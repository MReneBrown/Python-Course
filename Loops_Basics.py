# Lists

# players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

# for player in players:
#     print(player)

# Altuve
# Bregman
# Correa
# Gattis


# Dictionary

players = {
    '2b': 'Altuve',
    '3b': 'Bregman',
    'ss': 'Correa',
    'dh': 'Gattis'
}

for position, player in players.items():
    print('Position', position)
    print('Player name', player)

Position 2b
Player name Altuve
Position 3b
Player name Bregman
Position ss
Player name Correa
Position dh
Player name Gattis 
