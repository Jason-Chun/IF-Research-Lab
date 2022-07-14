repeat = 0
prompt = "\nPlease tell us your age so we can tell you your ticket price for the movie"
prompt += "\nEnter 'quit' when you are done: "


while repeat < 20:

  age = input(prompt)

  if age == 'quit':
    break

  age = int(age)

  if age < 3:
    print("Your ticket is free")
  elif 3 <= age < 12:
    print("Your ticket is $10")
  else:
    print("Your ticket is $15")
  repeat += 1