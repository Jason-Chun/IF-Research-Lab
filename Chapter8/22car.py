def car(manu, model, **other):
  other['manufacturer'] = manu
  other['model'] = model
  return other

thing = car('lamborghini', 'aventador', color = 'black', sticker = 'canada dry')
print(thing)