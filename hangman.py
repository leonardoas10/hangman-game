import random
import os
import unicodedata
from ascii import Ascii


class HangmanGame:
    def __init__(self):
        self.word_to_guess = ''
        self.dashes = ''
        self.word_divided = []
        self.resolving = True
        self.chances = 0
        self.lang = ''
        self.points = 0
        self.records = []

    def read_file(self, lang) -> any:
        """ Read the file depending of your choice: en | es"""
        try:
            file = 'en.txt'
            if lang == 'es':
                file = 'es.txt'

            with open(file, 'r', encoding="utf-8") as f:
                string = random.choice(f.readlines())
                self.word_to_guess = unicodedata.normalize('NFKD', string).encode(
                                    'ASCII', 'ignore').decode()
                self.word_divided = [w for w in self.word_to_guess[:-1]]
                self.dashes = ['_' for w in self.word_to_guess[:-1]]
                self.chances = len(self.dashes) + 3
        except Exception as e:
            print('Error read_file() => ', e)

    def guessing(self, letter):
        """ Return the guess of the word, in case you waste your chances you lose"""
        try:
            if letter in self.word_to_guess:
                hints = [i for i, value in enumerate(self.word_divided)
                        if value == letter] # returns the index of the letter
                if len(hints) > 1: # if the letter exist twice
                    for hint in hints:
                        self.dashes[hint] = letter
                else:
                    index = self.word_divided.index(letter)
                    self.dashes[index] = letter
                self.counting_dashes()
            else:
                os.system("clear")
                print('Wrong!, no exist letter' if self.lang == 'en' else 'No existe la letra', letter)
                self.chances = self.chances - 1
                if self.chances == 0:
                    self.resolving = False
                    Ascii.lose()
                    print('YOU ARE LOST, THE WORD IS =>' if self.lang == 'en' else 'HAS PERDIDO, LA PALABRA ES =>', self.word_to_guess)
                    print('YOUR POINTS WAS {}'.format(self.points) if self.lang == 'en' else 'TU PUNTAJE FUE DE {}'.format(self.points))
                    self.records.append(self.points)
                    print('YOUR RECORDS {}'.format(self.points) if self.lang == 'en' else 'ESTO SON TUS RECORDS {}'.format(self.records))
                    self.play_again()
        except Exception as e:
            print('Error guessing() => ', e)

    def counting_dashes(self):
        """ Count dashes remaining to guess the word."""
        try:   
            result = '_' in self.dashes
            if not result:
                self.resolving = False
                os.system("clear")
                Ascii.win()
                self.points += self.chances
                print('YOU GUESSED THE WORD =>' if self.lang == 'en' else 'HAS ADIVINADO LA PALABRA =>', self.word_to_guess)
                print('YOU WON {} POINTS, YOUR TOTAL IS: {}' if self.lang == 'en' else 'SUMASTE {} PUNTOS, TU TOTAL ES: {}'.format(self.chances, self.points))
                self.play_again()
            else:
                print('KEEP GOING!' if self.lang == 'en' else 'SIGUE ASI!')
        except Exception as e:
            print('Error counting_dashes() => ', e)

    def play_again(self):
        """Ask if you wanna play again"""
        try:
            answer = input('Do you wanna play again? (y): ' if self.lang == 'en' else 'Quieres jugar de nuevo? (s): ').lower()
            if answer == "y" or answer == "s":
                self.read_file(self.lang)
                self.resolving = True
                self.run()
            else:
                os.system("clear")
                Ascii.bye()
                print('Thanks for playing HANGMAN. Atte. Leonardo' if self.lang == 'en' else 'GRACIAS POR JUGAR HANGMAN. Atte. Leonardo')
        except Exception as e:
            print('Error play_again() => ', e)

    def run(self):
        try:
            if not self.lang:
                self.lang = input('Select your language | Selecciona tu lenguaje => english (en) | espanol (es): ').lower()
                assert len(self.lang) > 1, "Select an option | Ingresar una opcion"
                self.read_file(self.lang)
            Ascii.start()
            # print('HANGMAN GAME!', self.word_to_guess)
            print('HANGMAN GAME!')
            while self.resolving:
                print('You have {} strikes less!'.format(self.chances) if self.lang == 'en' else 'Te quedan {} intentos!'.format(self.chances))
                print(self.dashes)
                guess_letter = input('Enter a letter: ' if self.lang == 'en' else 'Ingresa una letra: ')
                print()
                if guess_letter == '' or guess_letter.isnumeric():
                    os.system("clear")
                    print('You must enter a letter!' if self.lang == 'en' else 'Debes de ingresar una letra!')
                else:
                    self.guessing(guess_letter)
        except (Exception, ValueError):
            print()


if __name__ == '__main__':
    game = HangmanGame()
    game.run()
