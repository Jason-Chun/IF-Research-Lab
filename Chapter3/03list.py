motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[1]
print (motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


motorcycle = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycle.pop()
print(f"The last motorycle I owned was a {last_owned.title()}.")

first_owned = motorcycle.pop(0)
print(f"The first motorycle I owned was a {first_owned.title()}.")

motorcycle.remove('yamaha')
print(motorcycle)