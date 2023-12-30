import random
import string
import os
from words_list import WORDS
from hangman_message import MESSAGE
from hangman_animation import animation

    
class Word():
    def __init__(self) -> None:
        # self.secret_word = "Camión".upper()
        self.secret_word = random.choice(WORDS).upper()
        self.stressed_letters = {"Á":"A", "É":"E", "Í":"I", "Ó":"O", "Ú":"U"}
        self.remove_stress_mark()
        self.letters_to_guess = set(self.secret_word)
        self.guessed_letters = set()
        self.allowed_letters = set(string.ascii_uppercase + "Ñ")

    def get_letters_to_guess(self) -> set:
        return self.letters_to_guess
    
    def get_status(self) -> list:
        return [letra if letra in self.guessed_letters else "_" for letra in self.secret_word]
    
    def get_guessed_letters(self) -> set:
        return self.guessed_letters
    
    def get_secret_word(self) -> str:
        return self.secret_word
    
    def is_word_stressed(self):
        return any(l in self.stressed_letters for l in self.secret_word)

    def check_a_letter(self, letter) -> int:
        if letter in self.allowed_letters - self.guessed_letters:
            self.guessed_letters.add(letter)

            if letter in self.letters_to_guess:
                self.letters_to_guess.remove(letter)
                return 0
            else:
                return 1
            
        elif letter in self.guessed_letters:
            return 2
        else:
            return 3
    
    def remove_stress_mark(self):
        if self.is_word_stressed():
            
            modified_word = list(self.secret_word)
            for letter in modified_word:
                if letter in self.stressed_letters:
                    stressed_letter = letter
                    index = modified_word.index(letter)
                    modified_word[modified_word.index(letter)] = self.stressed_letters[letter]
                    
            self.secret_word, modified_word = "".join(modified_word), self.secret_word
            self.stress_mark_data = modified_word, stressed_letter, index
    

class Hangman():
    def __init__(self) -> None:
        animation()
        os.system("clear" if os.name == "posix" else "cls")

        self.word = Word()
        self.vidas = 7
        self.error = ["", "La letra que elegiste no esta en la palabra",
                "Ya escogiste esa letra. Por favor escoge una letra diferente.",
                "Esta letra no es válida"]
        self.error_id = 0
    
    def show_current_status(self):
        print(MESSAGE[self.vidas].format(self.vidas))
        print(" ".join(self.word.get_status()), "\n")
        print(f"Has usado estas letras: {' '.join(self.word.get_guessed_letters())}", "\n")
        print(self.error[self.error_id])
    
    def play_again(self):
        os.system("clear" if os.name == "posix" else "cls")
        answer = ""
        while answer not in ["S","N"]:
            answer = input("¿Quieres jugar de nuevo S o N?\n--> ").upper()
        
        if answer == "S":
            self.__init__()
            self.run()

        
    def game_over(self):
        # El juego llega a esta linea si el jugador adivina todas
        # las letras de la palabra. O si se queda sin vidas.
        os.system("clear" if os.name == "posix" else "cls")
        if self.vidas == 0:
            print(MESSAGE[self.vidas])
            print(f"La palabra era: {self.word.get_secret_word()}")
        else:
            print(f"Exelente, adivinaste la palabra {self.word.get_secret_word()}!")
        input("Presiona la tecla Enter para continuar...")
        self.play_again()

    def run(self):
        # iniciamos el ciclo principal que se ejcuta mientras el suario
        # tenga vidas y le queden letras por adivinar
        while len(self.word.get_letters_to_guess()) > 0 and self.vidas > 0:
            os.system("clear" if os.name == "posix" else "cls")
            self.show_current_status()

            user_input = input("Ingresa una letra: --> ").upper()
            
            self.error_id = self.word.check_a_letter(user_input)
            
            if self.error_id == 1:
                self.vidas -= 1

        self.game_over()


if __name__ == "__main__":
    game = Hangman()
    game.run()