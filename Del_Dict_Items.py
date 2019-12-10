teams = {
    "astros" : ["Altuve", "Correa", "Bregman"],
    "angels" : ["Trout", "Pujols"],
    "yankees" : ["Judge", "Stanton"],
    "red sox" : ["Price", "Betts"],
}

# del teams['astros']
# as long as you know with 100% certainty that the key exists the del items is 
# fast and works great.

# print(teams)

# {'angels': ['Trout', 'Pujols'], 'yankees': ['Judge', 'Stanton'], 'red sox': ['Price', 'Betts']}

# print(teams['mets'])

# Traceback (most recent call last):
#   File "del_dict_items.py", line 14, in <module>
#     print(teams['mets'])
# KeyError: 'mets'

# print(teams.get('mets', 'No team found by that name'))

# No team found by that name


# teams.pop('astros', 'No team found by that name')

# print(teams)

# {'angels': ['Trout', 'Pujols'], 'yankees': ['Judge', 'Stanton'], 'red sox': ['Price', 'Betts']}


# remove_team = teams.pop('rays', 'No team found by that name')

# print(teams)
# print(remove_team)

"""
{
'astros': ['Altuve', 'Correa', 'Bregman'], 
'angels': ['Trout', 'Pujols'], 
'yankees': ['Judge', 'Stanton'], 
'red sox': ['Price', 'Betts']
}
No team found by that name
"""
remove_team = teams.pop('yankees', 'No team found by that name')

print(teams)
print(remove_team)

{'astros': ['Altuve', 'Correa', 'Bregman'], 'angels': ['Trout', 'Pujols'], 'red sox': ['Price', 'Betts']}
['Judge', 'Stanton']

# pop will remove the key but the value remains and will be printed out
# within a variable storing it the value of the key removed.

