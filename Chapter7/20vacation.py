prompt = "If you could have your dream vacation anywhere, where would it be? "
pol = True
response = {}

while pol:

  name = input("Please state your name: ")

  vaca = input(prompt)

  response[name] = vaca

  next = input("would you like to let someone else take the poll? (yes/no)")
  if next == 'no':
    pol = False

for name, vaca in response.items():
  print(f"{name} would like to vist {vaca}")

