import json

def greet():
  file = 'Chapter10/username.json'
  
  try:
    with open(file) as f:
      username = json.load(f)
  except FileNotFoundError:
    username = input("What's your name?:")
    with open(file, 'w') as f:
      json.dump(username, f)
      print(f"We'll remember you when you come back {username}")
  else:
      print(f'Welcome back {username}')

greet()