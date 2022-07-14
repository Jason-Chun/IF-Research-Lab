guests = ['Mom', 'Dad', 'Grandma']
for guest in guests:
  print(f"\nDearest {guest},you are invited to diner at the Jason residents. Please arrive by 6 pm on Saturday.\nSincerely,\nJason")
for guest in guests:
  print(f"\nDearest {guest},I have found another larger table so a few more people will be joining us.\nSincerely,\nJason")

guests.insert(3,'Bryson')
guests.append('Auggie')
guests.append('Jessie')
for guest in guests:
  print(f"\nDearest {guest},you are invited to diner at the Jason residents. Please arrive by 6 pm on Saturday.\nSincerely,\nJason")
removed = guests.pop()
print(f" Dear {removed}, \nyou have been uninvited from the dinner.")
removed = guests.pop(4)
print(f"Dear {removed}, \nyou have been uninvited from the dinner.")
removed = guests.pop(3)
print(f"Dear {removed}, \nyou have been uninvited from the dinner.")
removed = guests.pop(2)
print(f"Dear {removed}, \nyou have been uninvited from the dinner.")
for guest in guests:
  print(f"\nDearest {guest},you are still invited to diner at the Jason residents. Please arrive by 6 pm on Saturday.\nSincerely,\nJason")
print(f"I will be inviting {len(guests)} guests")
del guests[1]
del guests[0]
print(guests)
