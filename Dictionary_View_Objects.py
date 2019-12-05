players = {
    "ss" : "Correa", 
    "2b" : "Altuve",
    "3b" : "Bregman",
    "DH" : "Gattis",
    "OF" : "Springer",
}

# print(players.keys())

# print(players.values())

# print(players.items())
"""
dict_keys(['ss', '2b', '3b', 'DH', 'OF'])
dict_values(['Correa', 'Altuve', 'Bregman', 'Gattis', 'Springer'])
dict_items([('ss', 'Correa'), ('2b', 'Altuve'), ('3b', 'Bregman'), ('DH', 'Gattis'), ('OF', 'Springer')])
"""

"""
print(players.values()[1])

Traceback (most recent call last):
  File "Dictionary_View_Objects.py", line 21, in <module>
    print(players.values()[1])
TypeError: 'dict_values' object is not subscriptable
"""

# player_names = list(players.copy().values())
# print(players)

# {'ss': 'Correa', '2b': 'Altuve', '3b': 'Bregman', 'DH': 'Gattis', 'OF': 'Springer'}

teams = {
    "astros" : ["Altuve", "Correa", "Bregman"],
    "angels" : ["Trout", "Pujols"],
    "yankees" : ["Judge", "Stanton"],
    "red sox" : ["Price", "Betts"],
}

team_groupings = teams.items()

# print(team_groupings)

"""
dict_items([
    ('astros', ['Altuve', 'Correa', 'Bregman']),
    ('angels', ['Trout', 'Pujols']),
    ('yankees', ['Judge', 'Stanton']),
    ('red sox', ['Price', 'Betts'])
    ]),
    """

# print(len(team_groupings))

# 4

print(list(team_groupings)[0][1][0])

Altuve

"""
print(list(team_groupings)[2])
('yankees', ['Judge', 'Stanton'])

print(list(team_groupings)[2][1])
['Judge', 'Stanton']

print(list(team_groupings)[2][1][1])
Stanton

"""

