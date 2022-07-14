file = 'Chapter10/book.txt'

while True:
  response = input('What is you name? If you would like to quit please enter quit: ')

  if response == 'quit':
    break
  else:
    print(f'Hi, {response}')

    with open(file, 'a') as file_object:
      file_object.write(f'\n{response}')