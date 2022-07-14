filename = 'Chapter10/programming.txt'

with open(filename, 'w') as file_object:
  file_object.write('I love programming')
  file_object.write('\nI like games')

with open(filename, 'a') as file_object:
  file_object.write('\nBorb')
  file_object.write('\nRorb')