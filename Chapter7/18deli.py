sandwich_orders = ['meatball sub', 'tuna sub', 'ham sub', 'bologna sub', 'turkey sub']
finished_order = []


for sand in sandwich_orders:
  print(f"I'm making the {sand}")
     

while sandwich_orders:
  finish = sandwich_orders.pop(0)
  finished_order.append(finish)

print("\n Sandwiches made")
for wich in finished_order:
  print(f"{wich}")