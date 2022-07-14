with open('Chapter10/pi_digits.txt') as file_object:
  contents = file_object.read()
print(contents)

file_name = 'Chapter10/pi_digits.txt'

with open(file_name) as file_object:
  for line in file_object:
    print(f"\n{line}")

with open(file_name) as file_object:
  lines = file_object.readlines()
for line in lines:
  print(f"\n{line.rstrip()}")

pi_string = ''
for line in lines:
  pi_string += line.strip()
print(f"\n{pi_string}")
print(len(pi_string))

file = 'Chapter10/pi_million.txt'

with open(file) as file_object:
  lines = file_object.read()
  pi = ''
  for line in lines:
    pi += line.strip()
  print(f"{pi[:52]}...")
  print(len(pi))

  birthday = input("enter your birthday in mmddyy format: ")

  if birthday in pi:
    print("Your birhtday appears in the first million digits of pi")
  else:
    print("You bday doesn't appear in the first million digits of pi")