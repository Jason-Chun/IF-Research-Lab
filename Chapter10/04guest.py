response = input("What is your name: ")

file = 'Chapter10/guest.txt'

with open(file,'a') as file_object:
  file_object.write(response)