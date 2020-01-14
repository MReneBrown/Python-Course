import fnmatch
from fnmatch import fnmatchcase
import os

players = [
    "Jose Altuve 2B",
    "Carlos Correa SS",
    "Alex Bregman 3B",
    "Scooter Gennett 2B"
]

second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]

print("players that play second base:", second_base_players)

players that play second base: ['Jose Altuve 2B', 'Scooter Gennett 2B']