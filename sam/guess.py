
# game that computer generate a random number (1-100)
# user tries to guess and input the guess
# print out if the guess is greater or less than the generated number
# if it is correct, print "Hurray!"


import random

user_level = input("Choose your difficulty from easy, medium, hard: ")
  
if user_input == "hard":
  
elif user_input == "medium":

else:
  


keep_playing = True
while keep_playing:
  random_number = random.randint(1,100)
  #print(random_number)

  #for value in range(1,21):
  while True:
    user_input = input("Choose a number between 1-100: (type quit to end the game)")
    if user_input == "quit":
      keep_playing = False
      break
    user_input = int(user_input)
    print(user_input)

    if random_number == user_input:
      print("Hurray, you got it!")
      break
    elif 0 > user_input or user_input > 100:
      print("this number isn't allowed")
    elif user_input > random_number:
      print("Thats too high.")
    elif user_input < random_number:
      print("Thats too low.")  
  