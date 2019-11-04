sentence = 'The quick brown fox jumped over the lazy dog'

print(sentence) Runs just fine
# ------------------------------------------------------
sentence= "The quick brown fox jumped over the lazy dog"

print(sentence_two  Runs just fine
# ------------------------------------------------------

sentence = "The quick brown fox jumped over the lazy dog'

print(sentence)

#  ERROR
#  File "String_Basics.py", line 9
#     sentence = "The quick brown fox jumped over the lazy dog'
#                                                             ^
# SyntaxError: EOL while scanning string literal


# Double and single quotes are going to be treated the same in Python
# ---------------------------------------------------------
sentence = 'The quick brown fox jumped over the lazy dog'

print(sentence)


sentence_two = 'That is my dog's bowl'
print(sentence_two)

#    File "String_Basics.py", line 24
#     sentence = 'That is my dog's bowl'
#                                ^
# SyntaxError: invalid syntax
# If you include a backslash prior to the single quote such as
#  dog\'s it will include the next character (') as a string
# (escape values) rather than the ending of that string.

sentence_three = "That is my dog's bowl"

sentence_four = "Tiffany said, \"That is my dog's bowl\""

print(sentence_four)

