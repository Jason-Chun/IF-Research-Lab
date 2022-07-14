name = 'Chapter10/learn.txt'

with open(name) as file_object:
  thing = file_object.read()
print(thing)

print(f"\n")

with open(name) as file_object:
  for line in file_object:
    print(line)

print(f"\n")

with open(name) as file_object:
  lines = file_object.readlines()
for line in lines:
  print(line)

print(f"\n")

with open(name) as file_object:
  lines = file_object.readlines()
for line in lines:
  new = line.replace('I', 'You')
  print(new)
