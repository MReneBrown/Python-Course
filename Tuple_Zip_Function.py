positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

# scoreboard = zip(positions, players)

# print(list(scoreboard))

# [('2b', 'Altuve'), ('3b', 'Bregman'), ('ss', 'Correa'), ('dh', 'Gattis')]

scoreboard = zip(players, positions)

# print(list(scoreboard))

# [('Altuve', '2b'), ('Bregman', '3b'), ('Correa', 'ss'), ('Gattis', 'dh')]

print(list(scoreboard)[-1])

('Gattis', 'dh')
