teams = {
    "astros": ["Altuve", "Correa", "Bregman"],
    "angels": ["Trout", "Pujols"],
    "yankees": ["Judge", "Stanton"],
    "red sox": ["Price", "Betts"]
}

# featured_team = teams['mets']
featured_team2 = teams.get("mets", "No featured team")
featured_team3 = teams.get("yankees", "No featured team")


# print(featured_team)
# Traceback (most recent call last):
#   File "get_function_dictionary.py", line 8, in <module>
#     featured_team = teams['mets']
# KeyError: 'mets'
print(featured_team2)
print(featured_team3)

No featured team
['Judge', 'Stanton']

