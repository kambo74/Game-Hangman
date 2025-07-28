import random as rnd
from data import word_list


word = rnd.choice(word_list).lower().strip()
placeholder = []
position = 0
chances = 13
print(f"Guess chances: {chances}\n")

for letter in word:
    placeholder += "_"


while "".join(placeholder) != word and chances > 0  :
    guess = input("Enter a letter to guess: ").lower().strip()
    for letter in word:
        if letter == guess:
            placeholder[position] = letter
        position += 1
    position = 0
    chances -= 1
    print(f"Guess left: {chances}\n")
    print("".join(placeholder))

if "".join(placeholder) == word :
    print(f"You win this round!")
else:
    print(f"\n \nYou are HANGED! the word was: {word}")
