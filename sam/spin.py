import random
people = ['Jason', 'Philip', 'Jaden']

thing = 3

random_number = random.randint(1,2)

random_two = random.randit(1,1)


if random_number == 0:
  print(f"{people[0]} is 1st")
  del people[0]
  thing = thing-1
elif random_number== 1:
  print(f"{people[1]} is 1st")
  del people[1]
  thing = thing-1
else:
  print(f"{people[2]} is 1st")
  del people[2]
  thing = thing-1

if thing == 2:
  if random_two == 0:
    print(f"{people[0]} is 2nd")
    del people[0]
  else:
    print(f"{people[1]} is 2nd")
    del people[1]

print(f"{people} is 3rd")




#how would you make the code run if there is only 2 values in the list?
