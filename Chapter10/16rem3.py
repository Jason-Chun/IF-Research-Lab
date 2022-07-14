import json

def get():
  file = 'Chapter10/username.json'
  
  try:
    with open(file) as f:
      username = json.load(f)
  except FileNotFoundError:
    return None
  else:
    return username

def get_new():
  username = input("What is your name?:")
  file = 'Chapter10/username.json'
  with open(file, 'w') as f:
    json.dump(username, f)
  return username

def greet():
  username = get()
  if username:
    print(f"Welcome back {username}")
  else:
    username = get_new()
    print(f"We'll remember you when you come back {username}")
    
greet()