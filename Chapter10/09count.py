def count(file):
  try:
    with open(file, 'r') as f:
      contents = f.read()
  except FileNotFoundError:
    pass
  else:
    words = contents.split()
    word = len(words)
    print(f"{file} has {word} words")

file = ['Chapter10/alice.txt', 'Chapter10/book.txt', 'Chapter10/guest.txt', 'Chapter10/learn.txt', 'Chapter10/aerfvewc.txt']
for filename in file:
  count(filename)