rivers = {
    'Nile' : 'Egypt',
    'Amazon' : 'Brazil',
    'Mississippi' : 'America',
}

for key, value in rivers.items():
  print(f"The {key} is a river that runs through {value}")
for river in rivers.keys():
  print(f"\n{river} {rivers[river]}")
  
for river in rivers.values():
  print(f"\n{river}")