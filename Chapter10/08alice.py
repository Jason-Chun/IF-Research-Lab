file = '/home/runner/IF-Research-Lab/Chapter10/alice.txt'

try:
  with open(file, encoding = 'utf-8') as f:
    contents = f.read()
except FileNotFoundError:
  print('no')
else:
  words = contents.split()
  word = len(words)
  print(word)