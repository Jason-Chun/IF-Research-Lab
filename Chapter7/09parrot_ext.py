prompt = "\nTell me anything and I will repeat it to you"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
  message = input(prompt)
  if message != 'quit':
    print(message)

active = True
while active:
  message = input(prompt)

  if message == 'quit':
    active = False
  
  else:
    print(message) 