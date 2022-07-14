import json

name = input('What is your name?: ')

file = 'Chapter10/username.json'

with open(file, 'w') as f:
  json.dump(name, f)
print(f"We'll remember you {name}")
