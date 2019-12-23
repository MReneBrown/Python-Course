# def greeting(**kwargs):
#     print(kwargs)


# greeting()

# {}           This return will be as a dictionary.

#-------------------------------------------------

# def greeting(**kwargs):
#     print(kwargs)


# greeting(first_name = 'Kristine', last_name = 'Hudgens')

# {'first_name': 'Kristine', 'last_name': 'Hudgens'}

#-------------------------------------------

def greeting(**kwargs):
    if kwargs:
        print(f"Hi {kwargs['first_name']} {kwargs['last_name']}, have a great day!")
    else:
        print(f"Hi Guest, have a great day!")



greeting(first_name = 'Kristine', last_name = 'Hudgens')
greeting()

Hi Kristine Hudgens, have a great day!
Hi Guest, have a great day!


