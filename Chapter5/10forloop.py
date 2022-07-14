requested_toppings = ['mushroom', 'pepper', 'cheese']

for requested_topping in requested_toppings:
  print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")

requested_toppings = ['mushroom', 'pepper', 'pizza']


for requested_topping in requested_toppings:
  if requested_topping == 'pizza':
    print("we're out of pizza")
  else:
    print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")

requested_pizza = []

if requested_pizza:
  for requested_pizzas in requested_pizza:
    print(f"Adding {requested_pizza}")
  print("\nFinished making your pizza!")
else:
  print("are you sure you want a plain pizza?")

available_topping = ['mushroom', 'olive', 'bell pepper', 'pepperoni']
requested_topping = ['pepperoni', 'pinapple', 'olive']
for requested_toppings in requested_topping:
  if requested_toppings in available_topping:
    print(f"Adding {requested_toppings}")
  else:
    print(f"Sorry we don't have {requested_toppings}")
print("\nYour pizzas ready")