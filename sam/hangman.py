import random
import nltk
nltk.download('words')

from nltk.corpus import words

word_list=words.words()

HANGMAN_PICS = ['''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
      |
      |
      |
     ===''']
  
word_list = [word for word in word_list if len(word)>7 and len(word)<12]

target_word = random.choice(word_list)

target_word = target_word.lower()
print(target_word)

wordlist = list(target_word)

print(HANGMAN_PICS[-1])

body = ['leg', 'leg', 'arm', 'arm', 'body', 'head']


word = ['_'] * len(target_word)
print(" ".join(word))

used_letter = []



while body:
  user_input = input(f"Guess the {len(target_word)} letters of the word: ")
  position = 0

  if len(user_input) > 1:
    print("\nOnly one letter at a time please")
    continue

  if user_input in used_letter:
    print(f"\nSorry you already used this letter")
    continue
  
  used_letter.append(user_input)  
  used_letter.sort()
  
  if user_input in target_word:
    for letter in wordlist:
      if user_input == letter:
        word[position] = user_input
      position = position + 1
  else:
    HANGMAN_PICS.pop()
    body.pop()

  print(HANGMAN_PICS[-1])

  print(f"Used letters: {' '.join(used_letter)}")

  print(" ".join(word))

  if word == wordlist:
    print("yay you completed the word")
    print(f"The word was {target_word}")
    break