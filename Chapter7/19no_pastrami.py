sandwich_orders = ['meatball sub','pastrami', 'tuna sub', 'ham sub','pastrami', 'bologna sub','pastrami', 'turkey sub']
finished_order = []

for sand in sandwich_orders:
  if sand == 'pastrami':
    print("We are out of pastrami")
    while 'pastrami'in sandwich_orders:
      sandwich_orders.remove('pastrami')
    continue
  print(f"I'm making the {sand}")
     

while sandwich_orders:
  finish = sandwich_orders.pop(0)
  finished_order.append(finish)

print("\n Sandwiches made")
for wich in finished_order:
  print(f"{wich}")