
import random


# The following will choose a random word out of an array to be "winner" word to guess
def pick_a_word():
    word_position = random.randint(0, len(words) - 1)
    return words[word_position]


# Turns a string into a list
def string_to_list(winner_word_list, winner_word_string):
    for winner_word_strings in winner_word_string:
        winner_word_list.append(winner_word_strings)


# Will compare the user's guess letters to the letters of the winner word
def compare(winner_word_list, guess_letters, multiple_underline):
    for winner_word_lists in range(len(winner_word_list)):
        if winner_word_list[winner_word_lists] == guess_letters:
            multiple_underline[winner_word_lists] = guess_letters
    return ' '.join(multiple_underline)


# returns the user's letters that were incorrect
def error(guess_wrong, incorrect_list):
    for listing in guess_wrong:
        incorrect_list.append(listing)
    return ' '.join(wrong_list)


if __name__ == '__main__':

    hang = [
        '''
      _______
      |     |
      O     |
            |
            |
        ========== 
    ''',
        '''
     _______
     |     |
     O     |
     |     |
           |
        ========= 
          ''',
        '''
     _______
     |     |
     O     |
     |\    |
           |
        ========= 
          ''',
        '''
     _______
     |     |
     O     |
    /|\    |
           |
       ========= 
        ''',
        '''
    _______
    |     |
    O     |
   /|\    |
     \    |
       ========= 
        ''',
        '''
    _______
    |     |
    O     |
   /|\    |
   / \    |
       =========
        '''
    ]
    # An array of words, having a animal theme
    words = ['elephant', 'monkey', 'shark', 'dog', 'cat', 'mouse', 'frog', 'lizard', 'snake', 'turtle',
             'bird', 'crab', 'spider', 'lion', 'giraffe', 'penguin', 'eagle', 'chicken', 'beetle', 'cricket', 'goat',
             'sheep','donkey', 'hippo', 'bat', 'camel', 'llama', 'raccoon', 'sloth','buffalo', 'zebra', 'horse', 'rabbit',
             'crocodile', 'shrimp', 'dolphin', 'fish', 'kangaroo'
             ]

    # Variables
    lives_remaining = 7
    correct_word_list = []
    currentNum = 1
    incorrect = 0
    correct_letters = ' '
    underline = []
    wrong_list = []
    winner_word = pick_a_word()
    string_to_list(correct_word_list, winner_word)

    # displays the underline symbol with the exact number to match that of the letters in "winner" word
    for correct_word_lists in correct_word_list:
        multiple_underlines = '_' * len(correct_word_lists)
        underline.append(multiple_underlines)
    print('Lets play hangman!')
    print('Hint: Animals only')
    while True:
        if currentNum < lives_remaining:
            guessed_letters = input("Enter a single letter or enter quit: ")
            if guessed_letters.lower() == "quit":
                print('Have a nice day!')
                break
            elif guessed_letters not in 'abcdefghijklmnopqrstuvwxyz': # Make sure the user enters only alphabet letters
                guessed_letters = input('Please, only enter a letter')

            if guessed_letters in correct_word_list:
                print('You got it')
                correct_letters = compare(correct_word_list, guessed_letters, underline)
                print(correct_letters)
                if correct_letters == ' '.join(correct_word_list):
                    print('Finished')
                    break
            else:
                print('Try again')
                print(error(guessed_letters, wrong_list)) # prints out the users letters that didn't match the winner word
                print(hang[incorrect])
                print(correct_letters)
                incorrect += 1
                currentNum += 1
        else:
            print('You have failed, answer was: ' + winner_word)
            break
