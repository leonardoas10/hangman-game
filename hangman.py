import random
import os
import unicodedata

class HangmanGame:
    def __init__(self):
        self.word_to_guess = ''
        self.dashes = ''
        self.word_divided = []
        self.resolving = True
        self.chances = 0

    def read_file(self):
        with open('data.txt', 'r', encoding="utf-8") as f:
            string = random.choice(f.readlines())
            self.word_to_guess = unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode() 
            self.word_divided = [w for w in self.word_to_guess[:-1]]
            self.dashes = ['_' for w in self.word_to_guess[:-1]]
            self.chances = len(self.dashes) + 3

    def guessing(self, letter):
        if letter in self.word_to_guess:
            hints = [i for i,value in enumerate(self.word_divided) if value == letter]
            if len(hints) > 1:
                for hint in hints:
                    self.dashes[hint] = letter
            else:
                index = self.word_divided.index(letter)
                self.dashes[index] = letter
            self.counting_dashes(self.dashes)
        else:
            os.system("clear")
            print('Wrong!, no exist letter', letter)
            self.chances = self.chances - 1
            if self.chances == 0:
                self.resolving = False
                print('YOU ARE LOST, THE WORD IS => ', self.word_to_guess)
                self.play_again()
                
    def counting_dashes(self, dash):
        result = '_' in dash
        if not result:
            self.resolving = False
            os.system("clear")
            print('YOU GUESSED THE WORD => ', self.word_to_guess)
            self.play_again()

        else:
            print('KEEP GOING!')

    def play_again(self):
        answer = input('Do you wanna play again? (Y): ')
        if answer == 'Y':
            self.resolving = True
            self.run()
        else:
            os.system("clear")
            print('Thanks for playing HANGMAN. Atte. Leonardo')

    def run(self):
        try:
            self.read_file()
            print('HANGMAN GAME!', self.word_to_guess)
            while self.resolving:
                print('You have {} strikes less!'.format(self.chances))
                print(self.dashes)
                guess_letter = input('Enter a letter: ')
                print()
                if guess_letter == '' or guess_letter.isnumeric():
                    os.system("clear")
                    print('You must enter a letter!')
                else:
                    self.guessing(guess_letter)
        except ValueError:
            print()

if __name__ == '__main__':
    game = HangmanGame()
    game.run()