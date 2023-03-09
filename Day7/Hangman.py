import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(logo)

from HangmanWords import word_list

end_of_game = False 
lives=6

chosen_word = random.choice(word_list).lower()

word_length=len(chosen_word)

blank_list = []
for letter in chosen_word: 
        blank_list += '_'


while not end_of_game:
    guess = input("Guess A Letter : ").lower()
    for pos in range (0,len(chosen_word)):
            letter=chosen_word[pos]
            if letter == guess:
                   blank_list[pos]=letter
    if guess not in chosen_word:
           lives-=1
           if lives ==0:
                  end_of_games = True 
                  print("You Lose")

    if "_" not in blank_list:
           end_of_game = True
           print("You Win.")
    print(f"{' '.join(blank_list)}")
    print(stages[lives])

    