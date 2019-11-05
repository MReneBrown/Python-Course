# The quick brown fox jumped
# T -> mapped to 0 in the zero base numbering system
# h -> 1
# e -> 2
# ' ' -> 3


# starter_sentence = 'The quick brown fox jumped'
# starter_sentence[3] = 'A'
# print(starter_sentence)

# Traceback (most recent call last):
#   File "access_portions_strings.py", line 9, in <module>
#     starter_sentence[3] = 'A'
# TypeError: 'str' object does not support item assignment
# Immutable- meaning you cannnot change the value of the 
# string by assigning a new value. Once a string is assigned
# a value, that is what it is.  Value of [3] is ' '.


# starter_sentence = 'The quick brown fox jumped'
# first = starter_sentence[0]   # range
# second = starter_sentence[1]  # range
# third = starter_sentence[2]   # range bad way of doing changing a sentence
# new_sentence = first + second + third
# print(new_sentence)

# starter_sentence = 'The quick brown fox jumped'
# first_word = starter_sentence[0:3]
# new_sentence = first_word
# print(new_sentence)  # When ran in terminal prints out The

starter_sentence = 'The quick brown fox jumped'

new_sentence = 'Thy' + starter_sentence[3:] 
# leave the range value after colon blank, it will go to end of string
# no value needed if you want the rest of the string assigned
print(new_sentence) 

