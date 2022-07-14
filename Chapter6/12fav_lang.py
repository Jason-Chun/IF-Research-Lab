favorite_language = {
    'jen': ['python', 'ruby'],
    'Jaden': ['c'],
    'Jason':['java', 'go'],
    'Philip': ['ruby', 'haskell']
}


for name, languages in favorite_language.items():
  print(f"\n{name.title()}'s favorite languages are:")
  for language in languages:
    print(f"\t{language.title()}")