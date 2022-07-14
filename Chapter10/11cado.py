file = 'Chapter10/cat.txt'
file2 = 'Chapter10/dog.txt'
try:
  with open(file , 'r') as f:
    content = f.read()
except FileNotFoundError:
  pass
else:
  print(content)
  
try:
  with open(file2, 'r') as fr:
    contents = fr.read()
except FileNotFoundError:
  pass
else:
  print(f"\n{contents}")