import random

word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list).lower()

print(chosen_word)


blank_list = []
for letter in chosen_word: 
        blank_list += '_'


guess = input("Guess A Letter : ").lower()

for pos in range (0,len(chosen_word)):
    letter=chosen_word[pos]
    if letter == guess:
        blank_list[pos]=letter

print(blank_list)
