def formated(first, last):
  full = f"{first} {last}"
  return full.title()
musician =formated('me', 'you')
print(musician)

def form(first, last, middle = ''):
  if middle:
    full = f"{first} {middle} {last}"
  else:
    full = f"{first} {last}"
  return full
music = form('Jason', 'Chun')
print(music)

music = form('jason', 'joonwoo', 'chun')
print(music)
