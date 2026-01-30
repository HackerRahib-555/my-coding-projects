import random
number = random.randint(0, 100)
global lives
lives = 3

     
def gameplay():
    while True:
        number = random.randint(0, 100)

        guess = input('Guess the number: ').strip()
        print(number)
        if int(guess) > number:
            print('Too low!')
            lives -= 1
        elif int(guess) < number:
            print('Too high!')
            lives -= 1
        else:
            print('You guessed it correctly!')
            print(f'The number was: {number}')
            play = input('do you want to play again?').strip().lower()
        if lives == 0:
            print('Game over!')
            print(f'The number was: {number}')
            play = input('do you want to play again?').strip().lower()
        if play.lower() == 'yes':
            continue
        else:
            print("Thank you for Playing!")
            break
           




gameplay()

   