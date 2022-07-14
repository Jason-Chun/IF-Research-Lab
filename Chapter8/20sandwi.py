def make(order):
  orde = []
  for orders in order.split(','):
    orde.append(orders)
  print(orde)

order = input("What would you like in your sandwich:")

make(order)