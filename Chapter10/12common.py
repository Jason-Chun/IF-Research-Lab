file = 'Chapter10/alice.txt'

with open(file, 'r') as f:
  thing = f.read()
  
other = thing.lower().count('the ')
print(other)