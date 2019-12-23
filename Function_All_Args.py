# def greeting(time_of_day, *args, **kwargs):
#     print(f"Hi {' '.join(args)}, I hope that you are having a good {time_of_day}.")

#     if kwargs:
#         print('Your tasks for the day are:')
#         for key, val in kwargs.items():
#             print(f"{key} => {val}")


# greeting('morning',
#          'Kristine', 'Hudgens',
#          first = 'Empty dishwasher',
#          second = 'Take pupper outside',
#          third = 'Math homework')


# Hi Kristine Hudgens, I hope that you are having a good morning.
# Your tasks for the day are:
# first => Empty dishwasher
# second => Take pupper outside
# third => Math homework

# ---------------------------------------------------------------------
import datetime

def hw_tracker(time_of_day, x, *args, **kwargs):
    print(f"Hi {' '.join(args)}, Let us see if you have any homework for the {time_of_day} of {x}.")

    if kwargs:
        print('Today\'s unfinished assignments are:')
        for key, val in kwargs.items():
            print(f'{key} => {val}')

    # if x = datetime.date.now()
    #     print(x)


hw_tracker('afternoon',
           '12-23-2019',
           'Kristine', 'Hudgens',
           Math = 'Pages 125-126 odd',
           History = 'Pages 500-530',
           English = 'Pages 265-275')


Hi Kristine Hudgens, Let us see if you have any homework for the afternoon of 12-23-2019.
Today's unfinished assignments are:
Math => Pages 125-126 odd
History => Pages 500-530
English => Pages 265-275