def pizza(*topping):
  print(topping)

pizza('pepperoni')
pizza('lettuce', 'snails', 'turkey')

def pizzaa(*topping):
  print("\nMaking a pizza with the following toppings:")
  for toppings in topping:
    print(f"- {toppings}")

pizzaa('pepperoni')
pizzaa('lettuce', 'snails', 'turkey')

def pizzaaa(size, *topping):
  print(f"\nMaking {size}-inch pizza with the following toppings:")
  for toppings in topping:
    print(f"- {toppings}")

pizzaaa(12,'pepperoni')
pizzaaa(15, 'lettuce', 'snails', 'turkey')
