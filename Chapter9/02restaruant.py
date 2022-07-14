class Resturant:
  def __init__(store, name, cuisine):
    store.name = name
    store.cuisine = cuisine

  def describe(store):
    print(f"\n{store.name} is big")
    print(f"{store.name} has food")

  def open(store):
    print(f"{store.name} is now open")

res = Resturant('food', 'korean')
ress = Resturant('eat', 'bulgarian')
resss = Resturant('enjoy' , 'Mexican')

print(f"The resturants name is {res.name}")
print(f"The resturant has {res.cuisine} food")
res.describe()
res.open()

ress.describe()
resss.describe()