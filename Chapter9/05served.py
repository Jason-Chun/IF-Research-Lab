class Resturant:
  def __init__(store, name, cuisine):
    store.name = name
    store.cuisine = cuisine
    store.served = 0

  def describe(store):
    print(f"\n{store.name} is big")
    print(f"{store.name} has food")

  def open(store):
    print(f"{store.name} is now open")

  def set(store, served):
    print(served)

  def inc(store, num):
    store.served += num
    print(store.served)

res = Resturant('food', 'korean')
ress = Resturant('eat', 'bulgarian')
resss = Resturant('enjoy' , 'Mexican')
rest = Resturant('thing', 'chinese')

hi = rest.served = 14
print(hi)
rest.set(15)
rest.inc(100)

print(f"The resturants name is {res.name}")
print(f"The resturant has {res.cuisine} food")
res.describe()
res.open()

ress.describe()
resss.describe()