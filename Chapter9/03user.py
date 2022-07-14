class User:
  def __init__(person, first, last, age):
    person.first = first
    person.last = last
    person.age = age

  def des(person):
    print(f"\nName: {person.first} {person.last}")
    print(f"Age: {person.age}")

  def greet(person):
    print(f"Hello {person.first}")

jason = User('Jason', 'Chun', 14)
philip = User('Philp', 'Park', 14)
jaden = User('Jaden', 'Kang', 13)
joshua = User('Joshua', 'Kang', 14)
jesse = User('Jesse', 'Sohn', 13)
sam = User('Sam', 'Kim', '?')

jason.des()
jason.greet()

philip.des()
philip.greet()

jaden.des()
jaden.greet()

joshua.des()
joshua.greet()

jesse.des()
jesse.greet()

sam.des()
sam.greet()