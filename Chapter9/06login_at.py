class User:
  def __init__(person, first, last, age, attempt):
    person.first = first
    person.last = last
    person.age = age
    person.attempt = attempt

  def des(person):
    print(f"\nName: {person.first} {person.last}")
    print(f"Age: {person.age}")

  def greet(person):
    print(f"Hello {person.first}")

  def inc(person):
    person.attempt += 1
    print(person.attempt)

  def reset(person):
    person.attempt = 0
    print(person.attempt)

jason = User('Jason', 'Chun', 14, 1)
philip = User('Philp', 'Park', 14, 1)
jaden = User('Jaden', 'Kang', 13, 1)
joshua = User('Joshua', 'Kang', 14,1)
jesse = User('Jesse', 'Sohn', 13,1)
sam = User('Sam', 'Kim', '?',1)

you = User('you', 'me', 7, 123456789)
you.inc()
you.inc()
you.inc()
you.inc()
you.inc()
you.inc()
you.inc()
you.inc()
you.inc()

you.reset()


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