# Find function -returns the index of where substring starts

# sentence = 'The quick brown fox jumped over the lazy dog.'

# query = sentence.find('quick')
# print(query)
#-----------------------------------------------------------

# Index function -if the substring is not found in the string-throws error

# sentence = 'The quick brown fox jumped over the lazy dog.'
# query = sentence.find('quick')
# query_two = sentence.index('quick')
# print(query)
# print(query_two)

# 4
# 4
#------------------------------------------------------------------

# sentence = 'The quick brown fox jumped over the lazy dog.'
# query = sentence.find('oops')
# query_two = sentence.index('oops')
# print(query)
# print(query_two)

# Traceback (most recent call last):
#   File "finding_substring_find_index_in.py", line 12, in <module>
#     query_two = sentence.index('oops')
# ValueError: substring not found

#----------------------------------------------------------------

# sentence = 'The quick brown fox jumped over the lazy dog.'
# query = sentence.find('oops')
# query_two = sentence.index('oops')
# print(query)
# print(query_two)

# Index-if the substring is not found in the string-throws error

# Traceback (most recent call last):
#   File "finding_substring_find_index_in.py", line 12, in <module>
#     query_two = sentence.index('oops')
# ValueError: substring not found

#----------------------------------------------------------------

# sentence = 'The quick brown fox jumped over the lazy dog.'
# query = sentence.find('oops')
# query_two = sentence.index('oops')
# print(query)
# print(query_two)

# -1

#-----------------------------------------------------------------

# In Operator Function - PREFERRED OPTION FOR PYTHON DEVS
# In Operation - only cares about true or false value, not index of character
# Best practice normally because not looking for index but true or false value

# sentence = 'The quick brown fox jumped over the lazy dog.'
# # query = sentence.find('oops')
# # query_two = sentence.index('oops')
# # print(query)
# # print(query_two)

# query = 'fox' in sentence

# print(query)

# True

 #--------------------------------------------------------------

sentence = 'The quick brown fox jumped over the lazy dog.'
# query = sentence.find('oops')
# query_two = sentence.index('oops')
# print(query)
# print(query_two)

query = 'oops' in sentence

print(query)

False

#---------------------------------------------------
# Cleanest way/best practice in writing an if conditional

# if 'oops' in sentence:
#     ...
#