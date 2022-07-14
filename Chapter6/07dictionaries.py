user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    'blah': 'fermi'
}

for key, value in user_0.items():
  print(f"\nKey: {key}")
  print(f"\nValue: {value}")

for user in user_0.keys():
  print(user.title())

for user in sorted(user_0.keys()):
  print(f"{user} blah")


for user in user_0.values():
  print(user.title())

for user in set(user_0.keys()):
  print(user.title())