def person(first_n, last_n):
  peep = {'first' : first_n, 'last' : last_n}
  return peep

music = person('Jason', 'Chun')
print(music)

def people(first_n, last_n, age = None):
  peep = {'first' : first_n, 'last' : last_n}
  if age:
    peep['age'] = age
  return peep

musica = people('Jason', 'Chun', age = 14)
print(musica)