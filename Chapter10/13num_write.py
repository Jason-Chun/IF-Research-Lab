import json

numbers = [1,2,3,4,5,6,7]

file = 'Chapter10/num.json'

with open(file, 'w') as f:
  json.dump(numbers, f)

with open(file) as f:
  num = json.load(f)
print(num)