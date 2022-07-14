unprinted = ['phone', 'robot', 'dodo']
completed = []

while unprinted:
  current = unprinted.pop()
  print(f"Printing model: {current}")
  completed.append(current)

print("These have been printed")
for com in completed:
  print(com)