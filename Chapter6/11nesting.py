  zalien_0 = {'color':'green','points': 5}
alien_1 = {'color':'yellow','points': 10}
alien_2 = {'color':'red','points': 15}

alien = [alien_0, alien_1, alien_2]

for aliens in alien:
  print(aliens)

alien =[]
for alien_number in range(30):
  new_alien = {'color': 'green', 'points':5, 'speed':'slow', 'ID' : alien_number}
  alien.append(new_alien)

for aliens in alien[:3]:
  if aliens['color'] == 'green':
    aliens['color'] = 'yellow'
    aliens['speed'] = 'medium'
    aliens['points'] = 10
  elif aliens['color'] == 'yellow':
    aliens['color'] = 'red'
    aliens['speed'] = 'fast'
    aliens['points'] = 15

for aliens in alien[:5]:
  print(alien)
print('...')

print(f"Total number of aliens: {len(alien)}")



pizza = {
    'crust':'thick',
    'toppings':['mushrooms', 'extra cheese']
}

print(f"You orders {pizza['crust']} -crust pizza")
for topping in pizza['toppings']:
  print(f"\t{topping}")