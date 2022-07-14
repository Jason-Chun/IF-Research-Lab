pizza = ['pepperoni', 'meatlovers', 'supereme']
friend_pizza = pizza[:]
pizza.append('cheese')
friend_pizza.append('barbeque')
for pizzas in pizza:
  print(f"\nI like {pizzas} pizza.")
print("\nI really like pizza!")

for p in friend_pizza:
  print(f"\nMy friend likes {p} pizza.")
print("\nMy friend really likes pizza!")

print(pizza)
print(friend_pizza)