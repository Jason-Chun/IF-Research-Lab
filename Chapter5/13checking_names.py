current_user = ['me', 'myself', 'I', 'You']
new_user = ['me', 'I', 'rorb', 'bob']

for new in new_user:
  if new in current_user:
    print("This name is take")
  else:
    print("welcome")

#make case sensitive
for new in new_user:
  if new.lower() in [x.lower() for x in current_user]:
    print("This name is take")
  else:
    print("welcome")

