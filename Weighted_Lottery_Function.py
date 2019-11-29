# import numpy as np

# def weighted_lottery(weights):
#     container_list = []

#     for (name, weight) in weights.items():  # key=name, value=weight
#         # loop 1 time (winning)  loop 1000 (losing)
#         for _ in range(weight):
#             container_list.append(name)

#     return container_list

# # weights = {
# #         'winning': 1,
# #         'losing' : 1000
# #         }
# # weighted_lottery(weights)

# other_weights = {
#         'winning': 1,
#         'break_even': 2,
#         'losing' : 3
#         }

# print(weighted_lottery(other_weights))

# ['winning', 'break_even', 'break_even', 'losing', 'losing', 'losing']


import numpy as np

def weighted_lottery(weights):
    container_list = []

    for (name, weight) in weights.items():  # key=name, value=weight
        # loop 1 time (winning)  loop 1000 (losing)
        for _ in range(weight):
            container_list.append(name)

    return np.random.choice(container_list)

# weights = {
#         'winning': 1,
#         'losing' : 1000
#         }
# weighted_lottery(weights)

other_weights = {
        'winning': 1,
        'break_even': 2,
        'losing' : 3
        }

print(weighted_lottery(other_weights))

winning
losing
break_even
losing
break_even
losing
losing
losing

