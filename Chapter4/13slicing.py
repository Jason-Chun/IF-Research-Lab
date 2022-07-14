team2 = ['jason', 'philip', 'jaden', 'filler', 'otherfiller', '1', '2', '3']
print(team2[0:3])
print(team2[1:3])
print(team2[:3])
print(team2[2:])
print(team2[-3:])
print(team2[-3:20])
print(team2[0:7:2])
print("Here are the people on team2:")
for team in team2[:3]:
  print(team.title())

my_food = ['taco','ramen', 'pizza', 'burger']
friend_food = my_food[:]
print(my_food)
print(friend_food)
my_food.append('ice cream')
friend_food.append('popcicle')
print(my_food)
print(friend_food)