unconfirmed = ['Philip', 'Jaden', 'Jason', 'Jadon']
confirmed = []

while unconfirmed:
  current = unconfirmed.pop()
  print(f"\nVerifying user: {current.title()}")
  confirmed.append(current)

print("The following user have been confirmed: ")
for confirmeds in confirmed:
  print(confirmeds.title())