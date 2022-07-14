def passe(messages):
  while messages:
    borb = messages.pop()
    print(borb)
    rorb.append(borb)

messages = ['hi', 'you', 'are', 'a', 'person', 'maybe']
rorb = []

passe(messages[:])
print(messages)
print(rorb)

passe(messages)
print(messages)
print(rorb)