# Booleans
# Numbers
# Strings
# Bytes and byte arrays
# None
# Lists
# Tuples
# Sets
# Dictionaries


meal_completed = True
sub_total = 100
tip = sub_total * 0.2   # can use 1/5 instead of 0.2 and it will produce same answer.
total = sub_total + tip
receipt = "Your total is " + str(total)  
#total has to be a string to be added to the string printed out. Cannot be "+ total"
#will throw an error
print(receipt)
