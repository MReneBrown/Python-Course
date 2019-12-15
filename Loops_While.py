def guessing_game():
    while True:
        print('What is your guess?')
        guess = input()

        if guess == '42':
            print('You correctly guessed it!')
            return False
        else:
            print(f'No, {guess} is not the answer, please try again\n')

guessing_game()

What is your guess?
23
No, 23 is not the answer, please try again

What is your guess?
55
No, 55 is not the answer, please try again

What is your guess?
28
No, 28 is not the answer, please try again

What is your guess?
1
No, 1 is not the answer, please try again

What is your guess?
6
No, 6 is not the answer, please try again

What is your guess?
42
You correctly guessed it!