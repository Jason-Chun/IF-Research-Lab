file = 'Chapter10/poll.txt'

while True:
  response = input('What is you name? if you would like to quit enter quit: ')

  if response == 'quit':
    break
  else:
    answer = input('cat or dog? c or d: ')
  
    with open(file, 'a') as file_object:
      file_object.write(f"\n{response}:")
      file_object.write(answer)