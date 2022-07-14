import json

file = 'Chapter10/fav.json'

ask = input("What is your favorite number?:")

with open(file, 'w') as f:
  json.dump(ask, f)

with open(file) as f:
  number = json.load(f)

print(f"I can guess your favorite number. Is it {number}?")