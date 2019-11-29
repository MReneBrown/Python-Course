players = {
    "ss" : "Correa",   # created a key item pair ss=key Correa=value
    "2b" : "Altuve",
    "3b" : "Bregman",
    "DH" : "Gattis",
    "OF" : "Springer"
}

second_base = players ['2b']
designated_hitter = players ['DH']

print(players)
print(second_base)
print(designated_hitter)

# {'ss': 'Correa', '2b': 'Altuve', '3b': 'Bregman', 'DH': 'Gattis', 'OF': 'Springer'}
# Altuve
# Gattis


# second_base = players ['asdf']

# Traceback (most recent call last):
#   File "python_dictionaries.py", line 10, in <module>
#     second_base = players ['asdf']
# KeyError: 'asdf'