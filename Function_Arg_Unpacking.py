# def greeting(*args):
#     print('Hi ' + ' '.join(args))


# greeting('Tiffany', 'Hudgens')
# greeting('Kristine', 'M', 'Hudgens')

# Hi Tiffany Hudgens
# Hi Kristine M Hudgens


# def greeting(*args):
#     # print('Hi ' + ' '.join(args))
#     print(args)

# greeting('Tiffany', 'Hudgens')
# greeting('Kristine', 'M', 'Hudgens')

# ('Tiffany', 'Hudgens')
# ('Kristine', 'M', 'Hudgens')


# def greeting(time_of_day, *args):
#     print('Hi ' + ' '.join(args))
  

# greeting('Tiffany', 'Hudgens')
# greeting('Kristine', 'M', 'Hudgens')

# Hi Hudgens
# Hi M Hudgens
# Without an arg for the time of day, python will take the first
# arg and assigning it to the time of day.


def greeting(time_of_day, *args):
    print(f"Hi {' '.join(args)}, I hope that you are having a good {time_of_day}!")
  

greeting('morning', 'Tiffany', 'Hudgens')
greeting('afternoon', 'Kristine', 'M', 'Hudgens')


Hi Tiffany Hudgens, I hope that you are having a good morning!
Hi Kristine M Hudgens, I hope that you are having a good afternoon!