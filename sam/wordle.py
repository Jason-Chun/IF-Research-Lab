import random
import nltk
nltk.download('words')

Turns = 0

from nltk.corpus import words

word_list = words.words()

word_list = [word for word in word_list if len(word)==5]

target_word = random.choice(word_list)
target_word = target_word.upper()
#print(target_word)

# HEADER = '\033[95m'
# OKBLUE = '\033[94m'
# OKCYAN = '\033[96m'
# OKGREEN = '\033[92m' 
# WARNING = '\033[93m'
# FAIL = '\033[91m'
# ENDC = '\033[0m'
# BOLD = '\033[1m'
# UNDERLINE = '\033[4m'

print('You have 6 turns')
didWin = False
while Turns  < 6:
  print(f"\nThis is turn {Turns + 1}")
  
  response = input("Please enter a five letter word: ")
  
  if len(response) != 5:
    print(f"\nThis word is not five letters")
    continue
    
  if response not in word_list:
    print(f"\nThis is not a word")
    continue
    
  response = response.upper()
  
  result = list(response)
  
  target_word_tmp = list(target_word)
  
  for i in range(len(target_word_tmp)):
    if target_word_tmp[i] == response[i]:
      result[i] = f'\033[92m{response[i]}\033[0m'
      target_word_tmp[i] = ' '
      
  for i in range(len(target_word_tmp)):  
    if response[i] in target_word_tmp:
      result[i] = (f'\033[93m{response[i]}\033[0m')
      target_word_tmp[i] = ' '
  
  print(f'\n{"".join(result)}')
  
  Turns += 1

  if response == target_word:
    print("You win")
    didWin = True
    break

if not didWin:
  print(f'You lose. The word was {target_word}')