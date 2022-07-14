def printe(unprinted, completed):
  while unprinted:
    current = unprinted.pop()
    print(f"Printing model: {current}")
    completed.append(current)

def show(completed):
  print("These have been printed")
  for com in completed:
    print(com)

unprinted = ['phone', 'robot', 'dodo']
completed = []

printe(unprinted[:], completed)
show(completed)
print(unprinted)